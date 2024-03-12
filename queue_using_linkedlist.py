class Node:
    def __init__(self, value=None):
        self.next = None
        self.value = value

    def __str__(self):
        return str(self.value)


class Link:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        x = self.head
        while x:
            yield x
            x = x.next


class Queue:
    def __init__(self):
        self.linkedlist = Link()

    def __str__(self):
        values = [str(i) for i in self.linkedlist]
        return " ".join(values)

    def enqueue(self, value):
        newnode = Node(value)
        if self.linkedlist.head == None:
            self.linkedlist.head = newnode
            self.linkedlist.tail = newnode
        else:
            self.linkedlist.tail.next = newnode
            self.linkedlist.tail = newnode

    def isempty(self):
        if self.linkedlist.head==None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isempty():
            return "empty"
        else:
            temp=self.linkedlist.head
            if self.linkedlist.head==self.linkedlist.tail:
                self.linkedlist.head=None
                self.linkedlist.tail=None
            else:
                self.linkedlist.head=self.linkedlist.head.next
            return temp
    def peek(self):
        x=self.linkedlist.head
        return x




# a = Queue()
# a.enqueue(3)
# a.enqueue(4)
# a.enqueue(6)
# print(a)
# print(a.dequeue())
# print(a)
# print(a.peek())
