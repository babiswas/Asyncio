import functools
class A:
  def __init__(self,a,b):
      self.a=a
      self.b=b
  def __str__(self):
      return f"{self.a} and {self.b}"

def getitem(obj):
   return obj.a

if __name__=="__main__":
   l=[A(2,3),A(5,6),A(7,8),A(0,1),A(3,5),A(4,7)]
   bigger_obj=functools.reduce(lambda obj1,obj2:max(obj1,obj2,key=getitem),l)
   print(bigger_obj)

