import pandas as pd
import numpy as np
from geopy.distance import great_circle
from Levenshtein import distance as lev_distance
import time

start = time.time()

# Load the dataset into a pandas dataframe
df = pd.read_csv('C:\\Users\\vinay\\Desktop\\spatic\\assignment_data.csv')

# Create a new column to store whether each entry is similar to another
df['is_similar'] = 0
for i in range(len(df)):
 for j in range(i+1,len(df)):

  # Calculate the distance between the two entries with latitude and longitude using great_circle funcion of geopy module
  dist = great_circle((df.iloc[i]['latitude'], df.iloc[i]['longitude']), (df.iloc[j]['latitude'], df.iloc[j]['longitude'])).m

  # Calculate the Levenshtein distance between the two names
  name_d = lev_distance(df.iloc[i]['name'], df.iloc[j]['name'])

  # If the distance between the entries is less than 200 meters and the name distance is less than 5, then both the entries are marked similar  
  if dist < 200 and name_d < 5:
    df.at[i, 'is_similar'] = 1
    df.at[j, 'is_similar'] = 1

# Save the dataframe to a new csv file
df.to_csv('C:\\Users\\vinay\\Desktop\\spatic\\output.csv', index=False)


'''
The program loads the dataset into a pandas dataframe and then loops through all pairs of entries
 to calculate their distance and name distance. For calculating distance I have use great_circle which is more 
 accurate than geodesic and distance function of the geopy module  If the distance is less than 200 meters and the name 
 distance is less than 5, then both the entries are marked similar. The resulting dataframe is then saved 
 to a new csv file with the added 'is_similar' column.
 Approach or logic behind this program is bruteforce or naive approach. Therefore the Time complexity is O(N*N) where N is the entries.
 So I have optimize it to carry out computation in less time. Optimized Code is in the second python file.
'''




