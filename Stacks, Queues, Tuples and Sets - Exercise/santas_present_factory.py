from collections import deque

materials = list(map(int, input().split()))
magic = deque(map(int, input().split()))

presents = {
    "Doll": 150,
    "Wooden train": 250,
    "Teddy bear": 300,
    "Bicycle": 400,
}
crafted_presents = {}

while materials and magic:
    material = materials.pop()
    magic_level = magic.popleft()

    if material == 0 and magic_level == 0:
        continue
    if material == 0:
        magic.appendleft(magic_level)
        continue
    if magic_level == 0:
        materials.append(material)
        continue

    result = material * magic_level

    if result in presents.values():
        present = [k for k, v in presents.items() if v == result][0]
        crafted_presents[present] = crafted_presents.get(present, 0) + 1
    elif result < 0:
        materials.append(material + magic_level)
    else:
        materials.append(material + 15)

success = (
    ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or
    ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)
)

print("The presents are crafted! Merry Christmas!" if success else "No presents this Christmas!")
if materials:
    print(f"Materials left: {', '.join(map(str, materials[::-1]))}")
if magic:
    print(f"Magic left: {', '.join(map(str, magic))}")
for present, count in sorted(crafted_presents.items()):
    print(f"{present}: {count}")
