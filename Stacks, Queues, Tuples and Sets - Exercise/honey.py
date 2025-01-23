from collections import deque

bees = deque(map(int, input().split()))
nectar = list(map(int, input().split()))
symbols = deque(input().split())
total_honey = 0

while bees and nectar:
    bee = bees[0]
    nectar_value = nectar.pop()

    if nectar_value >= bee:
        symbol = symbols.popleft()
        bees.popleft()
        if symbol == "+":
            total_honey += abs(bee + nectar_value)
        elif symbol == "-":
            total_honey += abs(bee - nectar_value)
        elif symbol == "*":
            total_honey += abs(bee * nectar_value)
        elif symbol == "/" and nectar_value != 0:
            total_honey += abs(bee / nectar_value)

print(f"Total honey made: {total_honey}")
if bees:
    print(f"Bees left: {', '.join(map(str, bees))}")
if nectar:
    print(f"Nectar left: {', '.join(map(str, nectar))}")
