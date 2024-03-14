class Binarytree:
    def __init__(self,size):
        self.customlist=size*[None]
        self.lastusedindex=0
        self.maxsize=size
    def insertion(self,value):
        if self.lastusedindex+1==self.maxsize:
            return "tree is full"
        self.customlist[self.lastusedindex+1]=value
        self.lastusedindex+=1
        return "added"

    def preordertraversal(self,index,level=0):
        if index>self.lastusedindex:
            return
        else:
            print(" "*level+str(self.customlist[index]))
            level+=1
            self.preordertraversal(2*index,level)
            self.preordertraversal(2*index+1,level)

    def inordertraversal(self,index,level=0):
        if index>self.lastusedindex:
            return
        else:
            level += 1
            self.inordertraversal(2*index,level)
            print(" " * level + str(self.customlist[index]))
            self.inordertraversal(2*index+1,level)

    def postordertraversal(self,index,level=0):
        if index>self.lastusedindex:
            return
        else:
            level += 1
            self.postordertraversal(2*index,level)
            self.postordertraversal(2*index+1,level)
            print(" " * level + str(self.customlist[index]))

    def levelordertraversal(self):
        for i in self.customlist:
            if i is not None:
                print(str(i))

a=Binarytree(8)
a.insertion("DRINKS")
a.insertion("HOT")
a.insertion("COLD")
a.insertion("tea")
a.insertion("coffee")
a.insertion("sprite")
a.insertion("thumsup")
# a.postordertraversal(1)
# print()
# a.inordertraversal(1)
# print()
# a.preordertraversal(1)
#a.levelordertraversal()

