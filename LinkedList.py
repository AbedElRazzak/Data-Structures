class Node:
    def __init__(self, data):
        self.data = data
        self.nextNode = None


def printLinkedList(headOfList):
    temp = headOfList
    while temp != None:
        print(temp.data, "- ", end="")
        temp = temp.nextNode


def numberOfElements(headOfList):
    temp = headOfList
    i = 1
    while temp.nextNode != None:
        i += 1
        temp = temp.nextNode
    print("\n", "number of elements: ", i)


node0 = Node(0)
node1 = Node(1)
node2 = Node(2)
node0.nextNode = node1
node1.nextNode = node2
printLinkedList(node0)