def fill_the_box(height, length, width, *args):
    box_capacity = height * length * width
    cubes = 0
    for item in args:
        if item == "Finish":
            break
        cubes += item

    if cubes <= box_capacity:
        return f"There is free space in the box. You could put {box_capacity - cubes} more cubes."
    else:
        return f"No more free space! You have {cubes - box_capacity} more cubes."
print(fill_the_box(2, 8, 2, 2, 1, 7, 3, 1, 5, "Finish"))

print(fill_the_box(5, 5, 2, 40, 11, 7, 3, 1, 5, "Finish"))
