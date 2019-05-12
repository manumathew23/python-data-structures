''' Python's efficient key/value hash table structure is called a "dict". 
The contents of a dict can be written as a series of key:value pairs within braces { }.
E.g. dict = {key1:value1, key2:value2, ... }
'''

# Python program to illustrate dictionary 

# Create a new dictionary 
d = dict() # or d = {}


# NOTE: Dict keys must be of an immutable data type such as strings, numbers, or tuples

# Dict inside dict
dict_in_dict = {dict1: {}, dict2: {}}

# Add a key - value pairs to dictionary 
d['xyz'] = 123
d['abc'] = 345

# print the whole dictionary 
print(d) # {'xyz': 123, 'abc': 345}

# print only the keys 
print(d.keys()) # ['xyz', 'abc']

# print only values 
print(d.values()) # [123, 345]

# iterate over dictionary 
for i in d : 
	print("%s %d" %(i, d[i]))

# xyz 123
# abc 345


# another method of iteration 
for index, value in enumerate(d): 
	print(index, value , d[value]) 
# 0 xyz 123
# 1 abc 345

# check if key exist 
print('xyz' in d) # True

# delete the key-value pair 
del d['xyz'] 

# check again 
print("xyz" in d) # False
