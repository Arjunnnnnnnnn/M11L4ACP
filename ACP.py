
import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv('Penguins Data.csv')

culmen_length = df['Culmen Length (mm)'].dropna()
culmen_depth = df['Culmen Depth (mm)'].dropna()
flipper_length = df['Flipper Length (mm)'].dropna()
body_mass = df['Body Mass (g)'].dropna()

plt.figure(figsize=(12, 9))

plt.subplot(2, 2, 1)
plt.hist(culmen_length, bins=15, color='b', edgecolor='black')
plt.xlabel('Culmen Length (mm)')
plt.ylabel('Frequency')
plt.title('Culmen Length')
plt.grid(True)

plt.subplot(2, 2, 2)
plt.hist(culmen_depth, bins=10, color='r', edgecolor='black')
plt.xlabel('Culmen Depth (mm)')
plt.ylabel('Frequency')
plt.title('Culmen Depth')
plt.grid(True)

plt.subplot(2, 2, 3)
plt.hist(flipper_length, bins=14, color='g', edgecolor='black')
plt.xlabel('Flipper Length (mm)')
plt.ylabel('Frequency')
plt.title('Flipper Length')
plt.grid(True)

plt.subplot(2, 2, 4)
plt.hist(body_mass, bins=20, color='orange', edgecolor='black')
plt.xlabel('Body Mass (g)')
plt.ylabel('Frequency')
plt.title('Body Mass')
plt.grid(True)

plt.tight_layout()
plt.show()
