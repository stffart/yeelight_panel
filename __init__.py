import logging

from homeassistant.core import HomeAssistant
from homeassistant.config_entries import ConfigEntry
from .const import DOMAIN
_LOGGER = logging.getLogger(__name__)

async def async_setup_entry(hass: HomeAssistant, config: ConfigEntry) -> bool:
    """Set up component integration."""
    # Load the select platform entities
    await hass.config_entries.async_forward_entry_setups(config, ["select"])
    return True
