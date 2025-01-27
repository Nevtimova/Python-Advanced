presents = int(input())
n = int(input())

matrix = []
santa_row, santa_col = 0, 0
nice_kids = 0

for row in range(n):
    line = input().split()
    matrix.append(line)
    if "S" in line:
        santa_row, santa_col = row, line.index("S")
    nice_kids += line.count("V")

commands = []
while True:
    try:
        command = input()
        if command == "Christmas morning":
            break
        commands.append(command)
    except EOFError:
        break

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

gifts_delivered = 0

for command in commands:
    dr, dc = directions[command]
    matrix[santa_row][santa_col] = "-"
    santa_row += dr
    santa_col += dc

    cell = matrix[santa_row][santa_col]

    if cell == "V":  # Deliver a present to a nice kid
        presents -= 1
        gifts_delivered += 1
        matrix[santa_row][santa_col] = "-"
    elif cell == "C":  # Cookies: deliver to all surrounding cells
        for adj_dr, adj_dc in directions.values():
            adj_row, adj_col = santa_row + adj_dr, santa_col + adj_dc
            if 0 <= adj_row < n and 0 <= adj_col < n and presents > 0:
                if matrix[adj_row][adj_col] == "V":
                    gifts_delivered += 1
                if matrix[adj_row][adj_col] in ("V", "X"):
                    presents -= 1
                    matrix[adj_row][adj_col] = "-"

    matrix[santa_row][santa_col] = "S"

    if presents == 0:
        print("Santa ran out of presents!")
        break

for row in matrix:
    print(" ".join(row))

remaining_kids = nice_kids - gifts_delivered
if remaining_kids == 0:
    print(f"Good job, Santa! {gifts_delivered} happy nice kid/s.")
else:
    print(f"No presents for {remaining_kids} nice kid/s.")
