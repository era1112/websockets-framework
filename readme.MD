# websockets-framework
Collection of solutions for un-documented websockets control over IoT devices with a webui but no montioring app or decently useful API


Method:

  Discover undocumented ws commands:
  - Open Developer Tools
  - With recording on in the network tab, login/interact with the webUI
  - Filter to “ws” and messages.
  - Hope there is something in there that you can reuse
  - Console: queryObjects(WebSocket) is useful
  
  Develop script to automate commands:
  - Record traffic, change in new parameters to match device code
  - Modify script to carry out/poll on device-specific commands
  - May require capturing and scripting the login routine to generate session-specific bullshit (cookies or session IDs or whatever)

Documentation:
- This readme

Dependencies:
- Python: asyncio, websockets, ssl
- Device: Hope you get lucky and the device devs left ws open lol

