import asyncioFunction
import asyncio

async def function():
    print ("1")
    print("2")
async def main():
    await asyncio.gather(asyncioFunction.hello_world(), function())

asyncio.run(main())