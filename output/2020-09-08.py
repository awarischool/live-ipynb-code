import pandas as pd
url = 'https://github.com/PlayingNumbers/ds_salary_proj/raw/master/eda_data.csv'
df = pd.read_csv(url, index_col=0)

df.head()

df.info()

df.describe()

[1 3 5 7 9 10 12 15]