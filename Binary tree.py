import random
class Node():
    def __init__(self,key):
        self.key = key
        self.left = None
        self.right = None
    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)
    def _display_aux(self):
        #Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2

Root = Node(10)
treeSize = 10
node = Root
left = []
right = []
used = [10]

def GetKey(): #Random key generation
    nodekey = random.randint(0,20)
    while(nodekey in used):
        nodekey = random.randint(0,20)
    return(nodekey)

def AddNode():
    global Root
    node = Root
    newNode = int(input("Input an integer"))
    newNode = Node(newNode)
    placed = False
    while not placed:
        if newNode.key < node.key:
            if node.left != None:
                node = node.left
            else:
                node.left = newNode
                placed = True
        elif newNode.key > node.key:
            if node.right != None:
                node = node.right
            else:
                node.right = newNode
                placed = True
                    
            
def ShowTree():
    Root.display()


## Create Binary Tree ##
nodekey = GetKey()
while(treeSize > 0):
    if nodekey < node.key:
        if node.left != None:
            node = node.left
        else:
            node.left = Node(nodekey)
            treeSize = treeSize - 1
            used.append(nodekey)
            nodekey = GetKey()
            node = Root
    elif nodekey > node.key:
        if node.right != None:
            node = node.right
        else:
            node.right = Node(nodekey)
            treeSize = treeSize - 1
            used.append(nodekey)
            nodekey = GetKey()
            node = Root

## Display Binary Tree##
Root.display()
