# A set is an unordered collection with no duplicate elements

fruits = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(fruits)                      # {'orange', 'banana', 'pear', 'apple'}

print('orange' in basket)                 # True
print('crabgrass' in basket)              # False

# set operations on unique letters from two words

a = set('abracadabra')
b = set('alacazam')
print(a)                                  # {'a', 'r', 'b', 'c', 'd'}
print(a - b)                              # {'r', 'd', 'b'}
print(a | b)                              # {'a', 'c', 'r', 'd', 'b', 'm', 'z', 'l'}
print(a & b)                              # {'a', 'c'}
print(a ^ b)                              # {'r', 'd', 'b', 'm', 'z', 'l'}

set1 = set() 
set2 = set() 
   
# Adding elements to set1 
for i in range(1, 6): 
    set1.add(i) 
   
# Adding elements to set2 
for i in range(3, 8): 
    set2.add(i) 
   
print("Set1 = ", set1)                    # ('Set1 = ', set([1, 2, 3, 4, 5]))
print("Set2 = ", set2)                    # ('Set2 = ', set([3, 4, 5, 6, 7]))
