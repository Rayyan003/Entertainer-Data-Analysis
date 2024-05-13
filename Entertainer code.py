import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Sample entertainer data (replace with your dataset)
data = {
    'Name': ['Jennifer Lopez', 'Brad Pitt', 'Beyoncé', 'Chris Hemsworth', 'Taylor Swift'],
    'Age': [52, 58, 40, 38, 33],
    'Genre': ['Music', 'Film', 'Music', 'Film', 'Music'],
    'Popularity': [90, 85, 95, 80, 92]
}

# Create DataFrame
df = pd.DataFrame(data)

# Basic data analysis
print("Average Age of Entertainers:", df['Age'].mean())

# Popularity distribution
plt.hist(df['Popularity'], bins=5, color='skyblue', edgecolor='black')
plt.title('Popularity Distribution of Entertainers')
plt.xlabel('Popularity')
plt.ylabel('Frequency')
plt.show()