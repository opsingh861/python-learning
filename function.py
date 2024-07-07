# without return statement and arguments

# def hello():
#     print("Hello World")


# hello()  # prints Hello World


# # with return statement and arguments
# def add(a, b):
#     return a + b


# print(add(1, 2))  # prints 3


# with default arguments
# def add(a, b=2):
#     print("From add function 1")
#     return a + b


# def add(a):
#     print("From add function 2")
#     return a + 2


# print(add(1))  # function 1 will only run if function is not present


def sum(a, b) -> int:  # type hinting
    return "hello"


ans = sum(1, 2)
print(ans)  # prints 3
