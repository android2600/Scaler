class Linked_List:
    def __init__(self) -> None:
        self.head=None
        self.length=0

class Node:
    def __init__(self,data) -> None:
        self.value=data
        self.next=None

class Operations:
    def __init__(self) -> None:
        self.list_array=[]
        self.curr=None
        self.prev=None
        self.llist=Linked_List()

    def add(self,value):
        new=Node(value)
        new.next=self.llist.head
        self.llist.head=new
        self.llist.length+=1

    def append(self,value):
        temp=self.llist.head
        while temp.next!=None:
            temp=temp.next
        temp.next=Node(value)
        self.llist.length+=1


    def insert(self,value,index):
        if index>self.llist.length:
            return
        elif index==0:
            self.add(value)
            return
        else:
            self.curr=self.llist.head
            c=0
            while c<index and self.curr!=None:
                self.prev=self.curr
                self.curr=self.curr.next
                c+=1
            new_node=Node(value)
            self.prev.next=new_node
            new_node.next=self.curr
            self.llist.length+=1

    def delete(self,index): 
        if index>=self.llist.length:
            return
        
        if index==0:
            if self.llist.length==0:
                return
            else:
                self.llist.head=self.llist.head.next
                self.llist.length-=1
        
        elif index==self.llist.length-1:
            temp=self.llist.head
            while temp.next!=None:
                self.prev=temp
                temp=temp.next
            self.prev.next=None
            self.llist.length-=1
        
        else:
            self.curr=self.llist.head
            c=0
            while c<index and self.curr!=None:
                self.prev=self.curr
                self.curr=self.curr.next
                c+=1
            self.prev.next=self.curr.next
            self.llist.length-=1

    def print(self):
        self.list_array=[]
        temp=self.llist.head
        while(temp):
            self.list_array.append(str(temp.value))
            temp=temp.next
        print(self.list_array,self.llist.length)

test1=Operations()
test1.add("Hello")
test1.append("World")
test1.append("!!")
test1.print()
test1.insert("Earth",1)
test1.insert("People",4)
test1.print()
test1.delete(2)
test1.print()

