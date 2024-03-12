class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class Circularsll:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        x = self.head
        while x:
            yield x
            x = x.next
            if x == self.tail.next:
                break


    def creatingsll(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node

    def inserting(self,value,position):
        node=self.head
        if node is None:
            print("no elements in list")
        else:
            if position==0:
                newnode=Node(value)
                newnode.next=self.head
                self.head=newnode
                self.tail.next=newnode
            elif position == -1:
                a=Node(value)
                x=self.head
                while x!=self.tail:
                    x=x.next
                a.next = self.tail.next
                x.next=a
                self.tail=a
            else:
                i=0
                x=self.head
                while i<position-1:
                    x=x.next
                    i+=1
                    if x.next == self.tail.next:
                        print(f'location doesnot exist for the position {position}')
                        break
                temp=x.next
                a=Node(value)
                x.next=a
                a.next=temp



a = Circularsll()
a.creatingsll(13)
a.inserting(3,0)
a.inserting(4,1)
a.inserting(42,2)
a.inserting(43,3)
a.inserting(44,-1)
print([i.value for i in a])
