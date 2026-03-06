# Copy python file without comments

source = input("Enter source file name: ")
destination = input("Enter destination file name: ")

# open files
file1 = open(source, "r")
file2 = open(destination, "w")

for line in file1:
    if not line.strip().startswith("#"):
        file2.write(line)

file1.close()
file2.close()

# print contents
print("\nSource File Content:")
file1 = open(source, "r")
print(file1.read())

print("\nDestination File Content (without comments):")
file2 = open(destination, "r")
print(file2.read())

file1.close()
file2.close()