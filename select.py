"""Select entity for the My Select Component integration."""
from __future__ import annotations

import logging
from typing import Any

from homeassistant.components.select import SelectEntity
from homeassistant.core import HomeAssistant
from homeassistant.helpers.entity_platform import AddEntitiesCallback
from homeassistant.helpers.typing import ConfigType, DiscoveryInfoType
from homeassistant.config_entries import ConfigEntry

from miio.device import Device

_LOGGER = logging.getLogger(__name__)

# List of available options for the select entity
OPTIONS = ["RGB", "LightMusic0", "LightMusic1", "LightMusic2", "LightMusic3", "LightMusic4", "LightMusic5", "LightMusic6"]
# Initial state
DEFAULT_OPTION = "RGB"

async def async_setup_entry(
    hass: HomeAssistant,
    config: ConfigEntry,
    async_add_entities: AddEntitiesCallback,
    discovery_info: DiscoveryInfoType | None = None,
) -> None:
    """Set up the select platform."""
    async_add_entities([YeelightPanelEntity(hass, config.data)])


class YeelightPanelEntity(SelectEntity):
    """Representation of a select entity."""

    _attr_current_option = DEFAULT_OPTION
    _attr_options = OPTIONS
    _attr_name = "Yeelight Panel Mode"
    DEFAULT_COLOR = 65280

    def __init__(self, hass, config) -> None:
       _LOGGER.info(config)
       self._hass = hass
       self._entity = config['light_entity']
       self._ip = config['ip']
       self._token = config['token']
       self._dev = Device(config['ip'],config['token'])


    async def async_update(self):
        """Fetch the latest state from the device/API."""
        new_state = self._dev.send("get_prop", ["color_mode","light_music"])
        if int(new_state[0]) < 4:
          self._state = "RGB"
        else:
          light_music = int(new_state[1])
          if light_music > 6:
            light_music = 3
          self._state = "LightMusic%s" % (light_music)
          self._attr_current_option = self._state


    def select_option(self, option: str) -> None:
        """Change the selected option."""
        _LOGGER.info(f"Option selected: %s" % (option))
        if option == "LightMusic0":
          self._dev.send("set_ps",["light_music",0])
        if option == "LightMusic1":
          self._dev.send("set_ps",["light_music",1])
        if option == "LightMusic2":
          self._dev.send("set_ps",["light_music",2])
        if option == "LightMusic3":
          self._dev.send("set_ps",["light_music",3])
        if option == "LightMusic4":
          self._dev.send("set_ps",["light_music",4])
        if option == "LightMusic5":
          self._dev.send("set_ps",["light_music",5])
        if option == "LightMusic6":
          self._dev.send("set_ps",["light_music",6])
        if option == "RGB":
          rgb_color = self._dev.send("get_prop", ["rgb"])
          color = rgb_color[0]
          if color == '':
             color = self.DEFAULT_COLOR
          else:
             color = int(color)
          self._dev.send("set_rgb",[color,"smoooth",500])

        self._attr_current_option = option
