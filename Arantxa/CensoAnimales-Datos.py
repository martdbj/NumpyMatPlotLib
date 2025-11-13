import numpy as np

censo = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    names=True,              # usa la primera fila como nombres de columna
    dtype=None,              # infiere el tipo de cada columna (texto/número)
    encoding='utf-8-sig',        # importante por los acentos
    usecols=(0, 1, 2, 3)
)
# Print nombres de columnas en nuestros datos
print(censo.dtype.names)

# Creamos una lista con los distritos únicos que aparecen en nuestros datos
distritos = np.unique(censo['DISTRITO'])
print(distritos)

# Creamos una lista de todos los años en los que se recolectaron datos en nuestros datos
anyos = np.unique(censo['ANO'])
print(anyos)

# Generamos matrices individuales por distrito
for d in distritos:
    datos = censo[censo['DISTRITO'] == d]
    matriz = np.column_stack((datos['ANO'], datos['ESPECIE_CANINA'], datos['ESPECIE_FELINA']))
    print(f"{d}:")
    print(matriz)

