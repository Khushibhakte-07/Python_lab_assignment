# Read from one file and write in uppercase to another file

# open source file
file1 = open("input.txt", "r")

# read content
data = file1.read()

# convert to uppercase
data_upper = data.upper()

# open new file to write
file2 = open("output.txt", "w")

# write uppercase content
file2.write(data_upper)

# close files
file1.close()
file2.close()

print("Content copied in uppercase successfully.")