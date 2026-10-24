import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#load df
df = pd.read_csv('data/filtered_well_data.csv')

#creating list of unique aquifers in the dataset
aquifers = df['Aquifer'].unique().tolist()

for aquifer in aquifers:
    #filter by aquifer 
    