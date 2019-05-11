# Sample lists
fruits = ['apple', 'oranges', 'grapes']
marks = [10, 20, 30]
nested_list = [[1,2], [2,3]]
hetero_list = [1, 'Test', 20.00, ['Nested_list', 20], {1: 'this is a dict inside list'}]

# Accesing list elements:
print(fruits[0]) # prints 'apple'
print(nested_list[1]) # prints [2,3]

# Printing a whole list
for fruit in fruits:
    print(fruit) # Prints each item in the list fruits one by one

# List comprehension

a_list = [a for a in range(1, 10)]
print(a_list) # prints [1, 2, 3, 4, 5, 6, 7, 8, 9]

# List Methods:

# list.append(x)
# Add an item to the end of the list. Equivalent to a[len(a):] = [x]


# list.extend(iterable)
# Extend the list by appending all the items from the iterable. Equivalent to a[len(a):] = iterable.


# list.insert(i, x)
# Insert an item at a given position.

# list.remove(x)
# Remove the first item from the list whose value is equal to x. It raises a ValueError if there is no such item.

# list.pop([i])
'''
Remove the item at the given position in the list, and return it. 
If no index is specified, a.pop() removes and returns the last item in the list
'''


# list.clear()
# Remove all items from the list. Equivalent to del a[:].


# list.index(x[, start[, end]])
# Return zero-based index in the list of the first item whose value is equal to x.

# list.count(x)
# Return the number of times x appears in the list.

# list.sort(key=None, reverse=False)
# Sort the items of the list in place.

# list.reverse()
# Reverse the elements of the list in place.

# list.copy()
# Return a shallow copy of the list. Equivalent to a[:].



