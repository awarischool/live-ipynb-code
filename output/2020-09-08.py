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

plt.figure(figsize=(12, 8))
sns.barplot(data=df, x='job_simp', y='avg_salary')

df['avg_salary'].hist()

df.head()

df.describe().columns

num_cols = ['Rating', 'Founded', 'hourly', 'employer_provided']
sns.pairplot(df[num_cols])

num_cols = ['min_salary', 'max_salary', 'avg_salary', 'same_state', 'age']
sns.pairplot(df[num_cols])

num_cols = ['python_yn', 'R_yn','spark', 'aws', 'excel', 'desc_len', 'num_comp']
sns.pairplot(df[num_cols])

 