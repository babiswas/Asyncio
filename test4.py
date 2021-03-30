import asyncio

async def task(str1):
    print(f"Obtained task {str1}")
    await asyncio.sleep(2)
    print(f"Completed task {str1}")


async def main():
   task1=asyncio.create_task(task("Clean table"))
   task2=asyncio.create_task(task("Clean Desk"))
   task3=asyncio.create_task(task("Cook food"))
   await task1
   await task2
   await task3

if __name__=="__main__":
   asyncio.run(main())
