#!/usr/bin/python3
"""Class Node that defines a node of a singly linked list."""


class Node:
    """Node of a singly linked list."""
    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get/set the current data of the node."""
        return self.__data

    @data.setter
    def data(self, value):
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get/set the current next_node of the node."""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        if value is None or isinstance(value, Node):
            self.__next_node = value
        else:
            raise TypeError("next_node must be a Node object")


class SinglyLinkedList:
    """Defines a singly linked list."""
    def __init__(self):
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new node in the correct position(increasing order)."""
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
            return
        elif value < self.__head.data:
            new_node.next_node = self.__head
            self.__head = new_node
            return
        else:
            current = self.__head
            while current.next_node:
                if value < current.next_node.data:
                    new_node.next_node = current.next_node
                    current.next_node = new_node
                    return
                current = current.next_node
            current.next_node = new_node

    def __str__(self):
        """Print the singly linked list."""
        current = self.__head
        while current:
            print(current.data)
            current = current.next_node
        return ""
