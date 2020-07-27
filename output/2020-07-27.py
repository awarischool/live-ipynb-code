











### 3. Qual seria o melhor preço para as seguites imóveis (coletados da 
 primeira página do OLX)?
- Leste, 2 quartos, 100m2
- Leste, 2 quartos, 43m2
- Sul, 1 quarto, 41m2
- Sul, 1 quarto, 22m2
 #### Brainstorming
- Começar com variável que mais afeta
- Média dos aps com 2 quartos na zona leste
- Categorizar áreas
   - Definir intervalos
- Definir uma equação que correlacione area com aluguel
$$aluguel = area$$

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/WittmannF/awari-calculadora-imoveis-may-20/master/1-web-scraping/dados_calculadora_imoveis_aula.csv

df.head()

min_area = 90
max_area = 120
 df_filtrado = df[(df['zona']=='leste')&(df['quartos']==2.0)]

  df_filtrado = df_filtrado[(df_filtrado['area']>=min_area)&(df_filtrado['area']<=max_area)]

df_filtrado

df_filtrado.describe()

 