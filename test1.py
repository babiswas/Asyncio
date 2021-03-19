import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained {str1} task")
   await asyncio.sleep(3)
   return f"Completed {str1} task"

async def task_container():
     task_1=asyncio.create_task(task("Clean room"))
     task_2=asyncio.create_task(task("Clean Toilet"))
     task_3=asyncio.create_task(task("Arrange desk"))
     result1=await task_1
     result2=await task_2
     result3=await task_3
     print(result1)
     print(result2)
     print(result3)

if __name__=="__main__":
   asyncio.run(task_container())