# Zigarren Datenbank
Diese Home Assistant Integration ruft die Feuchtigkeitsdaten aus deinem Zigarren-Humidor über die Zigarren-DB API ab.

## Installation

Füge die Integration manuell in deiner `configuration.yaml` hinzu:

```yaml
sensor:
  - platform: zigarren_db
    humidor_id: 1
    name: Mein Humidor

  - platform: zigarren_db
    humidor_id: 4
    name: Humidorschrank
	scan_interval: 15
```


