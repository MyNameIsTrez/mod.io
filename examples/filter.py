import async_modio as modio
import asyncio

async def example():
    client = modio.Client(api_key="api key goes here")
    filters = modio.Filter()

    filters.text("The Lord of the Rings")
    #This will return every result where the name column contains any of 
    #the following words: 'The', 'Lord', 'of', 'the', 'Rings'

    filters.equals(id=10)
    # Get all results where the id column value is 10.

    filters.like(name="The Witcher*")
    #Get all results where 'The Witcher' is succeeded by any value

    filters.not_like(name="*Asset Pack")
    #Get all results where Asset Pack NOT is proceeded by any value.

    filters.values_in(id=[3,11,16,29])
    #Get all results where the id column value is 3, 11, 16 and 29.

    filters.sort("name")
    #Sort name in ascending order

    filters.sort("id", reverse=True)
    #Sort id in descending order

    filters.limit(20)
    #limit to 20 results

    filters.offset(5)
    #skip the first five results

    games, pagination_metadata = await client.get_games(filter=filters)
    #returns all the result that meet the above criteria

def main():
    loop = asyncio.get_event_loop()
    loop.run_until_complete(example())
    loop.close()

if __name__ == '__main__':
      main()  
