import asyncio
import aiofiles
import time

async def task(str1):
   print(f"Obtained task {str1}")
   await asyncio.sleep(2)
   return f"Completed task {str1}"

async def main():
    task1=asyncio.create_task(task("Clean desk"))
    task2=asyncio.create_task(task("Cook food"))
    task3=asyncio.create_task(task("Clean floor"))
    result=await task1
    result1=await task2
    result2=await task3
    return [result,result1,result2]

async def read_file(filename):
      async with aiofiles.open("test1.txt",mode='r') as file:
           content=await file.read()
      return content


async def main1():
   task1=asyncio.create_task(read_file("test1.txt"))
   task2=asyncio.create_task(read_file("test2.txt"))
   return [await task1,await task2]

async def read_file_line(filename):
   l=list()
   async with aiofiles.open(filename,mode='r') as files:
       async for line in files:
           l.append(line)
   return l

async def main2():
   task_list=[asyncio.create_task(read_file("test1.txt")) for i in range(8000)]
   return [await task for task in task_list]

def file_read(filename):
    content=''
    with open(filename) as file:
       content=file.read()
    return content


async def task4():
  async with aiofiles.open('test1.txt',mode='r') as file:
     content=await file.read()
  return content

async def task5():
   task11=asyncio.create_task(task("hello"))
   return await task11

async def main4():
   return await asyncio.gather(task4(),task5())
       
print("Displaying asynchronously")          
time1=time.time()  
loop=asyncio.get_event_loop()
loop.run_until_complete(main4())
print(time.time()-time1)


print("Displaying Synchronously")
time1=time.time()
l=[file_read("test1.txt") for i in range(8000)]
print(time.time()-time1)
