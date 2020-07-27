













import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/WittmannF/awari-calculadora-imoveis-may-20/master/1-web-scraping/dados_calculadora_imoveis_aula.csv

df.head()

min_area = 90
max_area = 120
 df_filtrado = df[(df['zona']=='leste')&(df['quartos']==2.0)]

  df_filtrado = df_filtrado[(df_filtrado['area']>=min_area)&(df_filtrado['area']<=max_area)]

df_filtrado

df_filtrado.describe()

df_onehot = pd.get_dummies(df)

df_onehot.head()



# Definir y - O que queremos prever
y = df_onehot['preco']
y.head()

# Definir entrada (todas as colunas menos o preço)
X = df_onehot.drop('preco', axis=1)
X.head()

# Regressão Linear
# 𝑎𝑙𝑢𝑔𝑢𝑒𝑙=𝑎𝑟𝑒𝑎∗𝑤1+𝑞𝑢𝑎𝑟𝑡𝑜𝑠∗𝑤2+𝑧𝑙𝑒𝑠𝑡𝑒∗𝑤3+𝑧𝑛𝑜𝑟𝑡𝑒∗𝑤4+𝑧𝑜𝑒𝑠𝑡𝑒∗𝑤5+𝑧𝑠𝑢𝑙∗𝑤6+𝑏
from sklearn.linear_model import LinearRegression
 LinearRegression()
 def LinearRegression(fit_intercept=True, normalize=False, copy_X=True, n_jobs=None)
View source
Ordinary least squares Linear Regression.
LinearRegression fits a linear model with coefficients w = (w1, ..., wp) to minimize the residual sum of squares between the observed targets in the dataset, and the targets predicted by the linear approximation.
Parameters
fit_intercept : bool, optional, default True
    Whether to calculate the intercept for this model. If set  
    to False, no intercept will be used in calculations  
    (i.e. data is expected to be centered).  
normalize : bool, optional, default False

X

y

# Árvore de Decisão
# Definir sequencia de regras para "chutar" o preço

# k Nearest Neighbors
# k vizinhos mais próximos

 