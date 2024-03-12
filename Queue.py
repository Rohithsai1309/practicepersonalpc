# using list
class Queue:
    def __init__(self):
        self.items=[]

    def __str__(self):
        values=[str(i) for i in self.items]
        return "->".join(values)
    def isempty(self):
        if self.items ==[]:
            return True
        else:
            return False
    def enqueue(self,value):
        self.items.append(value)
        return "element is inserted at end of queue"
    def dequeue(self):
        if self.items==[]:
            return "element not found"
        else:
            self.items.pop(0)

    def peek(self):
        if self.items==[]:
            return "empty no elements"
        else:
            return self.items[0]


aueue=Queue()
print(aueue.isempty())
print(aueue.enqueue(3))
print(aueue.enqueue(4))
print(aueue.enqueue(1))
print(aueue)
print(aueue.peek())
print(aueue.dequeue())
print(aueue)
print(aueue.peek())