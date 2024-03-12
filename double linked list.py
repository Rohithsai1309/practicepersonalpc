class Node:
    def __init__(self, value):
        self.value = value
        self.previous = None
        self.next = None


class doublell:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next


    def __reversed__(self):
        node=self.tail
        while node:
            yield node
            node=node.previous

    def inserting(self, value, position):
        if self.head == None:
            node = Node(value)
            self.head = node
            self.tail=node
        else:
            if position == 0:
                node = Node(value)
                node.next=self.head
                self.head.previous=node
                self.head=node
            elif position==-1:
                node=Node(value)
                node.previous=self.tail
                self.tail.next=node
                self.tail=node
            else:
                i=0
                temp=self.head
                while i<position-1 and temp.next!=None:
                    i+=1
                    temp=temp.next
                nextnode=temp.next
                node=Node(value)
                node.next=nextnode
                node.previous=temp
                nextnode.previous=node
                temp.next=node


a = doublell()
a.inserting(1, 0)
a.inserting(98,0)
a.inserting(2, 1)
a.inserting(55, 2)
a.inserting(66,3)
a.inserting(6,4)
a.inserting(33,5)
print([i.value for i in a])
print([i.value for i in reversed(a)])
