import requests
import geopandas as gpd
from pyproj import CRS

# URL do dataset de municípios de Minas Gerais
url = "https://raw.githubusercontent.com/tbrugz/geodata-br/master/geojson/geojs-31-mun.json"

path_output = "D:/Projetos/Agronomiq/Teste_Adm/"
file_output = "municipios-mg.geojson"

# Baixar o arquivo GeoJSON
response = requests.get(url)
if response.status_code == 200:
    with open(path_output + "municipios-mg-original.geojson", 'w', encoding='utf-8') as file:
        file.write(response.text)
else:
    print("Erro ao baixar o arquivo:", response.status_code)
    exit()

# Ler geojson e transforma para a projeção EPSG:31983
gdf = gpd.read_file(path_output + "municipios-mg-original.geojson")
gdf = gdf.to_crs(CRS.from_epsg(31983))
gdf['area_km2'] = gdf.geometry.area / 10**6

gdf.to_file(path_output + file_output, driver='GeoJSON')

print(f"Arquivo salvo em {path_output}{file_output}")
#