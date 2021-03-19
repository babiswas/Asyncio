import asyncio
from datetime import datetime


async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def main():
   print(datetime.utcnow().isoformat())
   res1=await task("Wash Clothes")
   res2=await task("Clean dishes")
   res3=await task("Cook food")
   res4=await task("Groom the floor")
   print(datetime.utcnow().isoformat())
   l=list()
   l.extend([res1,res2,res3,res4])
   return l

if __name__=="__main__":
   tasks=asyncio.run(main())
   print(tasks)
   