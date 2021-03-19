import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def main():
   print(datetime.utcnow().isoformat())
   l=await asyncio.gather(task("Wash clothes"),task("Cook Food"),task("Watch TV"))
   print(datetime.utcnow().isoformat())
   print(l)

async def main1():
   print(datetime.utcnow().isoformat())
   task1=asyncio.create_task(task("Wash Clothes"))
   task2=asyncio.create_task(task("Clean Table"))
   task3=asyncio.create_task(task("Cook Food"))
   l=await asyncio.gather(task1,task2,task3)
   print(datetime.utcnow().isoformat())
   print(l)
   


if __name__=="__main__":
   asyncio.run(main1())
   