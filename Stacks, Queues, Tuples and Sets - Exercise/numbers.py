seq1 = set(map(int, input().split()))
seq2 = set(map(int, input().split()))
n = int(input())

for _ in range(n):
    command = input()
    if command.startswith("Add First"):
        _, _, *numbers = command.split()
        seq1.update(map(int, numbers))
    elif command.startswith("Add Second"):
        _, _, *numbers = command.split()
        seq2.update(map(int, numbers))
    elif command.startswith("Remove First"):
        _, _, *numbers = command.split()
        seq1.difference_update(map(int, numbers))
    elif command.startswith("Remove Second"):
        _, _, *numbers = command.split()
        seq2.difference_update(map(int, numbers))
    elif command == "Check Subset":
        print(seq1.issubset(seq2) or seq2.issubset(seq1))

print(", ".join(map(str, sorted(seq1))))
print(", ".join(map(str, sorted(seq2))))
