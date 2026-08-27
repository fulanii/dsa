a = [1, 2, 3]
b = a
print(a is b) # True: same object, two names
print(id(a), id(b)) # a: 4394755584, b: 439475558


x = 5
y = x
y += 1
print(x, y) # 5 6


s1 = "hello"
s2 = s1
s2 += " world"
print(s1) # "hello"  unchanged

# Strings can't be edited in place. 
# s2 += " world" builds a whole new string object.


lst1 = [1, 2, 3]
lst2 = lst1
lst2.append(4)
print(lst1) # [1, 2, 3, 4] changed!

# lst2 and lst1 are the same object. 
# .append() mutates that object in place
# there's only one list, with two names on it.