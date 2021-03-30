class A:
   def __init__(self,a,b):
       self.a=a
       self.b=b
   def __str__(self):
       return f"{self.a} and {self.b}"

class B:
   def __init__(self,a,b,c):
       self.a=a
       self.b=b
       self.c=c
   def __str__(self):
       return f"{self.a},{self.b} and {self.c}"

if __name__=="__main__":
   l=list()
   l.append(A(1,3))
   l.append(A(2,4))
   l.append(A(6,7))
   obj_list=map(lambda obj:obj.a,l)
   print(list(obj_list))
   str_list=map(lambda obj:str(obj),l)
   print(list(str_list))
   obj1_list=map(lambda obj:obj.__dict__,l)
   print(list(obj1_list))
   k=list()
   k.append(A(5,6))
   k.append(B(1,2,3))
   k.append(A(8,9))
   k.append(B(5,6,7))
   print(list(map(lambda obj2:str(obj2),k)))
   
   




