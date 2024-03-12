import queue_using_linkedlist as q


class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftchild = None
        self.rightchild = None


newbt = TreeNode("DRINKS")
leftchild = TreeNode("HOT")
a = TreeNode("coffe")
b = TreeNode("tea")
c = TreeNode("sprite")
d = TreeNode("thumsup")
rightchild = TreeNode("COLD")
newbt.leftchild = leftchild
newbt.rightchild = rightchild
leftchild.leftchild = a
leftchild.rightchild = b
rightchild.leftchild = c
rightchild.rightchild = d


def preordertraversal(rootnode, level=0):
    if not rootnode:
        return
    print(" " * level + rootnode.data)
    level += 1
    preordertraversal(rootnode.leftchild, level)
    preordertraversal(rootnode.rightchild, level)


# preordertraversal(newbt)

def inordertraversal(rootnode, level=0):
    if not rootnode:
        return
    level += 1
    inordertraversal(rootnode.leftchild, level)
    print(" " * level + rootnode.data)
    inordertraversal(rootnode.rightchild, level)


#inordertraversal(newbt)

def postordertraversal(rootnode, level=0):
    if not rootnode:
        return
    level += 1
    postordertraversal(rootnode.leftchild, level)
    postordertraversal(rootnode.rightchild, level)
    print(" " * level + rootnode.data)


# postordertraversal(newbt)


def levelordertraversal(rootnode):
    if not rootnode:
        return
    else:
        customqueue = q.Queue()
        customqueue.enqueue(rootnode)
        while not customqueue.isempty():
            root = customqueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customqueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customqueue.enqueue(root.value.rightchild)

#levelordertraversal(newbt)
