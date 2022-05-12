from scipy import stats
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


############ Create a dataframe for suicide rates and each variable 
df = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/suicide-death-rates.csv')
df_drug = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/share-with-alcohol-or-drug-use-disorders.csv')
df_poverty = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/share-of-population-in-extreme-poverty.csv')
df_pollution = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/share-deaths-air-pollution.csv')
df_hunger = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/prevalence-of-undernourishment.csv')
df_literacy = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/primary-completion-rate.csv')
df_rights = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/human-rights-protection.csv')
df_gdp = pd.read_csv('/Users/williamma/Psych/Research/testing/Psych_Research/gdp-per-capita-in-us-dollar-world-bank.csv')


########### merging attempt


df_list = [df_drug, df_poverty, df_pollution, df_hunger, df_literacy, df_rights, df_gdp]
# df_merged = df

# df_list[0] = df_list[0][df_list[0].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[0], on=['Code', 'Year'], how='inner')
# df_list[1] = df_list[1][df_list[1].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[1], on=['Code', 'Year'], how='inner')

# df_merged.columns

# df_list[2] = df_list[2][df_list[2].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[2], on=['Code', 'Year'], how='inner')
# df_list[3] = df_list[3][df_list[3].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[3], on=['Code', 'Year'], how='inner')
# df_list[4] = df_list[4][df_list[4].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[4], on=['Code', 'Year'], how='inner')
# df_list[5] = df_list[5][df_list[5].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[5], on=['Code', 'Year'], how='inner')
# df_list[6] = df_list[6][df_list[6].Year==2012].drop(columns='Entity')
# df_merged = df_merged.merge(df_list[6], on=['Code', 'Year'], how='inner')

for i in range(len(df_list)):
    df_list[i] = df_list[i][df_list[i].Year==2012].dropna(axis=0)
    # df_merged = df_merged.merge(df_list[i], on=['Code', 'Year'], how='inner')

# print(df_merged)

# df = df[df.Year==2012].drop(columns='Entity')
# df_drug = df_drug[df_drug.Year==2012].drop(columns='Entity')
# df_poverty = df_poverty[df_poverty.Year==2012].drop(columns='Entity')
# df_pollution = df_pollution[df_pollution.Year==2012].drop(columns='Entity')
# df_hunger = df_hunger[df_hunger.Year==2012].drop(columns='Entity')
# df_literacy= df_literacy[df_literacy.Year==2012].drop(columns='Entity')
# df_rights = df_rights[df_rights.Year==2012].drop(columns='Entity')
# df_gdp = df_gdp[df_gdp.Year==2012].drop(columns='Entity')
# df_merged = df.merge(df_drug, on=['Code', 'Year'], how='inner')

# df.merge(df_war, on=['Code', 'Year'], how=)
# df.merge(df_war, on=['Code', 'Year'], how='inner')
# https://pandas.pydata.org/docs/reference/api/pandas.DataFrame.merge.html



####### Clean each dataframe by removing all elements that have no country code (to ensure that the data arrays all have the same length)
# for i in range(len(df["Code"])):
#     if pd.isnull(df.loc[i, 'Code']):
#         df = df.drop(index = i)

# for i in range(len(df_drug["Code"])):
#     if pd.isnull(df_drug.loc[i, 'Code']):
#         df_drug = df_drug.drop(index = i)

# for i in range(len(df_poverty["Code"])):
#     if pd.isnull(df_poverty.loc[i, 'Code']):
#         df_poverty = df_poverty.drop(index = i)

# for i in range(len(df_pollution["Code"])):
#     if pd.isnull(df_pollution.loc[i, 'Code']):
#         df_pollution = df_pollution.drop(index = i)

# for i in range(len(df_hunger["Code"])):
#     if pd.isnull(df_hunger.loc[i, 'Code']):
#         df_hunger = df_hunger.drop(index = i)

# for i in range(len(df_literacy["Code"])):
#     if pd.isnull(df_literacy.loc[i, 'Code']):
#         df_hunger = df_literacy.drop(index = i)

# for i in range(len(df_rights["Code"])):
#     if pd.isnull(df_rights.loc[i, 'Code']):
#         df_rights = df_rights.drop(index = i)

# for i in range(len(df_gdp["Code"])):
#     if pd.isnull(df_gdp.loc[i, 'Code']):
#         df_gdp = df_gdp.drop(index = i)

s = df["Deaths - Self-harm - Sex: Both - Age: Age-standardized (Rate)"]
s_drug = df_drug["Prevalence - Substance use disorders - Sex: Both - Age: Age-standardized (Percent)"]
s_poverty = df_poverty['$1.90 per day - share of population below poverty line']
s_pollution = df_pollution['Deaths - Cause: All causes - Risk: Air pollution - Sex: Both - Age: Age-standardized (Percent)']
s_hunger = df_hunger['Prevalence of undernourishment (% of population)']
s_literacy = df_literacy['Primary completion rate, total (% of relevant age group)']
s_rights = df_rights['Human rights protection']
s_gdp = df_gdp['GDP per capita (constant 2010 US$)']

######### Evaluate the spearman correlation
print(stats.spearmanr(s, s_drug))
print(stats.spearmanr(s, s_poverty))
print(stats.spearmanr(s, s_pollution))
print(stats.spearmanr(s, s_hunger))
print(stats.spearmanr(s, s_literacy))
print(stats.spearmanr(s, s_rights))
print(stats.spearmanr(s, s_gdp))

########### Plot the spearman correlation
df_plot = pd.DataFrame({'Suicide Rates': s,
                   'Drug Use': s_drug})

corr = df_plot.corr(method = 'spearman')

sns.jointplot(x="Suicide Rates", y="Drug Use", data=df_plot, alpha=0.2)

plt.show()


