def grocery_store(**kwargs):
    sorted_items = sorted(kwargs.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))
    return "\n".join([f"{key}: {value}" for key, value in sorted_items])
print(grocery_store(bread=5, pasta=12, eggs=12))
