#This example shows how to gain an OAuth 2 Access Token through the Email Authentication Flow to gain Write access
import async_modio
import asyncio

async def auth()
    client = async_modio.Client(api_key="your api key here")

    #request a security code be sent at this email adress
    await client.email_request("necro@mordor.com")

    #check your email for the security code
    code = input("Code: ")

    oauth2 = await client.email_exchange(code)

    #your oauth2 token is now stored in the variable

    #to save simply
    with open("oauth2.txt", "w") as f:
        f.write(oauth2)

    #and now the token is stored in oauth2.txt

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(auth())
    loop.close()

if __name__ == '__main__':
      main() 

