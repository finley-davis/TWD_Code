import pandas as pd



#add github file path later
#this one is a fildownlaoded at a different time (April 5th, 2025)
df = pd.read_csv('data/WellMain.txt', sep = '|', encoding = "cp1252", on_bad_lines = 'warn')

#only use useful columns
df = df[['StateWellNumber', 'WellDepth', 'County', 'DrillingYear', 'Aquifer', 'LongitudeDD', 'LatitudeDD']]
#show the inital shape(total number of data points) and columns of the dataframe
print(f'Initial dataframe shape: {df.shape}\n')

#only look at data from these aquifer (the nine major in Texas)
df = df[df['Aquifer'].isin(['Ogallala', 'Edwards (Balcones Fault Zone)', 'Edwards-Trinity Plateau', 'Carrizo-Wilcox', 'Gulf Coast', 'Pecos Valley', 'Seymour', 'Trinity', 'Hueco-Mesilla Bolson'])]
print(f'Dataframe shape after filtering by aquifer: {df.shape}\n')

#show the total amount of null values being removed for each column, then drop
print(f'Total null values: \n{df.isna().sum()}\n')
#drop null from aquifer code, longitude, and latitude
df = df.dropna(subset = ['Aquifer', 'WellDepth', 'DrillingYear', 'County', 'LongitudeDD', 'LatitudeDD'])
#show the shape of the dataframe after dropping null values
print(f'Dataframe shape after dropping null values: {df.shape}\n')

#filter by year
df = df[(df['DrillingYear'] >= 1920) & (df['DrillingYear'] <= 2023)]

#final shape of all used data points
print(f'Final dataframe shape: {df.shape}\n')

#output filtered data to csv for use in other scripts
df.to_csv('data/filtered_well_data.csv', index = False)