# Assignment

Panda Library is used to load dataset in dataframes <br>
Geopy module to calculate the distance <br>
Levenshtein module is used to find the similarity of the words


##Approach 1 : Bruteforce or Naive approach
The program loads the dataset into a pandas dataframe and then loops through all pairs of entries
to calculate their distance and name distance. For calculating distance I have use great_circle which is more 
accurate than geodesic and distance function of the geopy module  If the distance is less than 200 meters and the name 
distance is less than 5, then both the entries are marked similar. The resulting dataframe is then saved 
to a new csv file with the added 'is_similar' column.
Approach or logic behind this program is bruteforce or naive approach. Therefore the Time complexity is O(N*N) where N is the entries.
So I have optimize it to carry out computation in less time. Optimized Code is in the second python file.

##Approach 2 : Dictionary based
To optimize it I have used Dictionary to group entries by their rounded latitude and longitude values 
and then only compaes entries within each grid cell. This reduces the number of pairwise comaprisons with each other.
By rounding the latitude and longitude upto one decimal place results into entries which are nearer to each other are grouped into each cell.
This reduces the calculaion from entries with each other to entries which are grouped in one cell.
By this approach time taken for computation is reduced. 
Great_circle is used over geodesic and distance of the geopy module for accurate distance.
