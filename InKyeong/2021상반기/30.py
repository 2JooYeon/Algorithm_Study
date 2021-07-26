class Tree:
    def __init__(self, key):
        self.data = key
        self.left = None
        self.right = None
 
def isBST(root, l = None, r = None):
 
    if (root == None) :
        return True
 
    if (l != None and root.data != None and l.data != None and root.data <= l.data) :
        return False
 
    if (r != None and root.data != None and r.data != None and root.data >= r.data) :
        return False

    return isBST(root.left, l, root) and \
        isBST(root.right, root, r)
 
 
# Driver Code
if __name__ == '__main__':
    root = Tree(8)
    root.left = Tree(3)
    root.right = Tree(9)
    root.right.left = Tree(None)
    root.right.right = Tree(None)
    root.right.left.left = Tree(4)
    root.right.left.right = Tree(7)
    if (isBST(root,None,None)):
        print("It Is BST")
    else:
        print("It is not BST")

