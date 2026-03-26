import pandas as pd
import matplotlib.pyplot as plt

# Read dataset
df = pd.read_csv("recruitment_data.csv")

companies = df['Company']
recruits = df['Recruitments']

# -------------------------------
# (a) Bar Chart
# -------------------------------
plt.figure(figsize=(10,5))
plt.bar(companies, recruits)
plt.title("New Recruitments in Companies")
plt.xlabel("Company Name")
plt.ylabel("Number of Recruitments")
plt.xticks(rotation=30)
plt.grid(axis='y')
plt.show()

# -------------------------------
# (b) Pie Chart
# -------------------------------
plt.figure(figsize=(8,8))
plt.pie(recruits, labels=companies, autopct="%1.1f%%", startangle=90)
plt.title("Recruitments Distribution (Pie Chart)")
plt.show()

# -------------------------------
# (c) Customize Pie Chart
# -------------------------------
plt.figure(figsize=(8,8))
plt.pie(recruits, labels=companies, autopct="%1.1f%%", startangle=90,
        shadow=True, explode=[0.05]*len(companies))
plt.title("Customized Pie Chart of Recruitments")
plt.show()

# -------------------------------
# (d) Doughnut Chart
# -------------------------------
plt.figure(figsize=(8,8))
plt.pie(recruits, labels=companies, autopct="%1.1f%%", startangle=90)
centre_circle = plt.Circle((0,0), 0.70, fc='white')
plt.gca().add_artist(centre_circle)
plt.title("Doughnut Chart of Recruitments")
plt.show()

# -------------------------------
# Compare IBM & Amdocs
# -------------------------------
ibm = df[df['Company'] == "IBM"]['Recruitments'].values[0]
amdocs = df[df['Company'] == "Amdocs"]['Recruitments'].values[0]

plt.figure(figsize=(6,4))
plt.bar(["IBM", "Amdocs"], [ibm, amdocs])
plt.title("Comparison: IBM vs Amdocs Recruitments")
plt.ylabel("Recruitments")
plt.grid(axis='y')
plt.show()