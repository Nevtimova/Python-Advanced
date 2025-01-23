n = int(input())
unique_elements = set()

for _ in range(n):
    elements = input().split()
    unique_elements.update(elements)

print("\n".join(unique_elements))
