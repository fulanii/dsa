# Linked Lists

- [Linked Lists](#linked-lists)
    - [Differences between Linked List and regular List](#differences-between-linked-list-and-regular-list)
    - [Linked List Big O](#linked-list-big-o)
    - [Linked List: Under the hood](#linked-list-under-the-hood)
    - [Linked List: Constructor](#linked-list-constructor)
    - [Linked List: Append](#linked-list-append)
    - [Linked List: Pop](#linked-list-pop)
    - [Linked List: Prepend](#linked-list-prepend)
    - [Linked List: Pop First](#linked-list-pop-first)
    - [Linked List: Get](#linked-list-get)
    - [Linked List: Set](#linked-list-set)
    - [Linked List: Insert](#linked-list-insert)
    - [Linked List: Remove](#linked-list-remove)
    - [Linked List: Reverse (Common interview question)](#linked-list-reverse-common-interview-question)

---

### Differences between Linked List and regular List

1. A Linked List does not have indexes.
2. A List sits in one continuous block of memory. In a Linked List, the nodes are spread all over the place.
3. A Linked List has a variable called `head` which points to the first node, and `tail` which points to the last node. Each node points to the next one, and the last node points to `None`.

```
head                          tail
 |                             |
[11] -> [3] -> [23] -> [7] -> None
```

Since the nodes are spread out all over memory, it looks more like this:

```
        [23] ------> [7] -> None
         ^            ^
[11]     |            |
  \      |           tail
   ---> [3]
  ^
 head
```

A List looks like this, and this is why we can have indexes:

```
index:   0     1     2     3
       [11] [ 3] [23] [ 7]    <- one continuous block of memory
```

---

### Linked List Big O

**Append (add to the end)** `O(1)`: the new node goes after the last node, and `tail` gets moved to point at it. We already have `tail`, so there is no walking.

**Pop (remove from the end)** `O(n)`: each node only knows what comes *after* it, not what comes *before* it. Even though `tail` points directly at the last node, once you remove it you need the node *before* it to become the new tail, and nothing gives you that "before" node directly. You have to walk from `head` to find it.

**Prepend (add to the front)** `O(1)`: the new node points to whatever the old head was, then `head` is reassigned to point at the new node.

**Pop first (remove from the front)** `O(1)`: move `head` forward to the current head's `.next`. The old head gets orphaned (no longer referenced) and Python garbage collects it.

**Insert (add in the middle)** `O(n)`: walk from `head` to the node just before where you want to insert, then splice the new node in. Point it forward to what comes next, then point the previous node at it.

**Remove (remove from the middle)** `O(n)`: same walk as insert, to find the node before the one being removed.

**Lookup** `O(n)`: by value or by index, you have to walk from `head`.

| Operation | Linked List | List |
| --- | --- | --- |
| Append | `O(1)` | `O(1)` |
| Pop (end) | `O(n)` | `O(1)` |
| Prepend | `O(1)` | `O(n)` |
| Pop first | `O(1)` | `O(n)` |
| Insert | `O(n)` | `O(n)` |
| Remove | `O(n)` | `O(n)` |
| Lookup by index | `O(n)` | `O(1)` |
| Lookup by value | `O(n)` | `O(n)` |

---

### Linked List: Under the hood

In a Linked List, a node is essentially a dictionary which contains the value and the pointer:

```python
{
    "value": 4,
    "next": None
}
```

All the previous nodes are also dictionaries, each one nested inside the `next` of the node before it:

```python
head = {
    "value": 11,
    "next": {
        "value": 3,
        "next": {
            "value": 23,
            "next": {
                "value": 7,
                "next": None
            }
        }
    }
}

print(head["next"]["next"]["value"])  # 23
```

---

### Linked List: Constructor

> The constructor just sets up a list with a starting value or an empty one.

```python
new_node = Node(value)   # make the node
self.head = new_node     # only node, so it's the head...
self.tail = new_node     # ...and the tail too
self.length = 1          # keep track of length
```

---

### Linked List: Append

```python
def append(self, value) -> bool:
    """
    Create new node and add to the end
    """
    add_node = Node(value)

    # only checking head because:
    # head and tail are always in sync by design.
    # If you maintain the list correctly,
    # they're either both None (empty list) or both
    # pointing to something (non-empty list).
    # There's no valid state where one is None and the other isn't.
    if self.head is None:  # checking if list empty
        self.head = add_node
        self.tail = add_node
    else:
        self.tail.next = add_node
        self.tail = add_node

    self.length += 1
    return True
```

---

### Linked List: Pop

> `pop()` typically means "remove and return the **last** node". `O(n)`
>
> The 2 edge cases for `pop()` are:
> 1. The Linked List is empty
> 2. It only has 1 node

```python
def pop(self):
    """
    Remove last node
    """
    if self.head is None:  # empty list
        return None

    if self.head is self.tail:  # only 1 node
        popped = self.head
        self.head = None
        self.tail = None
        self.length -= 1
        return popped

    pre = self.head
    temp = self.head

    # pre always stays one step behind temp
    while temp.next is not None:
        pre = temp
        temp = temp.next

    self.tail = pre
    self.tail.next = None
    self.length -= 1

    return temp
```

---

### Linked List: Prepend

> There are three common ways to check if a Linked List is empty, and all of them work if the list is kept consistent:
>
> ```python
> if self.head is None:     # 1. check the pointer
> if self.length == 0:      # 2. check the counter
> if not self.head:         # 3. truthiness
> ```
>
> `self.head is None` is the safest: it checks the actual structure, so it stays correct even if the `length` bookkeeping has a bug.

```python
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
    return True
```

---

### Linked List: Pop First

> Move `head` forward *before* detaching the old head. If you set `current.next = None` first, `self.head.next` is already `None` and the rest of the list is lost.

```python
def pop_first(self):
    if self.length == 0:
        return None

    current = self.head
    self.head = self.head.next
    current.next = None
    self.length -= 1

    if self.length == 0:
        self.tail = None

    return current
```

---

### Linked List: Get

> Indexes start at `0`, so the last node is at `length - 1`. There is nothing at `index == length`, which is why the check is `>=`.

```python
def get(self, index):
    if index < 0 or index >= self.length:
        return None

    current = self.head
    count = 0

    while count != index:
        current = current.next
        count += 1

    return current
```

---

### Linked List: Set

```python
def set_value(self, index, value):
    temp = self.get(index)

    if temp is not None:
        temp.value = value
        return True

    return False
```

---

### Linked List: Insert

> Inserting at `index == length` is valid here (it means "add at the end"), so the check is `>` instead of `>=`.
>
> We grab the node *before* the target position (`index - 1`), because that is the node whose `next` has to change.

```python
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
```

| Method | Valid indexes | Out of range check |
| --- | --- | --- |
| `get`, `set_value`, `remove` | `0` to `length - 1` | `index < 0 or index >= self.length` |
| `insert_value` | `0` to `length` | `index < 0 or index > self.length` |

---

### Linked List: Remove

> Note: Depending on the method, we either return `True`/`False` to show whether the operation succeeded, or return the Node itself (or `None` if there isn't one).

```python
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

    return temp
```

---

### Linked List: Reverse (Common interview question)

> Swap `head` and `tail`, then walk the list flipping each node's `next` to point backwards. Three pointers: `before`, `temp` (current node) and `after`.

```python
def reverse(self):
    temp = self.head

    self.head = self.tail
    self.tail = temp

    before = None
    after = temp.next

    for _ in range(self.length):
        after = temp.next
        temp.next = before  # this is what reverses it
        before = temp
        temp = after
```

---

[^ Top](#linked-lists)
