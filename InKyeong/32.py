class Node():
    def __init__(self, data):
        self.data = data
        self.parent = self.left = self.right = None
        self.color = 'red'
          
class RedBlackTree:
    
    def grandparent_node(self,node):
        if (node != None and node.parent != None):
            return node.parent.parent
        else:
            return None
    
    def uncle_node(self,node):
        grandparent_node = self.grandparent_node(node)
        if grandparent_node == None:
            return None
    
        if node.parent == grandparent_node.left:
            return grandparent_node.right
        else:
            return grandparent_node.left
        
    def insert_1(self,node):
        if node.parent == None:
            node.color = 'black'
        else:
            self.insert_2(node)
        
    def insert_2(self,node):
        if node.parent.color == 'black':
            return
        else:
            self.insert_3(node)
    
    def insert_3(self,node):
        uncle = self.uncle_node(node)
    
        if (uncle != None and uncle.color == 'red'):
            node.parent.color = 'black'
            uncle.color = 'black'
            grandparent = self.grandparent_node(node)
            grandparent.color = 'red'
            self.insert_1(grandparent)
        else:
            self.insert_4(node)
    
    def insert_4(self,node):
        
        grandparent = self.grandparent_node(node)
    
        if(node == node.parent.right and node.parent == grandparent.left):
            self.rotate_left(node.parent)
            node = node.left
        elif (node == node.parent.left and node.parent == grandparent.right):
            self.rotate_right(node.parent)
            node = node.right
    
        self.insert_5(node)
    
    def rotate_left(self,node):
        c = node.right
        p = node.parent
    
        if (c.left != None):
            c.left.parent = node
    
        node.right = c.left
        node.parent = c
        c.left = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
    
        if (p != None):
            if (p.left == node):
                p.left = c
            else:
                p.right = c

    def rotate_right(self,node):
        c = node.left
        p = node.parent
    
        if (c.right != None):
            c.right.parent = node
    
        node.left = c.right
        node.parent = c
        c.right = node
        c.parent = p
        
        if c.parent == None:
            self.root = c
            
        if (p != None):
            if (p.right == node):
                p.right = c
            else:
                p.left = c
     
    def insert_5(self,node):
        grandparent = self.grandparent_node(node)
    
        node.parent.color = 'black'
        grandparent.color = 'red'

        if (node == node.parent.left):
            self.rotate_right(grandparent)
        else:
            self.rotate_left(grandparent)

            
    def __init__(self):
        self.root = None
        self.inserted_node = None
	
    def insert(self, data, parent_node):
        self.root = self.insert_value(self.root, data, parent_node)
        self.insert_1(self.inserted_node)
        return 
    
    def insert_value(self, node, data, parent_node):
        if node is None:
            node = Node(data)
            node.parent = parent_node
            self.inserted_node = node
        else:
            if data <= node.data:
                node.left = self.insert_value(node.left,data,node)
            else:
                node.right = self.insert_value(node.right,data,node)
        return node
    
    def find(self,search_key):
        return self.find_value(self.root, search_key)
    
    def find_value(self, root, search_key):
        if root is None or root.data == search_key:
            return root 
        elif search_key > root.data:
            return self.find_value(root.right, search_key)
        else:
            return self.find_value(root.left, search_key)      

rbt = RedBlackTree()

a = [41, 38, 31, 12, 19, 8]
    
for x in a:
    rbt.insert(x,None)
    
def check(node):
    if not node.left  == None : check(node.left)
    if node.parent != None:
        print('key: ', node.data, '/ parents: ', node.parent.data, '/ color: ', node.color, end = '\n')
    else:
        print('key: ', node.data, '/ parents: ', node.parent, '/ color: ', node.color, end = '\n')
    if not node.right == None : check(node.right)

check(rbt.root)