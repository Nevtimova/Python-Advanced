n = int(input())

board = [list(input()) for _ in range(n)]

moves = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]


def count_attacks(board, row, col):
    count = 0
    for dr, dc in moves:
        r, c = row + dr, col + dc
        if 0 <= r < n and 0 <= c < n and board[r][c] == "K":
            count += 1
    return count


removed_knights = 0
while True:
    max_attacks = 0
    knight_position = None

    for row in range(n):
        for col in range(n):
            if board[row][col] == "K":
                attacks = count_attacks(board, row, col)
                if attacks > max_attacks:
                    max_attacks = attacks
                    knight_position = (row, col)

    if max_attacks == 0:
        break

    row, col = knight_position
    board[row][col] = "0"
    removed_knights += 1

print(removed_knights)
