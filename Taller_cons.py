
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

# Punto 3
print('municipios afectados: \n' + str(municipios))

# Punto 4
atencion_casa = data[data['Ubicación del caso'] == 'Casa']
print('numero de personas en casa: ' + str(len(atencion_casa)))

# Punto 5
recuperados = data[data['Recuperado'] == 'Recuperado']
print('numero de personas recuperadas: ' + str(len(recuperados)))

# Punto 6
fallecidas = data[data['Ubicación del caso'] == 'Fallecido']
print('numero de personas fallecidas: ' + str(len(fallecidas)))

# Punto 7
tipos_casos = data.groupby('Tipo de contagio').count()
print(tipos_casos['ID'].sort_values(ascending=False))

# Punto 8
departamentos = data['Nombre departamento'].unique()
print('numero de departamentos afectados: ' + str(len(departamentos)))

# Punto 9
print('departamentos afectados: \n' + str(departamentos))

# Punto 10
tipos_casos = data.groupby('Ubicación del caso').count()
print(tipos_casos['ID'].sort_values(ascending=False))

# Punto 11
dep_conta = data.groupby('Nombre departamento').count()
top_10_dep = dep_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_dep)

# Punto 12
dep_falle = fallecidas.groupby('Nombre departamento').count()
print(dep_falle['ID'].sort_values(ascending=False).head(10))

# Punto 13
dep_recu = recuperados.groupby('Nombre departamento').count()
print(dep_recu['ID'].sort_values(ascending=False).head(10))

