#linked list creating nodes, sample
# class Node:
#     def __init__(self,value=None):
#         self.value=value
#         self.next=None
# class Sinlist:
#     def __init__(self):
#         self.head=None
#         self.tail=None
# a=Sinlist()
# n1=Node(1)
# n2=Node(2)
# a.head=n1
# a.head.next=n2
# a.tail=n2
#up to here

#insertion in linked list

class Node:
    def __init__(self,value=None):
        self.value=value
        self.next=None
class Sinlist:
    def __init__(self):
        self.head=None
        self.tail=None

    def __iter__(self):
        node=self.head
        while node:
            yield node
            node=node.next
    def insertsll(self,value,location):
        newnode=Node(value)
        if self.head is None:
            self.head=newnode
            self.tail=newnode
        else:
            if location==0:
                newnode.next=self.head
                self.head=newnode
            elif location==-1:
                newnode.next = None
                self.tail.next=newnode
                self.tail=newnode
            else:
                i=0
                temp=self.head
                while i<location-1:
                    temp=temp.next
                    i+=1
                nextone = temp.next
                newnode.next = nextone
                temp.next=newnode
                if temp==self.tail:
                    self.tail=newnode
                    newnode.next=None
    def delesll(self,location):
        if location==0:
            s=self.head.next
            self.head=s
            s.head=None
        else:
            i=0
            temp=self.head
            s=temp
            while i<location-1:
                s=temp
                temp=temp.next
                i+=1
            if not temp:
                raise ValueError("Invalid location. The linked list does not have enough elements.")
            a=temp.next
            s.next=a
            if temp == self.tail:
                self.tail = a
    def find(self,value): #returning index of element
        i=0
        s=self.head
        a=True
        while a:
            if s.value==value:
                print(i)
                break
            else:
                s=s.next
                i+=1
                if not s:
                    print("no matching element")
                    break
a=Sinlist()
a.insertsll(1,0)
a.insertsll(12,1)
a.insertsll(13,2)
a.insertsll(24,3)
a.insertsll(123,4)
a.insertsll(6,5)
a.insertsll(5,6)
a.insertsll(0,5)
a.insertsll(44,-1)
print([i.value for i in a])
a.find(1)


print([i.value for i in a])

##do it again





