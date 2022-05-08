from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Create a dataframe for suicide rates and each variable 
df = pd.read_csv('/Users/williamma/downloads/Psych_Research/data/input/suicide-death-rates.csv')
df
s = df["Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)"]

df_drug = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/share-with-alcohol-or-drug-use-disorders.csv')
df_drug
s_drug = df_drug["Prevalence - Substance use disorders - Sex: Both - Age: Age-standardized (Percent)"]

# Clean each dataframe by removing all elements that have no country code (to ensure that the data arrays all have the same length)
for i in range(len(df["Code"])):
    if pd.isnull(df.loc[i, 'Code']):
        df = df.drop(index = i)

for i in range(len(df_drug["Code"])):
    if pd.isnull(df_drug.loc[i, 'Code']):
        df_drug = df_drug.drop(index = i)

# Evaluate the spearman correlation
print(stats.spearmanr(df["Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)"], df_drug["Prevalence - Substance use disorders - Sex: Both - Age: Age-standardized (Percent)"]))

# Plot the spearman correlation
df_plot = pd.DataFrame({'Suicide Rates': s,
                   'Drug Use': s_drug})

corr = df_plot.corr(method = 'spearman')

sns.jointplot(x="Suicide Rates", y="Drug Use", data=df_plot, alpha=0.2)

plt.show()


