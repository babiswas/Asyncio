class Node:
   def __init__(self,value):
       self.value=value
       self.left=None
       self.right=None

   def inorder(self):
       if self:
          if self.left:
             self.left.inorder()
          print(self.value)
          if self.right:
             self.right.inorder()

   def vertical_order_traversal(self):
       top_view=list()
       bottom_view=list()
       queue=[]
       vert_list=dict()
       queue.append((self,0))
       while queue:
           obj,index=queue.pop(0)
           if index not in vert_list:
              vert_list[index]=[]
           vert_list[index].append(obj.value)

           if obj.left:
              queue.append((obj.left,index-1))
           if obj.right:
              queue.append((obj.right,index+1))
       for ptr in sorted(vert_list.keys()):
               top_view.append(vert_list[ptr][0])
               bottom_view.append(vert_list[ptr][-1])
       print("The top view of the tree is")
       print([val for val in top_view])
       print("The bottom view of the tree is")
       print([val for val in bottom_view])
                      
   def insert(self,value):
       if self.value>value:
          if self.left:
             self.left.insert(value)
          else:
             self.left=Node(value)
       elif self.value<value:
           if self.right:
              self.right.insert(value)
           else:
              self.right=Node(value)
       else:
          print("Duplication not allowed")

if __name__=="__main__":
   node=Node(12)
   node.insert(6)
   node.insert(10)
   node.insert(4)
   node.insert(2)
   node.insert(5)
   node.insert(11)
   node.insert(9)
   node.insert(20)
   node.insert(18)
   node.insert(25)
   node.insert(23)
   print("The inorder traversal of the node is")
   node.inorder()
   print("The vertical order traversal of the tree is")
   node.vertical_order_traversal()
   
   