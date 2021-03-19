import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def all_task():
   print(datetime.utcnow().isoformat())
   finished,pending=await asyncio.wait([task("Clean clothes"),task("Clean room"),task("Clean house")],return_when=asyncio.ALL_COMPLETED)
   print(datetime.utcnow().isoformat())
   for obj in finished:
      print(obj.result())
   


if __name__=="__main__":
       asyncio.run(all_task())
          
   