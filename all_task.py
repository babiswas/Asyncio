import asyncio
from datetime import datetime
from time import sleep

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(3)
   return f"Completed task {str1}"


async def main():
   result1=await task("Wash clothes")
   result2=await task("Drink water")
   result3=await task("Read book")
   result4=await task("Drink water")
   l=list()
   l.extend([result1,result2,result3,result4])
   return l

def super_task():
   def sub_task(str1):
       sleep(3)
       print(f"Performing {str1}")
   sub_task("cleaning room")
   task_status=asyncio.run(main())
   print(task_status)
   sub_task("cleaning car")
   

if __name__=="__main__":
   super_task()

   
   


