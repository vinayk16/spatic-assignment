import pandas as pd
import numpy as np
from geopy.distance import great_circle
from Levenshtein import distance as lev_distance

# Load the dataset into a pandas dataframe
df = pd.read_csv('C:\\Users\\vinay\\Desktop\\spatic\\assignment_data.csv')

# Create a column to store whether each entry is similar to another
df['is_similar'] = 0

# Create a dictionary to store entries grouped by rounded latitude and longitude
grid = {}
for i in range(len(df)):
    lat_rounded = round(df.iloc[i]['latitude'], 1)
    lon_rounded = round(df.iloc[i]['longitude'], 1)
    key = (lat_rounded, lon_rounded)
    if key in grid:
        grid[key].append(i)
    else:
        grid[key] = [i]

# Loop through all groups of entries within each grid cell
for cell in grid.values():
    for i in range(len(cell)):
        for j in range(i+1, len(cell)):

            # Calculate the distance between the two entries using their latitude and longitude
            dist = great_circle((df.iloc[cell[i]]['latitude'], df.iloc[cell[i]]['longitude']), (df.iloc[cell[j]]['latitude'], df.iloc[cell[j]]['longitude'])).m
            # Calculate the Levenshtein distance between the two names
            name_dist = lev_distance(df.iloc[cell[i]]['name'], df.iloc[cell[j]]['name'])
           # print(i)
            # If the distance between the entries is less than 200 meters and the name distance is less than 5, mark both entries as similar
            if dist < 200 and name_dist < 5:
                df.at[cell[i], 'is_similar'] = 1
                df.at[cell[j], 'is_similar'] = 1

# Save the dataframe to a new csv file with the added 'is_similar' column
df.to_csv('C:\\Users\\vinay\\Desktop\\spatic\\output.csv', index=False)


''' To optimize it I have used Dictionary to group entries by their rounded latitude and longitude values 
and then only compaes entries within each grid cell. This reduces the number of pairwise comaprisons with each other.
By rounding the latitude and longitude upto one decimal place results into entries which are nearer to each other are grouped into each cell.
This reduces the calculaion from entries with each other to entries which are grouped in one cell.
By this approach time taken for computation is reduced. 
Great_circle is used over geodesic and distance of the geopy module for accurate distance.
'''
