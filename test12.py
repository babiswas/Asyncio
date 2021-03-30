import aiohttp
import asyncio

URL="https://captivateprime.adobe.com/primeapi/v2/badges"
headers=dict()
headers["Authorization"]="oauth 6401681362abe7350a7280a80ff73431"

async def task2():
   async with aiohttp.ClientSession() as session:
        async with session.get(URL,headers=headers) as response:
             print(response.status)
             return await response.json()

async def task1(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(3)
   return f"Completed task {str1}"

async def main():
   task_1=asyncio.create_task(task2())
   task_2=asyncio.create_task(task1("hello"))
   return [await task_1,await task_2]
   

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   print(loop.run_until_complete(main()))


