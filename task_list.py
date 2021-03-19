import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def all_tasks():
   print(datetime.utcnow().isoformat())
   return await asyncio.gather(task("Clean Clothes"),task("Repair Car"),task("Read Book"))

if __name__=="__main__":
   task_list=asyncio.run(all_tasks())
   print(datetime.utcnow().isoformat())
   print(task_list)


   