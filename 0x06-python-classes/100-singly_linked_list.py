#!/usr/bin/python3
"""defines a node of a singly linked list"""


class Node:
    """defines a node of a singly linked list.

    Attributes:
        data (int): The data of the current Node.
        next_node (Node): The next node of the current node
    """

    def __init__(self, data, next_node=None):
        """Initialize a new Node instance

        Args:
            data (int): The data for the new Node.
            next_node (Node): The next node of the new node.
        """
        self.data = data
        self.next_node = next_node

    @property
    def data(self):
        """Get data"""
        return self.__data

    @data.setter
    def data(self, value):
        """Set data

        Args:
            value (int): new data value

        Raises:
            TypeError: If value is not an integer
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """Get next_node"""
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """Set next_node.

        Args:
            value (Node): The next node of the current node.

        Raises:
            TypeError: If value is not a Node or None.
        """
        if not isinstance(value, Node) and value is not None:
            raise TypeError("next_node must be a Node object")
        self.__next_node = value


class SinglyLinkedList:
    """defines a singly linked list"""

    def __init__(self):
        """Initialize a SinglyLinkedList"""
        self.__head = None

    def sorted_insert(self, value):
        """Inserts a new Node into the correct sorted position in the list"""

        curr = self.__head
        new = Node(value)

        if self.__head is None:
            self.__head = new
            return

        if curr.data > value:
            new.next_node = curr
            self.__head = new
            return

        while curr.next_node and curr.next_node.data < value:
            curr = curr.next_node

        tmp = curr.next_node
        curr.next_node = new
        new.next_node = tmp

    def __str__(self):
        """Define the print() representation of a SinglyLinkedList."""
        curr = self.__head
        res = []
        while curr:
            res.append(str(curr.data))
            curr = curr.next_node
        return '\n'.join(res)
