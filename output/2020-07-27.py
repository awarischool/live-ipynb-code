











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
$$aluguel = area * w + b$$
 - Extendendo a equação da reta para todas as colunas
$$aluguel = area * w_1 + quartos * w_2 + b$$
 #### Problemas
- Como tratar a coluna zonas
   - S1: Associar um número inteiro para cada zona (1 - Norte, 2 - Sul, 3 
- Leste, 4 - Oeste)
       - P: Não há proporcionalidade entre zonas
   - Associar uma nova "variável" para cada zona
 

import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/WittmannF/awari-calculadora-imoveis-may-20/master/1-web-scraping/dados_calculadora_imoveis_aula.csv

df.head()

min_area = 90
max_area = 120
 df_filtrado = df[(df['zona']=='leste')&(df['quartos']==2.0)]

  df_filtrado = df_filtrado[(df_filtrado['area']>=min_area)&(df_filtrado['area']<=max_area)]

df_filtrado

df_filtrado.describe()

pd.get_dummies(df)

 