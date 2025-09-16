# Zigarren Datenbank – Home Assistant Integration
Diese Home Assistant Integration ruft die Feuchtigkeitsdaten aus deinem Zigarren-Humidor über die Zigarren-DB API ab.

## ⚙️ Installation
Füge die einzelnen Humidore manuell in deiner `configuration.yaml` hinzu:

```yaml
sensor:
  - platform: zigarren_db
    name: Mein Humidor
    humidor_id: 1
    api: x-xxxxxxx-xxxxxxx-xxxxxxx
  - platform: zigarren_db
    humidor_id: 4
    name: Humidorschrank
    api: x-xxxxxxx-xxxxxxx-xxxxxxx
    scan_interval: 300  # Optional - Alle 5 Minuten (300 Sekunden)
```

## 🪲️ Debugging Code
Füge für das Debugging Log manuell in deiner `configuration.yaml` den Text hinzu:

```yaml
logger:
  default: info
  logs:
    custom_components.zigarren_db: debug
```