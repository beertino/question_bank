##########
#Task 3.1#
##########

class Node:

    # constructor()
    def __init__(self, data):
        self.data = data
        self.leftPtr = -1
        self.rightPtr = -1

    # modifier methods
    def setData(self, s):
        self.data = s

    def setLeftPtr(self, x):
        self.leftPtr = x

    def setRightPtr(self, y):
        self.rightPtr = y

    # accessor methods
    def getData(self):
        return self.data

    def getLeftPtr(self):
        return self.leftPtr

    def getRightPtr(self):
        return self.rightPtr
    

# define class Tree
class Tree:

    # define and initialise attributes of class Tree
    def __init__(self):
     
        # the tree data
        self.tree = []

        # index for the root position of the tree array
        self.root = -1

        # index for the next unused node
        self.NextFreePosition = 0

    # inserts a new item into the binary tree structure
    def add(self, newItem):
        self.tree.append(Node(newItem))
        if self.root == -1:
            self.root = self.NextFreePosition
            self.NextFreePosition = 1
        else:
            # traverse the tree to find the position for the new value
            CurrentPosition = self.root
            LastMove = 'X'
            PreviousPosition = -1
            while CurrentPosition != -1:
                PreviousPosition = CurrentPosition
                if newItem < self.tree[CurrentPosition].data:
                    # move left
                    LastMove = 'L'
                    CurrentPosition = self.tree[CurrentPosition].leftPtr
                else:
                    # move right
                    LastMove = 'R'
                    CurrentPosition = self.tree[CurrentPosition].rightPtr
             
            if LastMove == 'R':
                self.tree[PreviousPosition].rightPtr = self.NextFreePosition
            else:
                self.tree[PreviousPosition].leftPtr = self.NextFreePosition

            self.NextFreePosition += 1

    # output

    #### format this however you want, as long as it's legible ####
    def Print(self):
        print('{0:12}{1:12}{2:12}{3}'.format('Node Index','Data','Left Ptr','Right Ptr'))

    # for each node
        for node in self.tree:
            print('{0:^12}{1:<12}{2:^12}{3:^12}'.format(self.tree.index(node),node.data,node.leftPtr,node.rightPtr))
            
# Task 3.3
# to output the data stored in the tree in reverse order
    def postOrderTraversal(self, root = 0):
        if self.tree[root].leftPtr is not -1:
            self.postOrderTraversal(self.tree[root].leftPtr)
        if self.tree[root].rightPtr is not -1:
            self.postOrderTraversal(self.tree[root].rightPtr)
        print(self.tree[root].data)


# main
NewTree = Tree()
NewTree.add("Tiger")
NewTree.add("Lemur")
NewTree.add("Bat")
NewTree.add("Yak")
NewTree.add("Ostrich")
NewTree.add("Raccoon")
NewTree.add("Macaw")
NewTree.add("Zebra")
#NewTree.Print()

NewTree.postOrderTraversal()
