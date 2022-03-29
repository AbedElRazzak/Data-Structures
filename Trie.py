class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}
        self.isVisited = False
        self.nodeIndex = 0

    def childrenAreVisited(self):
        visited = False
        for i in self.children:
            if self.children[i].isVisited == True:
                visited = True
            else :
                visited = False
        return visited
    
    def hasChildren(self):
        if len(self.children) == 0:
            return False
        else:
            return True
    
    def doesFreeCharsExist(self):
        res = False
        for child in self.children:
            if "$" in child or "#" in child:
                continue
            else:
                res = True
        return res
    
    def hasMoreThanOneChar(self):
        numChar = 0
        for child in self.children:
            if "$" in child or "#" in child:
                continue
            else:
                numChar += 1
        if numChar == 1:
            return False
        else:
            return True


class Stack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def remove(self):
        self.items.pop()
    
    def isEmpty(self):
        if self.items is None:
            return True
        else:
            return False

    def printStack(self):
        print("Stack = ", self.items)

      
class Queue:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        self.items.append(item)
    
    def remove(self):
        if len(self.items) != 0:
            self.items.pop(0)
    
    def printQueue(self):
        print("Queue = ", self.items)
    
    def isEmpty(self):
        if self.items == None:
            return True
        else:
            return False





class CompressedTrie:
    def __init__(self):
        self.root = Node(None)
        
    
    def add(self, word, endChar):
        temp = self.root
        word = word + endChar
        while word != "":
            # if the trie is empty
            if len(self.root.children) == 0:
                # print("trie is empty just add the word", word)
                newNode = Node(word)
                self.root.children[word] = newNode
                newNode.nodeIndex = self.root.nodeIndex + 1
                word = ""
                # print(self.root.children)
             # if the trie is NOT empty
            else:
                for childInd, child in enumerate(temp.children):
                    # print("###", child, "in", temp.data)
                    # if the first char of the word exist in the children of temp
                    if word[0] == child[0]:
                        # if the len of the word is Shorter than the selected child
                         if len(word) <= len(child):
                             ind = 0
                             while word[ind] == child[ind]:
                                #  print(word[ind], ind)
                                 if ind < len(child) - 1:
                                     ind += 1
                                 else:
                                     break
                             if child[ind:len(child)] == endChar:
                                 word = ""
                                 print("ERROR word already exist")
                                 break
                             else:
                                #  print("adding", word, "to", child)
                                 baseNode = Node(None)
                                 baseNode.children = temp.children[child].children.copy()
                                 temp.children[child].children.clear()
                                 temp.children[child].data = child[:ind]
                                 baseNode.data = child[ind:len(child)]
                                 temp.children[child].children[child[ind:len(child)]] = baseNode
                                 temp.children[child[:ind]] = temp.children.pop(child)
                                #  baseNode.nodeIndex = temp.children[child[:ind]].nodeIndex + 1
                                 newNode = Node(word[ind:len(word)])
                                 temp.children[child[:ind]].children[word[ind:len(word)]] = newNode
                                #  newNode.nodeIndex = temp.children[child[:ind]].nodeIndex + 1
                                 word = ""
                                 break
                    ## if the len of the word is Longer than the selected child
                         else:
                             ind = 0
                            #  print("word", word,"longer than", child)
                             while word[ind] == child[ind]:
                                #  print(word[ind], ind)
                                 if ind < len(child) - 1:
                                     ind += 1
                                 else:
                                     break
                            #  print("split word to", word[ind + 1:len(word)])
                            #  print("here", child, "\n")
                             if ind == len(child) - 1 and len(temp.children[child].children) != 0:
                                 word = word[ind + 1:len(word)]
                                 temp = temp.children[child]
                                 break 
                             else:
                                 baseNode = Node(None)
                                 baseNode.children = temp.children[child].children.copy()
                                 temp.children[child].children.clear()
                                 temp.children[child].data = child[:ind]
                                 baseNode.data = child[ind:len(child)]
                                 temp.children[child].children[child[ind:len(child)]] = baseNode
                                 temp.children[child[:ind]] = temp.children.pop(child)
                                #  baseNode.nodeIndex = temp.children[child[:ind]].nodeIndex + 1
                                 newNode = Node(word[ind:len(word)])
                                 temp.children[child[:ind]].children[word[ind:len(word)]] = newNode
                                #  newNode.nodeIndex = temp.children[child[:ind]].nodeIndex + 1
                                 word = ""
                                 break
                ## if the first char of the word DOES NOT exist in the children of temp
                    elif childInd == len(temp.children) - 1:
                        newNode = Node(word)
                        temp.children[word] = newNode
                        # newNode.nodeIndex = temp.children[child].nodeIndex + 1
                        word = ""
                        break


    def printTrie(self):
        queue = Queue()
        queue.push(self.root)
        temp = self.root
        while queue.isEmpty() is False:
            print(temp.data, "-> ", temp.children)
            if temp.hasChildren() is True:
                for child in temp.children:
                    queue.push(temp.children[child])
            if len(queue.items) == 1:
                break
            else:
                queue.remove()
                temp = queue.items[0]
        

class SuffixTree:
    def __init__(self):
        self.compressedTrie = CompressedTrie()
        self.root = self.compressedTrie.root
    
    def add(self, word, endChar):
        temp = ""
        for charInd in range(len(word) - 1, -1, -1):
            temp = word[charInd] + temp
            self.compressedTrie.add(temp, endChar)
    
    def printSuffixTree(self):
        self.compressedTrie.printTrie()






class TrieNode:

    def __init__(self,data):
        self.data = data
        self.children = {}
        self.endOfWord = False
        self.charIndex = 0
    
    def hasChildren(self):
        if self.children is None:
            return False
        else:
            return True


class Trie(object):

    def __init__(self):
        self.rootNode = TrieNode(None)
    

    def addToTrie(self, word):
        temp = self.rootNode
        for indCh, ch in enumerate(word):
            if ch in temp.children:
                temp = temp.children[ch]
            elif temp.endOfWord == False:
                newNode = TrieNode(ch)
                temp.children[ch] = newNode
                newNode.charIndex = temp.charIndex + 1
                temp = newNode
        temp.endOfWord = True
    

    def searchWord(self,word):
        temp = self.rootNode
        for indCh, ch in enumerate(word):
            if ch in temp.children:
                temp = temp.children[ch]
        if temp.endOfWord is True and temp.data == word[len(word) - 1] and temp.charIndex == indCh + 1:
            print("the word", word, "is saved in the trie")
        else:
            print("the word", word, "is not saved in the trie")
    

    def printTrie(self):
        queue = Queue()
        queue.push(self.rootNode)
        temp = self.rootNode
        while queue.isEmpty() is False:
            print(temp.data, "-> ", temp.children, temp.charIndex)
            if temp.hasChildren() is True:
                for child in temp.children:
                    queue.push(temp.children[child])
            if len(queue.items) == 1:
                break
            else:
                queue.remove()
                temp = queue.items[0]
            


def depthFS(head):
    stack = Stack()
    visited = []
    stack.push(head)
    visited.append(head.data)
    temp = head
    while stack.isEmpty() is False:
        if temp.hasChildren() is True and temp.childrenAreVisited() is False:
            for childInd in temp.children:
                stack.push(temp.children[childInd])
        elif temp.hasChildren() is False or temp.childrenAreVisited() is True:
            temp.isVisited = True
            visited.append(temp.data)
            stack.remove()
            # if "$" not in temp.data and "#" not in temp.data:
            #     print(temp.data)
        if len(stack.items) == 1:
            break
        else:
            temp = stack.items[len(stack.items) - 1]
        
    print(visited)




