# Lab Assignment 1

# Taking input from user
numbers = tuple(map(int, input("Enter integers separated by space: ").split()))

# a) Total number of items
print("Total number of items:", len(numbers))

# b) Last item in the tuple
print("Last item:", numbers[-1])

# c) Elements in reverse order
print("Tuple in reverse order:", numbers[::-1])

# d) Check if integer 5 is present
if 5 in numbers:
    print("Yes, 5 is present in the tuple.")
else:
    print("No, 5 is not present in the tuple.")

# e) Remove first and last items, sort remaining, and print result
if len(numbers) > 2:
    new_tuple = tuple(sorted(numbers[1:-1]))
    print("Sorted tuple after removing first and last items:", new_tuple)
else:
    print("Not enough elements to remove first and last items.")