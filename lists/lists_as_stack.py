# Stacks - Last in first out
# Methods used - append and pop

number_stack = [1,2,3,4,5,6,7,8,9]

def add_to_stack(stack, value):
  stack.appned(value)
  return stack

def remove_from_stack(stack):
  if stack:
    stack.pop()
  return stack

number_stack = add_to_stack(number_stack, 10)
print(number_stack) # [1,2,3,4,5,6,7,8,9, 10]

number_stack = remove_from_stack(number_stack)
print(number_stack )# [1,2,3,4,5,6,7,8,9]
