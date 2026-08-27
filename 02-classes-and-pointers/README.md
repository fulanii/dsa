> Classes skipped already familiar with python classes and oop
> 

### Pointers

> The core model: everything is a reference
> 

In Python, every variable is a name that points to an object in memory, never the object itself. 
Assignment (=) never copies data, It just makes a name point to an existing object.

```python
a = [1, 2, 3]
b = a
print(a is b) # True: same object, two names
print(id(a), id(b)) # a: 4394755584, b: 439475558
```

is checks identity (same object in memory), while == checks equality (same value).

### The dividing line: mutable vs. immutable

This is the single most important concept. It's not about the type category (number vs. list), it's about whether the object can be changed in place once created.

| Immutable (safe to share) | Mutable (shared = shared changes) |
| --- | --- |
| `int`, `float`, `bool` | `list` |
| `str` | `dict` |
| `tuple` | `set` |
| `frozenset` | custom objects (by default) |

**Immutable types:** once created, the object itself can never change. Any "modification" actually creates a brand new object.

```python
x = 5
y = x
y += 1
print(x, y) # 5 6
```

`y += 1` doesn't touch the `5` object, it makes `y` point to a new object `6`. `x` still points to the original `5`, untouched.

Same logic applies to strings:

```python
s1 = "hello"
s2 = s1
s2 += " world"
print(s1) # "hello"  unchanged

# Strings can't be edited in place. 
# s2 += " world" builds a whole new string object.
```

**Mutable types:** the object itself can be changed without creating a new one, and every name pointing to it sees the change.

```python
lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1) # [1, 2, 3, 4] changed!

# lst2 and lst1 are the same object. 
# .append() mutates that object in place
# there's only one list, with two names on it.
```