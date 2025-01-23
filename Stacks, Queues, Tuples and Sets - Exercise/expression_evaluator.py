from collections import deque

expression = input().split()
numbers = deque()

for token in expression:
    if token.isdigit() or (token[0] == '-' and token[1:].isdigit()):
        numbers.append(int(token))
    else:
        while len(numbers) > 1:
            num1 = numbers.popleft()
            num2 = numbers.popleft()
            if token == "+":
                numbers.appendleft(num1 + num2)
            elif token == "-":
                numbers.appendleft(num1 - num2)
            elif token == "*":
                numbers.appendleft(num1 * num2)
            elif token == "/":
                numbers.appendleft(num1 // num2)

print(numbers[0])
