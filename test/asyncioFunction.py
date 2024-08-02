import asyncio

async def hello_world():
    print("Hello")
    await asyncio.sleep(5)
    print("World")