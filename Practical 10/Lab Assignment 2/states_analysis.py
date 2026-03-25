
import pandas as pd

# Create table (data)
data = {
    'State': ['Maharashtra', 'Gujarat', 'Rajasthan', 'Uttar Pradesh', 'Madhya Pradesh'],
    'Area': [307713, 196244, 342239, 243286, 308252],   # in sq km
    'Population': [124000000, 68000000, 81000000, 230000000, 85000000]
}

# Create DataFrame
df = pd.DataFrame(data)

# a) Complete information
print("----- COMPLETE STATE DATA -----")
print(df)

# b) State with largest Area
print("\nState with Largest Area:")
print(df[df['Area'] == df['Area'].max()]['State'])

# c) State with largest Population
print("\nState with Largest Population:")
print(df[df['Population'] == df['Population'].max()]['State'])

# d) Population Density = Population / Area
df['Density'] = df['Population'] / df['Area']
print("\n----- DATA WITH DENSITY -----")
print(df)

# e) State with highest Density
print("\nState with Highest Population Density:")
print(df[df['Density'] == df['Density'].max()]['State'])