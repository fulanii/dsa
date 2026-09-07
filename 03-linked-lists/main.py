{"value": 4, "next": None}

head = {
    "value": 11,
    "next": {"value": 3, "next": {"value": 23, "next": {"value": 7, "next": None}}},
}

print(head["next"]["next"]["value"]) # 23

class Node:
    """
    A class using to only create new nodes
    """

    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        """
        Use to create new node
        """

        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.lenght = 1




    def append(self, value):
        """
        Create new node and add to the end
        """

    def prepend(self, value):
        """
        Create new node
        and add new node to beginning
        """

    def insert(self, index, value):
        """
        Create new node
        insert at index
        """
