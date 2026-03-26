import pandas as pd

# Creating Diamonds DataFrame (as given in question)
data = {
    "carat": [0.23, 0.21, 0.23, 0.29, 0.31],
    "cut": ["Ideal", "Premium", "Good", "Premium", "Good"],
    "color": ["E", "E", "E", "I", "J"],
    "clarity": ["SI2", "SI1", "VS1", "VS2", "SI2"],
    "depth": [61.5, 59.8, 56.9, 62.4, 63.3],
    "table": [55.0, 61.0, 65.0, 58.0, 58.0],
    "price": [326, 326, 327, 334, 335],
    "x": [3.95, 3.89, 4.05, 4.20, 4.34],
    "y": [3.98, 3.84, 4.07, 4.23, 4.35],
    "z": [2.43, 2.31, 2.31, 2.63, 2.75]
}

df = pd.DataFrame(data)

print("Diamonds DataFrame:\n")
print(df)

# -----------------------------------------
# (i) Mean of price for each cut
# -----------------------------------------
print("\n(i) Mean of Price for each Cut:\n")
mean_price = df.groupby("cut")["price"].mean()
print(mean_price)

# -----------------------------------------
# (ii) Count, Minimum and Maximum price for each cut
# -----------------------------------------
print("\n(ii) Count, Minimum and Maximum Price for each Cut:\n")
count_min_max = df.groupby("cut")["price"].agg(["count", "min", "max"])
print(count_min_max)

# -----------------------------------------
# (iii) Average value of x, y, z separately
# -----------------------------------------
print("\n(iii) Average of x, y, z separately:\n")
print("Average x =", df["x"].mean())
print("Average y =", df["y"].mean())
print("Average z =", df["z"].mean())