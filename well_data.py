import pandas as pd

df = pd.read_csv('/Users/finleydavis/Desktop/Cardenas Research/new_analysis/county_analysis/WellMain.txt', sep = '|', encoding = "cp1252")
#df_sdr = pd.read_csv('/Users/finleydavis/Desktop/Cardenas Research/zx/SDRDownload/SDRDownload/WellData.txt', sep = '|', encoding = "cp1252", on_bad_lines = 'warn')

df = df[['StateWellNumber', 'WellDepth', 'County', 'DrillingYear', 'Aquifer', 'LongitudeDD', 'LatitudeDD']]

df = df[df['Aquifer'].isin(['Ogallala', 'Edwards (Balcones Fault Zone)', 'Edwards-Trinity Plateau', 'Carrizo-Wilcox', 'Gulf Coast', 'Pecos Valley', 'Seymour', 'Trinity', 'Hueco-Mesilla Bolsons'])]
print(df)

print(df.isnull().sum())
#drop null from aquifer code, longitude, and latitude
df = df.dropna(subset = ['Aquifer', 'DrillingYear', 'County', 'LongitudeDD', 'LatitudeDD'])

df = df[df['DrillingYear'] >= 1920]

print(df.shape)