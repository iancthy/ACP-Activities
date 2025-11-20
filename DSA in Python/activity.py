stack = []

stack.append(10)
stack.append(20)
stack.append(30)
print("Stack after pushes:", stack)

top = stack.pop()
print("Popped element:", top)
print("Stack after pop:", stack)

if stack:
    print("Top element:", stack[-1])
