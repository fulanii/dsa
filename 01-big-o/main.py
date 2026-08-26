def print_items(n):
    for i in range(n): # O(n)
        print(i)

# print_items(10)

def print_items(n):
    for i in range(n): # runs n times
        print(i)

    for j in range(n):  # runs n times
        print(j)

# print_items(10)

def print_items(n):
    for i in range(n):
        for j in range(n): 
            print(i, j)

# print_items(10) ## O(n^2)

def print_items(n):
    for i in range(n): # O(n²)
        for j in range(n): 
            print(i, j)

#             + 

    for k in range(n): # O(n)
        print(k)

# print_items(10) # O(n² + n) -> O(n²)

def add_items(n):
    return n + n + n

# print(add_items(10)) # O(1)

def count_halvings(n):
    count = 0
    while n > 1:
        n = n // 2 # cut n in half each time
        count += 1
    return count

# print(count_halvings(16)) # O(log n)

def print_items(a, b):
    for i in range(a): # runs a times
        print(i)

    for j in range(b):  # runs b times
        print(j)

# print_items(10, 100)


def print_items(a, b):
    for i in range(a):
        for j in range(b): 
            print(i, j)

# print_items(10, 100) # O(a * b)