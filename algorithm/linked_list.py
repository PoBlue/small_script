# reference: https://medium.com/@kojinoshiba/data-structures-in-python-series-1-linked-lists-d9f848537b4d

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None # the pointer initially points to nothing

    def traverse(self):
        node = self # start from the head node
        while node != None:
            print(node.val)
            node = node.next

def main():
    node1 = Node(12) 
    node2 = Node(99) 
    node3 = Node(37) 
    node1.next = node2 # 12->99
    node2.next = node3 # 99->37
    # the entire linked list now looks like: 12->99->37
    pass


if __name__ == '__main__':
    main()