# websockets-framework
Collection of solutions for un-documented websockets control over IoT devices with a webui but no montioring app or decently useful API


Method:

  Discover undocumented ws commands:
  - Open browser Developer Tools
  - Browse to device on HTTP. Don’t do HTTPS so you can see the commands.
  - With recording on in the DevTools network tab, login & interact with the webUI
  - In the DevTools, look for and select “ws” and then open the messages tab.
  
  Develop script to automate commands:
  - Record traffic, change in new parameters to match device code
  - Modify script to carry out/poll on device-specific commands
  - May require capturing and scripting the login routine to generate session-specific bullshit (cookies or session IDs or whatever)

Documentation:
- This readme

Dependencies:
- Python: asyncio, websockets, ssl
- Device: Hope you get lucky and the device devs left ws open lol

