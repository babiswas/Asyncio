import asyncio
from datetime import datetime

async def task(str1,n):
   print(f"Obtained task {str1}")
   await asyncio.sleep(n)
   return f"Completed task {str1}"

async def main():
   for obj in asyncio.as_completed([task("Clean Car",3),task("Gardening",2),task("Cook food",4)]):
      result=await obj
      print(result)

if __name__=="__main__":
   asyncio.run(main())

