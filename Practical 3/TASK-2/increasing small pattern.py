# Program: python Increasing Pattern (Small)

word = "python"

for i in range(1, len(word)+1):
    for j in range(i):
        print(word[j], end="")
    print()