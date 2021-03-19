import asyncio
from datetime import datetime

async def task(str1):
    print(f"Obtained task {str1}")
    await asyncio.sleep(2)
    return f"Completed task {str1}"

async def main():
   finished,pending=await asyncio.wait([task("chop Vegie"),task("Cook chicken"),task("Serve plates")],return_when=asyncio.ALL_COMPLETED)
   for obj in finished:
      print(obj.result())

if __name__=="__main__":
   asyncio.run(main())

          

