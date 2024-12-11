import pprint
import requests
import pandas as pd

###### População
url = "https://servicodados.ibge.gov.br/api/v3/agregados/6579/periodos/2024/variaveis/9324?localidades=N1[all]|N6[N3[31]]"

response = requests.get(url)
data = response.json()

dados_extraidos = []

# extrair as informações desejadas
for resultado in data[0]['resultados']:
    for serie in resultado['series']:
        localidade = serie['localidade']
        id_municipio = localidade['id']
        nome_municipio = localidade['nome']
        populacao_2024 = serie['serie'].get('2024', None)  # Obter a população para 2024

        # Adicionar os dados extraídos à lista
        dados_extraidos.append({
            'ID': id_municipio,
            'Municipio': nome_municipio,
            'Populacao 2024': populacao_2024
        })

df_pop = pd.DataFrame(dados_extraidos)

output_file = 'populacao_municipios_2024.csv'
df_pop.to_csv(output_file, index=False, encoding='utf-8')

print(f"Dados salvos em {output_file}")

###### PIB
url = "https://servicodados.ibge.gov.br/api/v3/agregados/21/periodos/2012/variaveis/37?localidades=N6[N3[31]]"

# Fazer a requisição e obter os dados JSON
response = requests.get(url)
data = response.json()

dados_extraidos = []

# extrair as informações desejadas
for resultado in data[0]['resultados']:
    for serie in resultado['series']:
        localidade = serie['localidade']
        id_municipio = localidade['id']
        nome_municipio = localidade['nome']
        pib_2012 = serie['serie'].get('2012', None)

        # Adicionar os dados extraídos à lista
        dados_extraidos.append({
            'ID': id_municipio,
            'Municipio': nome_municipio,
            'PIB': pib_2012
        })

dfPIB = pd.DataFrame(dados_extraidos)

output_file = 'pib_municipios_2012.csv'
dfPIB.to_csv(output_file, index=False, encoding='utf-8')

print(f"Dados salvos em {output_file}")


###### união das duas bases
# Combinar os DataFrames usando 'ID' como chave
df_combinado = pd.merge(df_pop, dfPIB, on='ID', how='inner')

# Selecionar e renomear as colunas
df_combinado = df_combinado[['ID', 'Municipio_x', 'Populacao 2024', 'PIB']]
df_combinado.columns = ['ID', 'Municipio', 'Populacao', 'PIB']

# Salvar o DataFrame combinado em um novo arquivo CSV
output_file = 'populacao-pib-municipios-mg.csv'
df_combinado.to_csv(output_file, index=False, encoding='utf-8')

print(f"Dados combinados salvos em {output_file}")