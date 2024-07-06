# integer
x = 1

# float
y = 2.8

# string
z = "hello"

# boolean
a = True

# list
b = ["apple", "banana", "cherry"] # mutable data type

# tuple
c = ("apple", "banana", "cherry") # immutable data type

# range
d = range(6) # sequence of numbers from 0 to 5 (by default)
d = range(2, 6) # a sequence of numbers from 2 to 5

# dictionary
e = {"name" : "John", "age" : 36} # key-value pairs (mutable)

# set
f = {"apple", "banana", "cherry"} # unordered collection of unique items (mutable)

# frozenset
g = frozenset({"apple", "banana", "cherry"}) # unordered collection of unique items (immutable)

# bytes
h = b"Hello" # immutable sequence of bytes (0 <= x < 256)

# bytearray
i = bytearray(5) # mutable sequence of bytes (0 <= x < 256)

# memoryview
j = memoryview(bytes(5)) # memory view object (memory view of the given argument) (immutable)
print(j)

# complex
z = 1j
print(z)

# None
k = None

#convert from one type to another:

# convert from int to float:
a = float(x)

# convert from float to int:
b = int(y)

# convert from int to complex:
c = complex(x)

# conver from int to string:
num = 10
s = str(num)

print(type(s)) # <class 'str'> (type function returns the type of the variable or object)

# convert from string to int:
num = "50"
i = int(num) # valid

str = "hello"
# i = int(str) # invalid

# convert from int to bytes:
b = bytes(x)
print(b)
