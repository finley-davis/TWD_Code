#info from here for qqplot: https://www.statsmodels.org/devel/generated/statsmodels.graphics.gofplots.qqplot.html

import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#load df
df = pd.read_csv('data/filtered_well_data.csv')

# we are only analyzing 1-yr intervals, 
# so we will fit lognormal distributions to one year bins for 
# each aquifer

#creating list of unique aquifers in the dataset
aquifers = df['Aquifer'].unique().tolist()


#try for 1 year
df = df[(df['Aquifer'] == 'Ogallala') & (df['DrillingYear'] == 1972)]

"""
#using qqplot to check for lognormality
#sm.qqplot(df['WellDepth'], line = 'q')

#this will prove if the data is lognormal or not
#if the data follows a lognormal distribution, 
#the points will fall almost exactly along the line in the qqplot
#sm.qqplot(np.log(df['WellDepth']), line = 's') 

#get x and y values for the qqplot
#this is useful for calculating the R^2 value for the qqplot
res = sm.ProbPlot(np.log(df['WellDepth']), fit = True)
print(res.theoretical_quantiles)


#plt.title('Q-Q Plot (Statsmodels)')
#plt.show()
"""
----------------------------------------
#calc. r^2 for the log qqplot
log_depth = np.log(df['WellDepth'])
res_log = sm.ProbPlot(log_depth, fit = True)

#get x and y values for the qqplot
x_log = res_log.theoretical_quantiles
y_log = res_log.sample_quantiles

#intercept and slope of the line of best fit for the qqplot
intercept_ = res_log.loc
slope = res_log.scale

fit_slope_log, fit_intercept_ = np.polyfit(x_log, y_log, 1)
y_fit_log = fit_slope_log * x_log + fit_intercept_

r_2_log = 1 - np.sum((y_log - y_fit_log) ** 2) / np.sum((y_log - np.mean(y_log)) ** 2)

print(f'R^2 value for the qqplot: {r_2_log}\n')

#calc. r^2 for the non-log qqplot
res_non_log = sm.ProbPlot(df['WellDepth'], fit = True)

# Get x and y values for the non-log qqplot
x_non_log = res_non_log.theoretical_quantiles
y_non_log = res_non_log.sample_quantiles

# Calculate the line of best fit for the non-log qqplot
fit_slope_non_log, fit_intercept_ = np.polyfit(x_non_log, y_non_log, 1)
y_fit_non_log = fit_slope_non_log * x_non_log + fit_intercept_

# Calculate R^2 for the non-log qqplot
r_2_non_log = 1 - np.sum((y_non_log - y_fit_non_log) ** 2) / np.sum((y_non_log - np.mean(y_non_log)) ** 2)

print(f'R^2 value for the non-log qqplot: {r_2_non_log}\n')

