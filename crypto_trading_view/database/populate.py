from asyncio import gather, run
from database.init import create_database
from service._ import create_user, add_favorite

async def populate():
    symbols = ['BTC', 'ETH', 'MATIC', 'AAVE', 'LINK', 'LTC', 'MANA', 'SUSHI', 'XRP']
    await create_database()
    await gather(*[create_user(name=f'name{iterator}') for iterator in range(10)])
    tasks = []

    for iterator in range(10):
        tasks += [add_favorite(user_id=iterator+1,symbols=symbols[index%10]) for index in range(10)]
    
    await gather(*tasks)


run(populate())