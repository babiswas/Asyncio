class A:
  def __init__(self,num):
      self.num=num
  def __iter__(self):
      if not hasattr(A,'threshold'):
         self.threshold=6
      return self
  def __next__(self):
      if self.num>self.threshold:
         raise StopIteration("Number greater than threshold")
      else:
         item=self.num
         self.num=self.num+1
         return item

if __name__=="__main__":
   obj=A(4)
   ptr=iter(obj)
   print(next(ptr))
   print(next(ptr))
   print(next(ptr))
   print(next(ptr))
   print(next(ptr))