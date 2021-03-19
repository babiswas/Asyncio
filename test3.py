import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def main():
  print(datetime.utcnow().isoformat())
  l=list()
  task1=asyncio.create_task(task("Clean Table"))
  task2=asyncio.create_task(task("Cook Food"))
  task3=asyncio.create_task(task("Groom the floor"))
  task4=asyncio.create_task(task("Wash Clothes"))
  result1=await task1
  result2=await task2
  result3=await task3
  result4=await task4
  l.append(result1)
  l.append(result2)
  l.append(result3)
  l.append(result4)
  for obj in l:
    print(obj)
  
  

if __name__=="__main__":
   asyncio.run(main())

  
   