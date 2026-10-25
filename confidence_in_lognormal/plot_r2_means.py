import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('confidence_in_lognormal/ln_confidence_outputs/mean_r2_values.csv')

#get the mean log and non-log r^2 values for each aquifer, row 1 and row 2
lnr2_df = df.iloc[0, :]
non_lnr2_df = df.iloc[1, :]

#plot the mean log and non-log r^2 values for each aquifer
aquifers = df.columns.tolist()

"""
figure, ax = plt.subplots(1, 2, figsize=(10, 6))

ax[0].bar(aquifers, lnr2_df, color='blue', alpha=0.7)
ax[0].set_title('Mean Log R^2 Values by Aquifer')
ax[0].set_xlabel('Aquifer')
ax[0].set_ylabel('Mean Log R^2 Value')
ax[0].set_ylim(0, 1)

ax[1].bar(aquifers, non_lnr2_df, color='orange', alpha=0.7)
ax[1].set_title('Mean Non-Log R^2 Values by Aquifer')
ax[1].set_xlabel('Aquifer')
ax[1].set_ylabel('Mean Non-Log R^2 Value')
ax[1].set_ylim(0, 1)

plt.tight_layout()
plt.show()
"""

#overlay plot of mean log and non-log r^2 values for each aquifer w seaborn
sns.axes_style('whitegrid')
plt.figure(figsize = (10, 6))
plt.bar(aquifers, lnr2_df, color = 'blue', alpha = 0.7, label = 'Mean Log R^2 Values')
plt.bar(aquifers, non_lnr2_df, color = 'yellow', alpha = 0.7, label = 'Mean Non-Log R^2 Values')
plt.title('Mean Log and Non-Log R^2 Values by Aquifer')
plt.xlabel('Aquifer')
plt.ylabel('Mean R^2 Value')
plt.ylim(0, 1)
plt.xticks(rotation = 45)
plt.legend(loc = 'lower left')
plt.tight_layout()

plt.savefig('confidence_in_lognormal/ln_confidence_outputs/mean_r2_values_by_aquifer.png', dpi = 300)