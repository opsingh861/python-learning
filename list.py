list = [1, "a", False, 3.14]  # list can contain different data types, list is mutable
print(list[0])  # prints [1, 'a', False, 3.14]

print(list[0:2])  # prints [1, 'a'], same slicing methods as strings

# list methods

# append() method
list.append("new")  # appends "new" to the end of the list
print(list)

# insert() method
list.insert(1, "new")  # inserts "new" at index 1

# remove() method
list.remove("new")  # removes the first occurrence of "new" from the list

# pop() method
list.pop(1)  # removes the element at index 1, if no index is provided, it removes the last element, returns the removed element (will change the original list)

# clear() method
list.clear()  # removes all elements from the list
print(list)

# copy() method
list = [1, "a", False, 3.14]
list2 = list.copy()  # returns a shallow copy of the list

# count() method
print(list.count(1))  # returns the number of occurrences of 1 in the list

# index() method
print(list.index(1))  # returns the index of the first occurrence of 1 in the list (will throw an error if the element is not in the list)

# reverse() method
list.reverse()  # reverses the list in place
print(list)

# sort() method
list = [3, 2, 1]
list.sort()  # sorts the list in ascending order
print(list)

