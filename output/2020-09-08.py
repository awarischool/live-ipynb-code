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

plt.figure(figsize=(16, 8))
sns.barplot(data=df, x='job_state', y='avg_salary')

sns.barplot?

df['avg_salary'].hist()

df.head()

df.describe().columns

num_cols = ['Rating', 'Founded', 'hourly', 'employer_provided']
sns.pairplot(df[num_cols])

num_cols = ['min_salary', 'max_salary', 'avg_salary', 'same_state', 'age']
sns.pairplot(df[num_cols])

num_cols = ['python_yn', 'R_yn','spark', 'aws', 'excel', 'desc_len', 'num_comp']
sns.pairplot(df[num_cols])

df.boxplot(column = ['age'])

df['age'].describe()

sns.boxplot(x=df['age'])

df.describe()

correlations_num_vals = df[['avg_salary', 'max_salary', 'min_salary', 'age', 'Rating']].corr()

cmap = sns.diverging_palette(220, 10, as_cmap=True)
sns.heatmap(correlations_num_vals, cmap=cmap, center=0)

cat_cols = ['Location', 'Headquarters', 'Size','Type of ownership', 'Industry', 'Sector', 
       'spark', 'aws', 'excel', 'job_simp', 'seniority']
df_cat = df[cat_cols]

col = cat_cols[0]

cat_num = df_cat[col].value_counts()

cat_num

plt.figure(figsize=(16, 8))
chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
chart = sns.barplot(x=cat_num.index, y=cat_num)
plt.plot()

for col in cat_cols:
  plt.figure(figsize=(16, 8))
  chart = sns.barplot(x=cat_num.index, y=cat_num)
  chart.set_xticklabels(chart.get_xticklabels(), rotation=90)
  cat_num = df_cat[col].value_counts()[:20]
  chart.set_title(col)
  plt.plot()

' '.join(['hello', 'world'])

words = ' '.join(df['Job Description'].values)

#!pip install wordcloud
from wordcloud import WordCloud

words[:1000]

wc = WordCloud()

wc.generate(words[:1000])
plt.sho

 

 