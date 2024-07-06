t = (1, "t", 3.14, False)  # tuple can contain different data types, tuple is immutable
print(t[0])  # prints 1
print(t[0:2])  # prints (1, 't'), same slicing methods as strings

# tuple methods
# count() method
print(t.count(1))  # returns the number of occurrences of 1 in the tuple

# index() method
print(t.index(1))  # returns the index of the first occurrence of 1 in the tuple (will throw an error if the element is not in the tuple)

# tuple concatenation
t2 = (1, "t", 3.14, False)
t3 = t + t2  # concatenates t and t2
print(t3)

# tuple packing and unpacking
t = (1, "t", 3.14, False)
(a, b, c, d) = t  # unpacks the tuple into variables a, b, c, and d
print(a)  # prints 1
print(b)  # prints 't'
print(c)  # prints 3.14
print(d)  # prints False

# tuple packing
t = 1, 2, 3, 4  # tuple packing
print(t)  # prints (1, 2, 3, 4)
