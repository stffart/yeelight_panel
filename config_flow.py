from homeassistant import config_entries
from .const import DOMAIN
import voluptuous as vol
import homeassistant.helpers.config_validation as cv
from homeassistant.helpers.selector import selector
from miio.device import Device

class YeelightPanelConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    """Config flow."""
    # The schema version of the entries that it creates
    # Home Assistant will call your migrate method if the version changes
    VERSION = 1
    MINOR_VERSION = 1
    async def async_step_user(self, info):
        errors = {}
        if info is not None:
          unique_id = 'yeelight_pane_%s' % info['light_entity']
          await self.async_set_unique_id(str(unique_id))
          self._abort_if_unique_id_configured()

          #test availability
          try:
            dev = Device(info['ip'],info['token'])
            dev.send("get_prop", ["power"])
            return self.async_create_entry(
                    title="%s" % (unique_id), data=info
                  )
          except Exception as e:
            errors['base'] = str(e)

        return self.async_show_form(
            step_id="user", data_schema=vol.Schema({vol.Required("light_entity"): selector({ "entity": { "domain": "light" } }), vol.Required("ip"): str, vol.Required("token"): str}), errors=errors
        )
