import asyncio
import aiohttp


class Endpoint:
   def __init__(self,l):
      self.iter1=iter(l)
   def __aiter__(self):
      return self
   async def __anext__(self):
      await asyncio.sleep(0)
      try:
        object=next(self.iter1)
      except StopIteration:
        raise StopAsyncIteration
      return object

async def main(endpoint):
   API_URL="https://captivateprimeqe.adobe.com/primeapi/v2/"+endpoint
   headers={"Authorization":"oauth "+"7b9a1a5f7417565865dbf69efee30e85"}
   async with aiohttp.ClientSession() as session:
       async with session.get(API_URL,headers=headers) as resp:
            if resp.status==200:
               return await resp.json()
            else:
               raise Exception


async def request():
   l=list()
   API_URL="https://captivateprimeqe.adobe.com/primeapi/v2/"
   headers={"Authorization":"oauth "+"7b9a1a5f7417565865dbf69efee30e85"}
   endpoints=["badges","catalogs"]
   async with aiohttp.ClientSession() as session:
       async for path in Endpoint(endpoints):
           async with session.get(API_URL+path,headers=headers) as resp:
              if resp.status==200:
                l.append(await resp.json())
              else:
                raise Exception
   return l


async def master_task():
    task1=asyncio.create_task(main("badges"))
    task2=asyncio.create_task(main("catalogs"))
    tasklist=[await task1,await task2]
    return tasklist

async def main1():
  completed,pending=await asyncio.wait([main("badges"),main("catalogs")],return_when=asyncio.ALL_COMPLETED)
  print([obj.result() for obj in completed])
  print([obj.result() for obj in pending])


async def main2():
   return await asyncio.gather(main("badges"),main("catalogs"))

if __name__=="__main__":
   loop=asyncio.get_event_loop()
   print(loop.run_until_complete(request()))





            