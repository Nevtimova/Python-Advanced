def age_assignment(*names, **ages):
    return "\n".join([f"{name} is {ages[name[0]]} years old." for name in sorted(names)])
print(age_assignment("Peter", "George", G=26, P=19))
