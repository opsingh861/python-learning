str = "This is a string"  # string is immutable
str = "This is a string"
str = """This is a
string"""  # triple quotes can be used for multiline strings
print(str)

# string functions and methods in python
# len() function
str = "This is a string"
print(len(str))

# string methods
# capitalize() method
str = "this is a string"
print(str.capitalize())

# casefold() method
str = "This Is A String"  # converts string to lowercase
print(str.casefold())

# center() method
str = "This is a string"
print(str.center(30))  # center the string in a string of length 30

# upper() method
str = "This is a string"
print(str.upper())  # converts string to uppercase

# lower() method
str = "This is a string"
print(str.lower())  # converts string to lowercase

# slicing in strings
str = "This is a string"
print(
    str[0:4]
)  # prints "This", 0 is inclusive and 4 is exclusive (0, 1, 2, 3) = 4 characters

# negative indexing
str = "This is a string"
print(
    str[-6:-1]
)  # prints "strin", -1 is exclusive and -6 is inclusive (-6, -5, -4, -3, -2) = 5 characters

str = "123456789"
print(str[0:10:2])  # prints "Ti s", 0 is inclusive, 10 is exclusive, 2 is step

str = "123456789"
print(str[:10])  # prints "This is a string", same as str[0:10]

str = "123456789"
print(str[0:])  # prints "This is a string", same as str[0:10]

str = "123456789"
print(str[:])  # prints "This is a string", same as str[0:10]

str = "123456789"
print(str[::-1])  # prints the string in reverse order

# string concatenation
str1 = "This is a"
str2 = " string"
print(str1 + str2)  # prints "This is a string"

# Access variables in strings

name = "John"
age = 23
str = "My name is {} and I am {} years old".format(name, age)
print(str)

# f-string
name = "John"
age = 23
str = f"My name is {name} and I am {age} years old"
print(str)

# escape characters
str = "This is a \"string\""
print(str)

str = "This is a \nstring"
print(str)

str = "This is a \tstring"
print(str)

str = "This is a \\string"
print(str)



