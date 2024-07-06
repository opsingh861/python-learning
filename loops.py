# for loop

# for i in range(10): # prints 0 to 9 (10 is exclusive)
#     print(i)

# # for loop with start and end
# for i in range(1, 10): # prints 1 to 9 (10 is exclusive and 1 is inclusive)
#     print(i)

# # for loop with step
# for i in range(2, 10, 2): # prints 1, 3, 5, 7, 9 (10 is exclusive and 1 is inclusive, 2 is the step)
#     print(i)

# for loop with negative step
# for i in range(10, 0, -1): # prints 10 to 1 (0 is exclusive and 10 is inclusive, -1 is the step)
#     print(i)


# str = "This is a string"

# for i in str:
#     print(i)

# # for loop in list
# list = [1, 2, 3, 4, 5]
# for i in list:
#     print(i)

# for i in range(len(list)):
#     print(list[i])


# # for loop with break
# for i in range(10):
#     if i == 5:
#         break
#     print(i)


# # for loop with continue
# for i in range(10):
#     if i == 5:
#         continue
#     print(i)


# for loop with pass
# for i in range(10):
#     pass  # does nothing (placeholder)
#     print(i)

# for loop with else
# for i in range(10):
#     print(i)
# else:  # executes when the loop is completed without a break
#     print("Loop completed")


# while loop

i = 0
while i < 10:
    print(i)
    i +=1  # increment i by 1
    
# optional else block
else:
    print("Loop completed")
