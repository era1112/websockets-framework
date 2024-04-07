import asyncio
import websockets
import ssl
#import requests

class Flashback():

    def __init__(self):
        self.ip = "a.b.c.d" ## put in your flashback's IP
        self.httpurl = "http://" + self.ip
        self.wsurl = "wss://" + self.ip + "/ws"
        self.username = "admin" ## username
        self.password = "abcd-1234" ## password
        
        # Just tested on non-secure HTTP, will likely work on HTTPS with enough leniancy on the SSL parameters here
        # Using a tls proxy on the client computer might work too
        self.ssl_context = ssl.SSLContext()
        self.ssl_context.check_hostname = False
        self.ssl_context.verify_mode = ssl.CERT_NONE
        self.ws = None

    # Main execution method. Separate from main() to house within asyncio.run() 
    async def run(self):
        async with websockets.connect(self.wsurl,ssl=self.ssl_context,subprotocols=['control']) as self.ws:
            await self.login()
            while True:
                await self.subscribe()
                await self.get_gps()

    # FB login command
    async def login(self):
        message = '{"cmd":"verifyUser","userName":"admin","passWord":"abcd-1234","interface":"new"}'
        await self.ws.send(message)
        result = await self.ws.recv()  # run forever
        print(result)

    # FB needs this subscribe() command. IDK maybe this is common in web development? I'm not a professional lol
    async def subscribe(self):
        message ='{"cmd":"subscribe","all":true}'
        await self.ws.send(message)
        result = await self.ws.recv()  # run forever
        print(result)

    # Purpose: Retrieve most-recent GPS fix
    # Returns: Lat/Long to stdout
    # Future: Should probably return the gps fix as a string instead and then have run() write it out to a parameterizable csv or something
    async def get_gps(self):
        await self.ws.send('{"cmd":"get","ps":["gps_state"]}')
        result2 = await self.ws.recv()
        print(result2)
        await asyncio.sleep(1)


if __name__ == "__main__":
    flashback=Flashback()
    asyncio.run(flashback.run())
    #flashback.run()
