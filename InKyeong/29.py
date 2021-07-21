from random import randint
class Node:
    def __init__(self, data):
        self.item = data
        self.ref = None

class LinkedList:
    def __init__(self):
        self.start_node = None

    def traverse(self):
        if self.start_node is None:
            print("List has no element")
            return
        else:
            n = self.start_node
            while n is not None:
                print(n.item , " ")
                n = n.ref

    def append(self, data):
        new_node = Node(data)
        if self.start_node is None:
            self.start_node = new_node
            return
        n = self.start_node
        while n.ref is not None:
            n= n.ref
        n.ref = new_node

    def insert(self, index, data):
        if index == 1:
            new_node = Node(data)
            new_node.ref = self.start_node
            self.start_node = new_node
        else :
            i = 1
            n = self.start_node
            while i < index-1 and n is not None:
                n = n.ref
                i = i+1
            if n is None:
                print("Index out of bound")
            else: 
                new_node = Node(data)
                new_node.ref = n.ref
                n.ref = new_node

    def delete_element_by_value(self, x):
        if self.start_node is None:
            print("The list has no element to delete")
            return 0

        # Deleting first node 
        if self.start_node.item == x:
            self.start_node = self.start_node.ref
            return 1

        n = self.start_node
        while n.ref is not None:
            if n.ref.item == x:
                break
            n = n.ref

        if n.ref is None:
            return 0
        else:
            n.ref = n.ref.ref
            return 1
    
    def remove(self, index) :
        if self.start_node is None:
            print("The list has no element to delete")
            return 0
        if index == 1:
            self.start_node = self.start_node.ref
            return 1

        i = 2
        n = self.start_node
        while n.ref is not None:
            if i == index:
                break
            i += 1
            n = n.ref

        if n.ref is None:
            return 0
        else:
            n.ref = n.ref.ref
            return 1
   

    def delete(self, x) :
        a = 1
        while (a == 1) :
            a = self.delete_element_by_value(x)
        
    def reverse(self):
        prev = None
        n = self.start_node
        while n is not None:
            next = n.ref
            n.ref = prev
            prev = n
            n = next
        self.start_node = prev

    def check_duplicates(self):
        if self.start_node is None:
            return 0
        n = self.start_node
        count = 0
        lists = []
        while n is not None:
            count = count + 1
            lists.append(n.item)
            n = n.ref
        w_count= {}
        for lst in lists:
            try: w_count[lst]+= 1
            except: w_count[lst]=1

        for k, v in w_count.items() :
            if v>1 :
                for _ in range(v-1):
                    self.delete_element_by_value(k)
        

random_linkedlist = LinkedList()
for _ in range(0, 20) :
    inputnum = randint(1, 50)
    random_linkedlist.append(inputnum)
random_linkedlist.traverse()
print("------------")
random_linkedlist.check_duplicates()
random_linkedlist.traverse()

