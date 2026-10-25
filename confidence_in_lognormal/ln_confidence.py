import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt

#load df
df = pd.read_csv('data/filtered_well_data.csv')

#creating list of unique aquifers in the dataset
aquifers = df['Aquifer'].unique().tolist()
results = []

for aquifer in aquifers:
    #filter by aquifer 
    aquifer_df = df[df['Aquifer'] == aquifer]

    #get unique years for aquifer
    years = aquifer_df['DrillingYear'].unique().tolist()

    #loop through each year and calc r^2 of each year for the aquifer
    for year in years:
        year_df = aquifer_df[aquifer_df['DrillingYear'] == year]

        #calc. r^2 for log qqplot and non-log qqplot
        depth = pd.to_numeric(year_df['WellDepth'], errors = 'coerce').to_numpy()
        depth = depth[np.isfinite(depth) & (depth > 0)]

        #a Q-Q line cannot be fit with fewer than two values or no variation.
        #this will fix the error
        if len(depth) < 2 or np.ptp(depth) == 0:
            continue

        log_depth = np.log(depth)

        #get sm plot and the ProbPlot objects containing its data
        #line = 's' stands for standardized line, which is this:
        #“s” - standardized line, the expected order 
        # statistics are scaled by the standard deviation 
        # of the given sample and have the mean added to them
        res_log = sm.ProbPlot(log_depth, fit = True)
        res_non_log = sm.ProbPlot(depth, fit = True)
        res_log.qqplot(line = 's')
        res_non_log.qqplot(line = 's')

        #loc is location param. for qqplot, which is the mean of the data and
        #in this cas represents the intercept of the line of the best fit plot
        intercept_log = res_log.loc
        intercept_non_log = res_non_log.loc

        #scale is scale param. for qqplot, which is the std. dev. of the data and
        #in this case represents the slope of the line of the best fit plot
        #NOTE: not exactly sure why, but this is what statsmodels does for the qqplot
        slope_log = res_log.scale
        slope_non_log = res_non_log.scale

        #get x and y values for the qqplot
        #x_log and y_log are the theoretical and sample quantiles for the log qqplot
        #which means they are the expected and actual values for the log qqplot
        x_log = res_log.theoretical_quantiles
        x_non_log = res_non_log.theoretical_quantiles
        y_log = res_log.sample_quantiles
        y_non_log = res_non_log.sample_quantiles

        #calculate the line of best fit for the log qqplot
        fit_slope_log, fit_intercept_log = np.polyfit(x_log, y_log, 1)
        y_fit_log = fit_slope_log * x_log + fit_intercept_log
        fit_slope_non_log, fit_intercept_non_log = np.polyfit(x_non_log, y_non_log, 1)
        y_fit_non_log = fit_slope_non_log * x_non_log + fit_intercept_non_log

        #calculate r^2 for the log qqplot
        #this is all taken from the original code I made for a simple one year dist.
        r_2_log = 1 - np.sum((y_log - y_fit_log) ** 2) / np.sum((y_log - np.mean(y_log)) ** 2)
        r_2_non_log = 1 - np.sum((y_non_log - y_fit_non_log) ** 2) / np.sum((y_non_log - np.mean(y_non_log)) ** 2)

        plt.close('all')

        results.append({
            'Aquifer': aquifer,
            'Year': year,
            'R2_log': r_2_log,
            'R2_non_log': r_2_non_log,
        })

# Overwrite the output so rerunning the script cannot create duplicate rows.
results_df = pd.DataFrame(results)
results_df.to_csv(
    'confidence_in_lognormal/ln_confidence_outputs/qqplot_r2_values.csv',
    index=False,
)


