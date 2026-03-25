import pandas as pd

# Read CSV file
df = pd.read_csv("books.csv")

print("\nComplete Report:\n")
print(df)

# a) Books by author
author_name = input("\nEnter author name: ")
print("\nBooks by", author_name)
print(df[df['author'] == author_name])

# b) Books by publisher
publisher_name = input("\nEnter publisher name: ")
print("\nBooks by", publisher_name)
print(df[df['publisher'] == publisher_name])

# c) Cheapest and Costliest book
print("\nCheapest Book:")
print(df[df['price'] == df['price'].min()])

print("\nCostliest Book:")
print(df[df['price'] == df['price'].max()])

# d) Sort by year
print("\nBooks Sorted by Year:")
print(df.sort_values(by='year'))