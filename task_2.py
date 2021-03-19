import asyncio
from datetime import datetime


async def task(str1):
    print(f"Obtained task {str1}")
    await asyncio.sleep(2)
    return f"Completed task {str1}"

async def main():
   print(datetime.utcnow().isoformat())
   task1=asyncio.create_task(task("Clean the Floor"))
   task2=asyncio.create_task(task("Cook Food"))
   task3=asyncio.create_task(task("Clean dishes"))
   l=list()
   l.extend([await task1,await task2,await task3])
   print(datetime.utcnow().isoformat())
   return l

if __name__=="__main__":
   task_list=asyncio.run(main())
   print(task_list)
