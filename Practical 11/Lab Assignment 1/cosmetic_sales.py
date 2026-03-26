import pandas as pd
import matplotlib.pyplot as plt

# Read CSV File
df = pd.read_csv("company_sales_data.csv")

# -------------------------------
# (a) Total Profit Line Plot
# -------------------------------
plt.figure(figsize=(8,5))
plt.plot(df['month_number'], df['total_profit'], marker='o', linestyle='-', linewidth=2)
plt.title("Total Profit of All Months")
plt.xlabel("Month Number")
plt.ylabel("Total Profit")
plt.grid(True)
plt.show()

# -------------------------------
# (b) All Product Sales Multiline Plot
# -------------------------------
plt.figure(figsize=(10,6))

plt.plot(df['month_number'], df['facecream'], label="Face Cream", marker='o')
plt.plot(df['month_number'], df['facewash'], label="Face Wash", marker='o')
plt.plot(df['month_number'], df['toothpaste'], label="Toothpaste", marker='o')
plt.plot(df['month_number'], df['bathingsoap'], label="Bathing Soap", marker='o')
plt.plot(df['month_number'], df['shampoo'], label="Shampoo", marker='o')
plt.plot(df['month_number'], df['moisturizer'], label="Moisturizer", marker='o')

plt.title("Sales Data of All Products")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(True)
plt.show()

# -------------------------------
# (c) Face Cream & Face Wash Bar Chart
# -------------------------------
plt.figure(figsize=(8,5))

plt.bar(df['month_number'] - 0.2, df['facecream'], width=0.4, label="Face Cream")
plt.bar(df['month_number'] + 0.2, df['facewash'], width=0.4, label="Face Wash")

plt.title("Face Cream and Face Wash Sales Data")
plt.xlabel("Month Number")
plt.ylabel("Units Sold")
plt.legend()
plt.grid(axis='y')
plt.show()

# -------------------------------
# (d) Total Sales Pie Chart (Last Year)
# -------------------------------
total_sales = [
    df['facecream'].sum(),
    df['facewash'].sum(),
    df['toothpaste'].sum(),
    df['bathingsoap'].sum(),
    df['shampoo'].sum(),
    df['moisturizer'].sum()
]

products = ["Face Cream", "Face Wash", "Toothpaste", "Bathing Soap", "Shampoo", "Moisturizer"]

plt.figure(figsize=(8,8))
plt.pie(total_sales, labels=products, autopct="%1.1f%%", startangle=140)
plt.title("Total Sales Data of Last Year (Each Product)")
plt.show()