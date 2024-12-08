# Agronomiq_Adm
**Testes de adminissão**

As três primeiras atividades estão em arquivos separados sendo:

**Atividade-1.py**
Faça um script que baixa o dataset de municípios do estado de Minas Gerais (usando este LINK, transforme-o em um GeoJSON na projeção EPSG:31983 e salve-o no diretório dados/ com o nome municipios-mg.geojson. Em seguida, neste mesmo script, adicione uma coluna a este vetor contendo a área de cada município em km² e salve o resultado no mesmo arquivo.

**Atividade-2.py**
 Procure uma fonte de dados confiável na internet de população e PIB dos municípios brasileiros e salve os dados de população e PIB dos municípios de Minas Gerais em um arquivo CSV com o nome dados/populacao-pib-municipios-mg.csv.

**Atividade-3.py**
 Utilize os dois arquivos de focos de desmatamento como base (dados/desmatamento_ago22.gpkg e dados/desmatamento_set_22.gpkg), junte-os em um único dataset, transforme-o em um GeoJSON na projeção EPSG:31983 e salve-o em dados/focos-desmatamento-mg.geojson.

**Atividade-4:** desenvolvida no Jutpyter notebook com quatro sub-atividades com o arquivo 02_analise.ipynb

- Qual a área total desmatada em hectares no estado de Minas Gerais em cada um dos meses de agosto e setembro de 2022?
- Qual a área total desmatada em km² no estado de Minas Gerais em todo o período fornecido (ago/set de 2022) por bioma?
- Qual a área total desmatada em km² no estado de Minas Gerais em cada um dos meses de agosto e setembro de 2022, por município?
- No notebook 02_analise.ipynb faça uma análise de correlação entre as variáveis de população e PIB dos municípios de Minas Gerais e a área desmatada em hectares. Apresente os resultados da forma que achar mais adequada.

**Atividade-5:** Objetivo de apresentar alguns resultados que possam contribuir com a gestão pública.
Foram gerados 5 resultados apresentados juntamente com os scripts no projeto "03_visualizacao.ipynb" também no Jupyter notebook

- Área desmatada por municípios
- Área desmatada por bioma/municípios
- Área desmatada por município espacialmente explícito
- Área desmatada por região
- Desmatamento relativo por município com destaque para cidades acima de 1% de desmatamento em relação a área total

**Biliotecas aplicadas nos scripts**
- import pandas as pd
- import geopandas as gpd
- import matplotlib.pyplot as plt
- import seaborn as sns
- import numpy as np
- import matplotlib as mpl
- import requests
- import os

