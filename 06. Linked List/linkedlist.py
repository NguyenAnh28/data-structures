
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

class LinkedList: # LinkedList class to manage the linked list operations
    def __init__(self):
        self.head = None