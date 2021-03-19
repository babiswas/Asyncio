import asyncio
from datetime import datetime

async def task(str1,n):
   print(f"Obtained task {str1}")
   await asyncio.sleep(n)
   return f"Completed task {str1}"

async def main():
   for task_status in asyncio.as_completed([task("Wash clothes",2),task("Clean shirts",1),task("clean floor",4)]):
       result=await task_status
       print(result)

if __name__=="__main__":
   asyncio.run(main())