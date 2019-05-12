# Tuples
# A tuple is a sequence of immutable Python objects

emptyTuple = ()

# 2 ways of creating a tuple
sample_tuple = (3, 7, 4, 2)
another_tuple = z = 3, 7, 4, 2

# NOTE: if you want to create a tuple containing only one value, you need a trailing comma after your item.
# tuple with one value
tup1 = (1,)

# not_a_tuple = (1)

# accesing values in a tuple
print(sample_tuple[0]) # 3


# slice a tuple
print(sample_tuple[0:2]) # (3, 7)

# Tupes are immutable
# sample_tuple[0] = 10 is not allowed

# index method
fruits = ('apple', 'guava', 'apple')
print(fruits.index('apple')) # 0

# count method
print(fruits.count('apple')) # 2

# Iterate through a tuple
for item in fruits:
    print(item)

# output
# apple
# guava
# apple

# unpacking a tuple
x, y = (7, 10);
print("Value of x is {}, the value of y is {}.".format(x, y))
# value of x is 7, value of y is 10

for index, item in enumerate(fruits):
  print(index, item)

# output
# apple, 0
# guava, 1
# apple, 2

#Advantages over list
# 1. Tuples are faster than lists.
'''
2. Some tuples can be used as dictionary keys (specifically, 
tuples that contain immutable values like strings, numbers, and other tuples)
'''
# 3. Tuples can be used as values in sets whereas lists can not

