class Queue:
    def __init__(self, maxsize):
        self.items = [None] * maxsize
        self.start = -1
        self.top = -1
        self.maxsize = maxsize

    def __str__(self):
        values = [str(i) for i in self.items]
        return " ".join(values)
    def isempty(self):
        if self.top == -1:
            return True
        else:
            False

    def isfull(self):
        if self.top + 1 == self.start:
            return True
        elif self.top == 0 and self.start == -1:
            return True
        else:
            return False

    def enqueue(self, value):
        if self.isfull():
            return "it is full"
        else:
            if self.top + 1 == self.maxsize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "element is added at end of queue"


    def dequeue(self):
        if self.isempty():
            return "it is empty"
        else:
            firstelement=self.items[self.start]
            start=self.start
            if self.start==self.top:
                self.start=-1
            elif self.start+1==self.maxsize:
                self.start=0
            else:
                self.start+=1
                self.items[start]=None
            return firstelement

#peek,delete can do
a = Queue(3)

a.enqueue(1)
a.enqueue(2)
a.enqueue(3)
a.enqueue(4)
print(a.dequeue())
print(a)
