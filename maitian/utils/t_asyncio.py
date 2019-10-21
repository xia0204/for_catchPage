import aiohttp
import asyncio

from asyncio import get_event_loop
# import ssl
#
# async def fetch(session,url):
#     async with session.get(url) as response:
#         return await response.text()
#
# async def main():
#     async with aiohttp.ClientSession() as session:
#         html = await fetch(session,"http://www.baidu.com")
#         print(html)

async def test0():
    print("start test0")
    asyncio.sleep(1)
    print("end test0")
async def test1():
    print("start test1")
    asyncio.sleep(2)
    print("end test1")
async def test2():
    print("start test2")
    asyncio.sleep(3)
    print("end test2")
async def main():
    await test0()
    await test1()
    await test2()
if __name__ == "__main__":
    # loop = get_event_loop()
    # loop.run_until_complete(main())
    res = asyncio.gather(test0(),test1(),test2())
    loop = get_event_loop()
    loop.run_until_complete(res)



