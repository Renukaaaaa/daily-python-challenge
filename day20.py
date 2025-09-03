def sort_stack(stack):
    if len(stack) <= 1:
        return
    top = stack.pop()
    sort_stack(stack)
    insert(stack, top)

def insert(stack, element):
    if not stack or element >= stack[-1]:
        stack.append(element)
        return
    top = stack.pop()
    insert(stack, element)
    stack.append(top)

stack = [3, 1, 4, 2]
sort_stack(stack)
print("Sorted stack:", stack)
