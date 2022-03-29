class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
    
    def hasChildren(self):
        if self.left != None or self.right != None:
            return True
        else:
            return False
    
    def hasAtLeastOneChild(self):
        if self.left != None and self.right != None:
            return False
        else:
            return True
    
    def isMinHeap(self, node, root):
        if node.data > root.data:
            return True
        else:
            return False


class Queue:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        if self.items == None:
            return True
        else:
            return False
    
    def push(self, item):
        if item is not None:
            self.items.append(item)
    
    def remove(self):
        self.items.pop(0)
    
    def printQueue(self):
        print("Queue = ", self.items)


def insertNode(head, node):
    queue = Queue()
    visited = []
    queue.push(head)
    temp = head
    while queue.isEmpty() is False:
        if temp.hasAtLeastOneChild() is True:
            visited.append(temp)
            break
        if temp.hasChildren() is True:
            queue.push(temp.left)
            queue.push(temp.right)
        visited.append(temp)
        if len(queue.items) == 1:
            break
        else:
            queue.remove()
            temp = queue.items[0]

    if temp.left == None:
        temp.left = node
    else:
        temp.right = node

    print("at node: ", temp.data)
    print("left: ", temp.left.data, "right: ", temp.right.data)
    print("\n")
    for i in visited:
        print(i.data, " ", end="")
    print("\n")
    ptr1 = node
    ptr2 = temp
    ptr3 = None
    for ele in visited:
        if ele.left == ptr2 or ele.right == ptr2:
            ptr3 = ele
    print("ptr1: ", ptr1.data, " ptr2: ", ptr2.data, " ptr3: ", ptr3.data)
    while ptr1 != ptr2 and ptr1 != ptr3:
        print("ptr1: ", ptr1.data, " left: ", ptr1.left)
        print("ptr2: ", ptr2.data, " left: ", ptr2.left.data)
        if ptr1.data < ptr2.data:
            print("yes swap them!")
            tempLeft = ptr1.left
            tempRight = ptr1.right
            if ptr2.left == ptr1:
                ptr1.left = ptr2
                ptr1.right = ptr2.right
            elif ptr2.right == ptr1:
                ptr1.right = ptr2
                ptr1.left = ptr2.left
            ptr2.left = tempLeft
            ptr2.right = tempRight
            temp = ptr1
            ptr1 = ptr2
            ptr2 = temp
        print("ptr1: ", ptr1.data, " left: ", ptr1.left)
        print("ptr2: ", ptr2.data, " left: ", ptr2.left.data)
        break

## this code is still in developement