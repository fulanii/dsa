{"value": 4, "next": None}

head = {
    "value": 11,
    "next": {"value": 3, "next": {"value": 23, "next": {"value": 7, "next": None}}},
}

# print(head["next"]["next"]["value"]) # 23


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
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value) -> bool:
        """
        Create new node and add to the end
        """
        add_node = Node(value)

        # only checking head coz:
        # head and tail are always in sync by design
        # if you maintain the list correctly,
        # they're either both None (empty list) or both
        # pointing to something (non-empty list).
        # There's no valid state where one is None and the other isn't.
        if self.head is None:  # checking if list empty
            self.head = add_node
            self.tail = add_node
            self.length = 1
        else:
            self.tail.next = add_node
            self.tail = add_node

        self.length += 1
        return True

    def pop(self):
        """
        Remove last node
        """
        if self.head is None:  # empty list
            return None

        if self.head is self.tail:  # only 1 value
            popped = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped.value

        pre = self.head
        temp = self.head

        while temp.next is not None:
            temp = temp.next
            pre = pre.next

        self.tail = pre
        self.tail.next = None

        return pre

    def prepend(self, value):
        """
        Create new node
        and add new node to beginning
        """
        new_node = Node(value)

        if self.head is not None:
            new_node.next = self.head
            self.head = new_node
        else:
            self.head = new_node
            self.tail = new_node

        self.length += 1

    def insert(self, index, value):
        """
        Create new node
        insert at index
        """
        new_node = Node(value)

    def pop_first(self):
        if self.length == 0:
            return None

        current = self.head
        current.next = None
        self.head = self.head.next
        self.length -= 1

        if self.length == 0:
            self.tail = None

        return current

    def get(self, index):

        if index < 0 or index > self.length:
            return None

        current = self.head
        count = 0

        while count != index:
            current = current.next
            count += 1

        return current

    def set_value(self, index, value):
        temp = self.get(index)

        if temp is not None:
            temp.value = value

    def insert_value(self, index, value):
        if index < 0 or index > self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        new_node = Node(value)
        prev = self.get(index - 1)
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return True

    def remove(self, index):
        if index < 0 or index >= self.length:
            return None

        if index == 0:
            return self.pop_first()

        if index == self.length - 1:
            return self.pop()

        prev = self.get(index - 1)

        temp = prev.next

        prev.next = temp.next

        temp.next = None

        self.length -= 1

        return

    def reverse(self):
        temp = self.head

        self.head = self.tail
        self.tail = temp

        before = None
        after = temp.next

        for _ in range(self.length):
            after = temp.next
            temp.next = before # this what reverses it
            before = temp
            temp = after


