# yeelight_panel
Yeelight Magi Light Panel HomeAssistant integration addon

[Yeelight Smart LED Light Panel](https://en.yeelight.com/product/smart-led-light-panels/)

Provides additional entity to control embedded music backlight modes. 

Not to be confused with music_mode available in the local integration protocol, this integration controls the built-in music backlight modes available in Yeelight Smart LED Panel.

Unfortunately, control of these modes is not available via LAN protocol, so to use it you need to connect the device to Mi Home cloud and get token to control device from HomeAssistant.

# Installation
1. Configure standard [Yeelight HomeAssistant integration](https://www.home-assistant.io/integrations/yeelight/) first, which allows to control RGB modes 
2. Clone repository to you HomeAssistant custom_components directory, as custom_components/yeelight_panel
3. Restart HomeAssistant
4. Add Integration from HomeAssistant: Devices & services > Integrations > + Add Integration > Magi Panel

Methods for obtaining Mi Home token are described [here](https://github.com/shaarkys/com.xiaomi-miio/blob/master/docs/obtain_token.md).

Choose your main Yeelight Panel entity created on step 1, specify ip-address in local network and Mi Home token.

5. Use new Select Entity to switch between LightMusic and RGB modes. 

