n = int(input())

matrix = [list(map(int, input().split())) for _ in range(n)]

while True:
    command = input()
    if command == "END":
        break

    action, row, col, value = command.split()
    row, col, value = int(row), int(col), int(value)

    if 0 <= row < n and 0 <= col < n:
        if action == "Add":
            matrix[row][col] += value
        elif action == "Subtract":
            matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(" ".join(map(str, row)))
