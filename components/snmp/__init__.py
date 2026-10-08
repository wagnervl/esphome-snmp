from esphome.const import CONF_ID
from esphome.components import sensor
import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.core import CORE

CODEOWNERS = ["@aquaticus"]

# No ethernet support at the moment
DEPENDENCIES = ["wifi"]

snmp_ns = cg.esphome_ns.namespace("snmp")
SNMPComponent = snmp_ns.class_("SNMPComponent", cg.Component)

CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(SNMPComponent),
            cv.Optional("contact", default=""): cv.string_strict,
            cv.Optional("location", default=""): cv.string_strict,
            **{
                cv.Optional(f"data{i}"): cv.use_id(sensor.Sensor)
                for i in range(1, 10)
            },
        }
    ),
    cv.only_with_arduino,
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])

    cg.add(var.set_location(config["location"]))
    cg.add(var.set_contact(config["contact"]))

    for i in range(1, 10):
        data_id = config.get(f"data{i}")
        if data_id:
            data_sensor = await cg.get_variable(data_id)
            cg.add(var.set_data_sensor(i - 1, data_sensor))

    await cg.register_component(var, config)

    if CORE.is_esp32:
        cg.add_library("WiFi", None)

    if CORE.is_esp8266 or CORE.is_esp32:
        cg.add_library(
            r"https://github.com/aquaticus/Arduino_SNMP.git",
            "2.1.0",
        )
