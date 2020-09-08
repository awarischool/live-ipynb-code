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

sns.barplot(data=df.groupby('job_simp').mean()['avg_salary'], )

 