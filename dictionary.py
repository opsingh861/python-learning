dic = (
    {}
)  # this is empty dicitonary (dictionary is a collection of key-value pairs where keys are unique, immutable and values can be anything)

# adding elements to dictionary
dic["key1"] = "value1"

# accessing elements in dictionary
print(dic["key1"])  # prints value1 (if the key is not present, it will throw an error)

# updating elements in dictionary
dic["key1"] = "new value1"
print(dic["key1"])  # prints new value1

# deleting elements in dictionary
del dic["key1"]
print(dic)  # prints {}

# dictionary methods
dic = {"key1": "value1", "key2": "value2", "key3": "value3"}

# get() method
print(dic.get("key1"))  # prints value1 (if the key is not present, it will return None)

# items() method
print(
    dic.items()
)  # prints dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3')]), returns a list of tuples

# keys() method
print(dic.keys())  # prints dict_keys(['key1', 'key2', 'key3']), returns a list of keys

# values() method
print(
    dic.values()
)  # prints dict_values(['value1', 'value2', 'value3']), returns a list of values

# pop() method
print(
    dic.pop("key1")
)  # removes the key-value pair with key "key1" and returns the value

# popitem() method
print(dic.popitem())  # removes the last key-value pair and returns it as a tuple

# clear() method
dic.clear()  # removes all key-value pairs from the dictionary
print(dic)  # prints {}


