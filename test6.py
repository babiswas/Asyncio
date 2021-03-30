import asyncio

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def main():
   completed,pending =await asyncio.wait([task("Clean Table"),task("Clean Desk"),task("Cook Food")],return_when=asyncio.ALL_COMPLETED)
   print([obj.result() for obj in completed])
   print([obj.result() for obj in pending])

if __name__=="__main__":
   asyncio.run(main())
