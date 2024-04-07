# websockets-framework
Collection of solutions for un-documented websockets control over IoT devices with a webui but no montioring app or decently useful API


Step 1: Discovering undocumented ws commands:
  Look at old ws messages:
  - Open Developer Tools
  - With recording on in the network tab, login/interact with the webUI
  - Filter to “ws” and messages.
  - Hope there is something in there that you can reuse

  Check for any open websockets:
  - Console: queryObjects(WebSocket)

  Pull mem reference to reuse an existing socket:
  - devtools -> memory -> heap -> search for "websocket" -> right click one, store as local var. Will make a new var called temp?

  Push commands into a socket:
  socketVar.send("Put it in quotes")

Step 2: Develop script to automate commands:
  - Record traffic, change in new parameters to match device code
  - Modify script to carry out/poll on device-specific commands
  - May require capturing and scripting the login routine to generate session-specific bullshit (cookies or session IDs or whatever)

Documentation:
- This readme

Dependencies:
- Python: asyncio, websockets, ssl
- Device: Hope you get lucky and the device devs are using ws in a way you can repurpose

