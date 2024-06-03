from collections import deque

stack = deque()

stack.append('a')
stack.append('b')
stack.append('c')

print('initial stack')

print(stack)


print('\Elements popped from stack:')
print(stack.pop())
print(stack.pop())
print(stack.pop())

print("\stack after elements ar popped")
print(stack)