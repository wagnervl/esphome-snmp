# SNMP component for ESPHome

This is an external ESPHome component that enables support for the SNMP protocol. The protocol is widely used in network management and network monitoring.

## ESP32-C3 Compatibility

This fork includes a compatibility fix for ESP32-C3 devices.

The original component attempts to include `esp_himem.h`, which is not supported by the ESP32-C3 architecture. This inclusion has therefore been disabled for ESP32-C3, while preserving the original behavior for supported ESP32 variants.

This change allows the SNMP component to compile successfully on ESP32-C3 devices.

### Tested with

- ESP32-C3 SuperMini
- ESPHome
- SNMP component from Aquaticus

## Generic Sensor Data

This fork supports exposing up to nine ESPHome sensors through SNMP.

The sensors can be configured using `data1` through `data9`:

```yaml
snmp:
  contact: "TEST"
  location: "TEST"
  data1: temperatura
  data2: umidade
  data3: tensao
```

Each configured sensor is exposed through a dedicated SNMP OID:

| Data  | SNMP OID                  |
|-------|---------------------------|
| data1 | `1.3.9999.32.10.1.0`     |
| data2 | `1.3.9999.32.10.2.0`     |
| data3 | `1.3.9999.32.10.3.0`     |
| data4 | `1.3.9999.32.10.4.0`     |
| data5 | `1.3.9999.32.10.5.0`     |
| data6 | `1.3.9999.32.10.6.0`     |
| data7 | `1.3.9999.32.10.7.0`     |
| data8 | `1.3.9999.32.10.8.0`     |
| data9 | `1.3.9999.32.10.9.0`     |

Sensor values are exposed as integer values multiplied by 10.

For example:

```text
ESPHome sensor: 23.7
SNMP value:     237
```

The scaling factor can then be applied by the monitoring system, such as Zabbix.

### Example

```yaml
sensor:
  - platform: bmp280_i2c
    address: 0x76
    temperature:
      name: "Temperatura"
      id: temperatura
    update_interval: 10s

snmp:
  contact: "TEST"
  location: "TEST"
  data1: temperatura
```

The value can be tested with:

```bash
snmpget -c public -v 2c <ESP_IP> 1.3.9999.32.10.1.0
```

## Original Project

**Source code:** https://github.com/aquaticus/esphome-snmp

**Documentation:** https://aquaticus.info/snmp.html

**Integration tests:** https://github.com/aquaticus/esphome_snmp_tests

**Latest tested ESPHome version:** [2026.9.1](https://esphome.io/changelog/2026.9.0/)
