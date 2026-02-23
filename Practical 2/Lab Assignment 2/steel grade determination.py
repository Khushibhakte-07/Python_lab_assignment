# Steel Grade Determination Program

hardness = float(input("Enter Hardness: "))
carbon = float(input("Enter Carbon Content: "))
tensile = float(input("Enter Tensile Strength: "))

condition1 = hardness > 50
condition2 = carbon < 0.7
condition3 = tensile > 5600

if condition1 and condition2 and condition3:
    grade = 10
elif condition1 and condition2:
    grade = 9
elif condition2 and condition3:
    grade = 8
elif condition1 and condition3:
    grade = 7
elif condition1 or condition2 or condition3:
    grade = 6
else:
    grade = 5

print("Steel Grade:", grade)