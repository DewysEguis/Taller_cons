
import pandas as pd

url = 'covid_22_noviembre.csv'
data = pd.read_csv(url, low_memory=False)

data.rename(columns={'ID de caso': 'ID'}, inplace=True)

data['Ubicación del caso'].replace('CASA', 'Casa', inplace=True)
data['Recuperado'].replace('fallecido', 'Fallecido', inplace=True)
data['Tipo de contagio'].replace('relacionado', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('RELACIONADO', 'Relacionado', inplace=True)
data['Tipo de contagio'].replace('EN ESTUDIO', 'En estudio', inplace=True)
data['Tipo de contagio'].replace('En Estudio', 'En estudio', inplace=True)
data['Sexo'].replace('m', 'M', inplace=True)
data['Sexo'].replace('f', 'F', inplace=True)

# Punto 1 
print('numero de casos de contagio: ' + str(len(data)))

# Punto 2
municipios = data['Nombre municipio'].unique()
print('numero de municipios afectados: ' + str(len(municipios)))