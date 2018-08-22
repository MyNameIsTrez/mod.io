import async_modio as modio
import asyncio

async def example():
    client = modio.Client(auth="oauth2 token goes here")
    newfile = modio.NewModFile(
            version="0.3.4",
            changelog = "New version which now contains <b> twice as many toilets </b>",
            active=True,
            metadata = "new_file,test_file,crazy"
        )

    newfile.add_file("path/to/file/new_release.zip")

    mod = await client.get_game(234).get_mod(567)
    modfile = await mod.add_file(newfile)

    print(modfile)
    #<modio.ModFile name=new_release.zip version=0.3.4 mod=567>

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
    loop.close()

if __name__ == '__main__':
      main() 