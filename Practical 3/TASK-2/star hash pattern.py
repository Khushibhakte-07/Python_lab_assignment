# Program 2: Star Hash Pattern

for i in range(1, 6):
    for j in range(1, i+1):
        if j % 2 == 1:
            print("*", end="")
        else:
            print("#", end="")
    print()