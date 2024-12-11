import geopandas as gpd
import pandas as pd 
import os

# Caminhos dos arquivos GeoPackage
gpk_ago = 'desmatamento_ago22.gpkg'
gpk_set = 'desmatamento_set22.gpkg'

# Ler os arquivos GeoPackage em GeoDataFrames
gdf_ago = gpd.read_file(gpk_ago)
gdf_set = gpd.read_file(gpk_set)

# Combinar os GeoDataFrames
gdf_combined = gpd.GeoDataFrame(pd.concat([gdf_ago, gdf_set], ignore_index=True))

# Transformar para a projeção EPSG:31983
gdf_combined = gdf_combined.to_crs(epsg=31983)

output_geojson = 'focos-desmatamento-mg.geojson'
gdf_combined.to_file(output_geojson, driver='GeoJSON')

print(f"Arquivo GeoJSON salvo em {output_geojson}")