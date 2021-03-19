import asyncio
from datetime import datetime

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"


async def main():
  print(datetime.utcnow().isoformat())
  status1=await task("Bapan")
  status2=await task("Priyanka")
  print(datetime.utcnow().isoformat())
  print(status1)
  print(status2)

def execute():
   print("Executing task")
   asyncio.run(main())
   def display():
     print("Displaying items")
   display()

if __name__=="__main__":
   execute()


     

