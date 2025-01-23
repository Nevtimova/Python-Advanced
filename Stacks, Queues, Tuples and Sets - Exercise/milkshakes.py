from collections import deque

chocolates = list(map(int, input().split(", ")))
milk = deque(map(int, input().split(", ")))
milkshakes = 0

while chocolates and milk and milkshakes < 5:
    chocolate = chocolates.pop()
    milk_cup = milk.popleft()

    if chocolate <= 0 and milk_cup <= 0:
        continue
    if chocolate <= 0:
        milk.appendleft(milk_cup)
        continue
    if milk_cup <= 0:
        chocolates.append(chocolate)
        continue

    if chocolate == milk_cup:
        milkshakes += 1
    else:
        chocolates.append(chocolate - 5)
        milk.append(milk_cup)

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

print(f"Chocolate: {', '.join(map(str, chocolates)) if chocolates else 'empty'}")
print(f"Milk: {', '.join(map(str, milk)) if milk else 'empty'}")
