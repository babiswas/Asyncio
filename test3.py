import asyncio

async def task(str1):
    print(f"Obtained task {str1}")
    await asyncio.sleep(3)
    print(f"Completed task {str1}")

async def main():
   await task("Clean desk")
   await task("Clean Table")
   await task("Cook food")

if __name__=="__main__":
   asyncio.run(main())