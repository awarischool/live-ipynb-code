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
sns.barplot(x=None, y=None, hue=None, data=None, order=None, hue_order=None, estimator=<function mean at 0x7fc2d482f840>, ci=95, n_boot=1000, units=None, seed=None, orient=None, color=None, palette=None, saturation=0.75, errcolor='.26', errwidth=None, capsize=None, dodge=True, ax=None, **kwargs)
Show point estimates and confidence intervals as rectangular bars.
A bar plot represents an estimate of central tendency for a numeric variable with the height of each rectangle and provides some indication of the uncertainty around that estimate using error bars. Bar plots include 0 in the quantitative axis range, and they are a good choice when 0 is a meaningful value for the quantitative variable, and you want to make comparisons against it.
For datasets where 0 is not a meaningful value, a point plot will allow you to focus on differences between levels of one or more categorical variables.

 