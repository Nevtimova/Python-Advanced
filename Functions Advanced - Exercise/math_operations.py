def math_operations(*args, a=0, s=0, d=0, m=0):
    operations = {"a": a, "s": s, "d": d, "m": m}
    op_cycle = ["a", "s", "d", "m"]

    for i, num in enumerate(args):
        op_key = op_cycle[i % 4]
        if op_key == "a":
            operations["a"] += num
        elif op_key == "s":
            operations["s"] -= num
        elif op_key == "d":
            if num != 0:
                operations["d"] /= num
        elif op_key == "m":
            operations["m"] *= num

    sorted_ops = sorted(operations.items(), key=lambda x: (-x[1], x[0]))
    return "\n".join(f"{key}: {value:.1f}" for key, value in sorted_ops)
print(math_operations(2.1, 12.56, 0.0, -3.899, 6.0, -20.65, a=1, s=7, d=33, m=15))
print(math_operations(-1.0, 0.5, 1.6, 0.5, 6.1, -2.8, 80.0, a=0, s=-2.3, d=0, m=0))
