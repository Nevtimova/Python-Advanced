n = int(input())

matrix = []
alice_row, alice_col = 0, 0

for row in range(n):
    line = input().split()
    matrix.append(line)
    if "A" in line:
        alice_row, alice_col = row, line.index("A")

commands = []
while True:
    try:
        commands.append(input())
    except EOFError:
        break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

tea_collected = 0
matrix[alice_row][alice_col] = "*"

for command in commands:
    dr, dc = directions[command]
    alice_row += dr
    alice_col += dc

    if not (0 <= alice_row < n and 0 <= alice_col < n):  # Alice went out of bounds
        print("Alice didn't make it to the tea party.")
        break

    cell = matrix[alice_row][alice_col]
    if cell == "R":  # Alice fell into the rabbit hole
        matrix[alice_row][alice_col] = "*"
        print("Alice didn't make it to the tea party.")
        break

    if cell.isdigit():  # Alice collects tea bags
        tea_collected += int(cell)

    matrix[alice_row][alice_col] = "*"

    if tea_collected >= 10:  # Alice collected enough tea
        print("She did it! She went to the party.")
        break

for row in matrix:
    print(" ".join(row))
