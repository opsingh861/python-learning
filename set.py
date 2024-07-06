s = (
    set()
)  # empty set, set is a collection of unique elements (set is mutable), set is unordered (no indexing), set is unhashable (cannot contain mutable elements)
s.add(1)
s.add(2)
s.add(3)
s.add(4)
s.add(5)
s.add(5)
s.add(5)
s.add(5)
s.add(5)
s.add(5)

# s = {1,2,3,4} # this is also a set

print(s)  # prints {1, 2, 3, 4, 5}

# set methods

# add() method
s.add(6)  # adds 6 to the set
print(s)

# remove() method
s.remove(6)  # removes 6 from the set
print(s)

# discard() method
s.discard(5)  # removes 5 from the set

# pop() method
s.pop()  # removes a random element from the set
print(s)

# clear() method
s.clear()  # removes all elements from the set
print(s)

# union method
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.union(s2)  # returns a new set with elements from both s1 and s2 (no duplicates)
print(s3)  # prints {1, 2, 3, 4, 5}

# intersection method
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.intersection(s2)  # returns a new set with elements common to both s1 and s2
print(s3)  # prints {3}

# difference method
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.difference(s2)  # returns a new set with elements in s1 but not in s2 (s1 - s2)
print(s3)  # prints {1, 2}

# symmetric_difference method
s1 = {1, 2, 3}
s2 = {3, 4, 5}
s3 = s1.symmetric_difference(s2)  # returns a new set with elements in either s1 or s2 but not in both
print(s3)  # prints {1, 2, 4, 5}
