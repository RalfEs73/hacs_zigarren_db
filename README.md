# Zigarren Datenbank – Home Assistant Integration
Diese Home Assistant Integration ruft die Feuchtigkeitsdaten aus deinem Zigarren-Humidor über die Zigarren-DB API ab.

## ⚙️ Installation
Füge die einzelnen Humidore manuell in deiner `configuration.yaml` hinzu:

```yaml
sensor:
  - platform: zigarren_db
    name: Mein Humidor
	humidor_id: 1
    api: xxxxxxxxxxxx
  - platform: zigarren_db
    humidor_id: 4
    name: Humidorschrank
    api: xxxxxxxxxxxx
    scan_interval: 15
```

## 🪲️ Debugging Code
Füge für das Debugging Log manuell in deiner `configuration.yaml` den Text hinzu:

```yaml
logger:
  default: info
  logs:
    custom_components.zigarren_db: debug
```