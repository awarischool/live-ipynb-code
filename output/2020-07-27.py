













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

X
X
DataFrame

X.fillna()

# Regressão Linear
# 𝑎𝑙𝑢𝑔𝑢𝑒𝑙=𝑎𝑟𝑒𝑎∗𝑤1+𝑞𝑢𝑎𝑟𝑡𝑜𝑠∗𝑤2+𝑧𝑙𝑒𝑠𝑡𝑒∗𝑤3+𝑧𝑛𝑜𝑟𝑡𝑒∗𝑤4+𝑧𝑜𝑒𝑠𝑡𝑒∗𝑤5+𝑧𝑠𝑢𝑙∗𝑤6+𝑏
from sklearn.linear_model import LinearRegression
 reg = LinearRegression()
 

reg.fit(X, y)

y

# Árvore de Decisão
# Definir sequencia de regras para "chutar" o preço

# k Nearest Neighbors
# k vizinhos mais próximos

 