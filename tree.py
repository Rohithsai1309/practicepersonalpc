class TreeNode:
    def __init__(self,data,children=[]):
        self.data=data
        self.children=children
    def __str__(self,level=0):
        ret = " " * level + str(self.data)+"\n"
        for i in self.children:
            ret += i.__str__(level+1)
        return ret
    def addchild(self,TreeNode):
        self.children.append(TreeNode)

a=TreeNode(1,[])
b=TreeNode(2,[])
c=TreeNode(3,[])
a.addchild(c)
a.addchild(b)
print(a)










