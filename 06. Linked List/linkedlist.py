
"""
What is a linked list? 

A linked list is a linear data structure where each element (node) contains a value and
a reference (or link) to the next node in the sequence. Unlike arrays, linked lists do not
store elements in contiguous memory locations, allowing for efficient insertions and deletions.
 
"""

# Ways to initialize a linked list

class Node: # Node class to represent each element in the linked list
    def __init__(self, data):
        self.data = data
        self.next = None

node1 = Node(15) # Creating a node with value 1
node2 = Node(22) # Creating a node with value 2 
node3 = Node(54) # Creating a node with value 3
node4 = Node(2) # Creating a node with value 4

node1.next = node2
node2.next = node3
node3.next = node4


head = node1

current = head
while current:
    print(current.data, end=" -> ") 
    current = current.next
print("None")