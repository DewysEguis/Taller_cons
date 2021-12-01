
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

# Punto 14
mun_conta = data.groupby('Nombre municipio').count()
top_10_mun = mun_conta['ID'].sort_values(ascending=False).head(10)
print(top_10_mun)

# Punto 15
mun_falle = fallecidas.groupby('Nombre municipio').count()
print(mun_falle['ID'].sort_values(ascending=False).head(10))

# Punto 16
mun_recu = recuperados.groupby('Nombre municipio').count()
print(mun_recu['ID'].sort_values(ascending=False).head(10))

# Punto 17
print(dep_conta)

# Punto 18
contageado_sexo = data.groupby('Sexo')
print(contageado_sexo.count()['ID'])

# Punto 19
list_by = ['Sexo', 'Nombre municipio', 'Nombre departamento']
print(data.groupby(list_by)['Edad'].mean())

# Punto 20
pais_procedencia = data.groupby('Nombre del país').count()
print(pais_procedencia['ID'].sort_values(ascending=False))

# Punto 21
print(data.sort_values(ascending=False, by='Fecha de diagnóstico'))

# Punto 22
tasa_mortalidad = (len(fallecidas) / len(data)) * 100
tasa_recuperacion = (len(recuperados) / len(data)) * 100
print('tasa de mortalidad: ' + "{:.6f}".format(tasa_mortalidad))
print('tasa de recuperación: ' + "{:.6f}".format(tasa_recuperacion))

# Punto 23
print('tasa de mortalidad:')
print(dep_falle['ID'] / len(data) * 100)
print('\ntasa de recuperación:')
print(dep_recu['ID'] / len(data) * 100)

# Punto 24
print('tasa de mortalidad:')
print(mun_falle['ID'] / len(data) * 100)
print('\ntasa de recuperación:')
print(mun_recu['ID'] / len(data) * 100)

# Punto 25
print(data.groupby(['Nombre municipio', 'Ubicación del caso'])['ID'].count())
