import pandas as pd
import numpy as np

df = pd.read_csv('confidence_in_lognormal/ln_confidence_outputs/qqplot_r2_values.csv')

#creating list of unique aquifers in the dataset
aquifers = df.iloc[:, 0].unique().tolist()

aquifer_r2_values = pd.DataFrame()

for aquifer in aquifers:
    #filter by aquifer 
    aquifer_df = df[df.iloc[:, 0] == aquifer]
    #unique years
    years = aquifer_df.iloc[:, 1].unique().tolist()

    #get log and non-log r^2 values for the aquifer
    log_r2_values = df[df.iloc[:, 0] == aquifer].iloc[:, 2]
    non_log_r2_values = df[df.iloc[:, 0] == aquifer].iloc[:, 3]

    #get mean of log and non-log r^2 values for each year
    mean_log_r2 = log_r2_values.mean()
    mean_non_log_r2 = non_log_r2_values.mean()

    aquifer_r2_values[aquifer] = [mean_log_r2, mean_non_log_r2]

    #output in terminal for better understqanding
    print(f"Mean log r^2 for {aquifer}: {mean_log_r2}")
    print(f"Mean non-log r^2 for {aquifer}: {mean_non_log_r2}")

#save to csv
#columns are aquifers, rows are mean log and non-log r^2 values
aquifer_r2_values.to_csv('confidence_in_lognormal/ln_confidence_outputs/mean_r2_values.csv', index = False)
