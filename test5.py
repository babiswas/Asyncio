import asyncio

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   print(f"Completed task {str1}")

async def main():
   await asyncio.gather(task("Complete book1"),task("Complete book2"),task("Complete book3"))

if __name__=="__main__":
   asyncio.run(main())