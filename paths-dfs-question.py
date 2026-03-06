############
# Challenge:
#
# Given a binary tree of integers, return all the paths from the tree's root to
# its leaves as an array of strings. The strings should have the following
# format: "root->node1->node2->...->noden", representing the path from root to
# noden, where root is the value stored in the root and node1, node2, ..., noden
# are the values stored in the 1st, 2nd,..., and nth nodes in the path
# respectively (noden representing the leaf).
############

###############
# Node class (please use this in your testing and in your solution)
###############

class Node:
    __slots__ = ['val', 'left', 'right']

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def addLeft(self, node):
        self.left = node

    def addRight(self, node):
        self.right = node


##############
# Test case 1:
#
#           5
#          / \
#         2   3
#        / \
#       10  4
#
# Expected output:  ["5->2->10", "5->2->4", "5->3"].
#
# Code to construct this tree:
# root = Node(5)
# b = Node(2)
# c = Node(3)
# d = Node(10)
# e = Node(4)
# root.addLeft(b)
# root.addRight(c)
# b.addLeft(d)
# b.addRight(e)
##############

##############
# Test case 2:
#
#          10
#         /  \
#        1    2
#            / \
#           3   6
#          / \   \
#         7   9   2

# Expected Output:  ["10->1", "10->2->3->7", "10->2->3->9","10->2->6->2"].
#      
# Code to construct this tree:
#       
# root = Node(10)
# b = Node(1)
# c = Node(2)
# d = Node(3)
# e = Node(6)       
# root.addLeft(b)
# root.addRight(c)
# c.addLeft(d)
# c.addRight(e)
# d.addLeft(Node(7))
# d.addRight(Node(9))
# e.addRight(Node(2))
##########

def create_paths(node):
    paths = []

    def dfs(node, path):
        if node is None:
            return
        
        path.append(node.val)

        if not node.left and not node.right:
            #paths.append("".join([f'{path[i]}->' if i < len(path) - 1 else f'{path[i]}' for i in range(len(path))]))
            paths.append("->".join(map(str, path)))
            return

        if node.left:
            dfs(node.left, path[:])
        
        if node.right:
            dfs(node.right, path[:])
    
    dfs(node, [])
    return paths

root = Node(10)
b = Node(1)
c = Node(2)
d = Node(3)
e = Node(6)       
root.addLeft(b)
root.addRight(c)
c.addLeft(d)
c.addRight(e)
d.addLeft(Node(7))
d.addRight(Node(9))
e.addRight(Node(2))

print(create_paths(root))