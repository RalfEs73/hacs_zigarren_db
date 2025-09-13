from homeassistant.components.sensor import SensorEntity
from homeassistant.helpers.aiohttp_client import async_get_clientsession
import logging

_LOGGER = logging.getLogger(__name__)

async def async_setup_platform(hass, config, async_add_entities, discovery_info=None):
    humidor_id = config.get("humidor_id")
    api = config.get("api", "")  # Zusätzlicher Parameter für die URL
    name = config.get("name", f"Humidor {humidor_id}")
    
    if humidor_id is not None and api:
        async_add_entities([ZigarrenHumidorSensor(hass, humidor_id, api, name)])
    else:
        _LOGGER.error("humidor_id oder api fehlt in der Konfiguration.")

class ZigarrenHumidorSensor(SensorEntity):
    def __init__(self, hass, humidor_id, api, name):
        self.hass = hass
        self._humidor_id = humidor_id
        self._api = api
        self._attr_name = name
        self._attr_native_unit_of_measurement = "%"
        self._attr_device_class = "humidity"
        self._attr_native_value = None
        self._attr_extra_state_attributes = {}

    async def async_update(self):
        session = async_get_clientsession(self.hass)
        url = f"https://zigarren-db.de/api/ha_humidor_test.php?humidor_id={self._humidor_id}&api={self._api}"
        headers = {
            "Accept": "application/json",
            "User-Agent": "HomeAssistant/2025.9"
        }

        try:
            async with session.get(url, headers=headers) as response:
                content_type = response.headers.get("Content-Type", "")
                if "application/json" in content_type:
                    data = await response.json()
                    _LOGGER.debug("API-Daten für Humidor %s: %s", self._humidor_id, data)

                    feuchtigkeit = data.get("feuchtigkeit")
                    self._attr_native_value = float(feuchtigkeit) if feuchtigkeit else None

                    self._attr_extra_state_attributes = {
                        "temperatur": float(data.get("temperatur", 0)),
                        "zigarren_lagernd": int(data.get("zigarren_lagernd", 0)),
                        "health": int(data.get("health", 0)),
                        "label": data.get("label", ""),
                        "api": self._api  # Optional: API-Parameter als Attribut anzeigen
                    }
                else:
                    _LOGGER.error("Unerwarteter Content-Type: %s", content_type)
                    self._attr_native_value = None
        except Exception:
            _LOGGER.exception("Fehler beim Abrufen der API")
            self._attr_native_value = None
