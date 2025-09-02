def evaluate_postfix(expression):
    stack = []
    for token in expression.split():
        if token in '+-*/':
            b = stack.pop()
            a = stack.pop()
            if token == '+':
                stack.append(a + b)
            elif token == '-':
                stack.append(a - b)
            elif token == '*':
                stack.append(a * b)
            elif token == '/':
                stack.append(int(a / b))  
        else:
            stack.append(int(token))
    return stack[0]


expr = "2 1 + 3 *"
result = evaluate_postfix(expr)
print(result) 
