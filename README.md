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

## Original Project

**Source code:** https://github.com/aquaticus/esphome-snmp

**Documentation:** https://aquaticus.info/snmp.html

**Integration tests:** https://github.com/aquaticus/esphome_snmp_tests

**Latest tested ESPHome version:** [2026.8.1](https://esphome.io/changelog/2026.8.0/)
