import pandas as pd
url = 'https://github.com/PlayingNumbers/ds_salary_proj/raw/master/eda_data.csv'
df = pd.read_csv(url, index_col=0)

df.head()

df.info()

df.describe().T

df['Job Title'].value_counts(normalize=True)

df['job_simp'].value_counts()

df[df['job_simp']=='na'].head()

df.groupby('job_simp').mean()['avg_salary']

job_state_avg_salary = df.groupby('job_state').mean()['avg_salary']

job_state_avg_salary.sort_values(ascending=False).head()

import seaborn as sns
import matplotlib.pyplot as plt
 

import seaborn as sns
tips = sns.load_dataset("tips")
ax = sns.barplot(x="day", y="total_bill", data=tips)

tips.head()

df.groupby('job_simp').mean()['avg_salary']

plt.figure(figsize=(12, 8))
sns.barplot(data=df, x='job_simp', y='avg_salary')

df['avg_salary'].hist()

sns.
barplot
sns.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean at 0x7fc2d482f840>, ci=95, n_boot=1000, units=None, seed=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)
blend_palette
boxenplot
boxplot
categorical
catplot
choose_colorbrewer_palette
choose_cubehelix_palette
choose_dark_palette
choose_diverging_palette
choose_light_palette
clustermap