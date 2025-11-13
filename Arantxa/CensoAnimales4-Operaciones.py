import numpy as np
import matplotlib.pyplot as plt

censo = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    names=True,              # usa la primera fila como nombres de columna
    dtype=None,              # infiere el tipo de cada columna (texto/número)
    encoding='utf-8-sig',        # importante por los acentos
    usecols=(0, 1, 2, 3)
)
anyos = np.unique(censo['ANO'])

#Totales por año
totalPerros = []
totalGatos = []
for a in anyos:
    datos = censo[censo['ANO'] == a]
    totalPerros.append(np.sum(datos['ESPECIE_CANINA']))
    totalGatos.append(np.sum(datos['ESPECIE_FELINA']))

# Promedio de perros/gatos en la ciudad
mediaPerros = np.mean(totalPerros)
mediaGatos = np.mean(totalGatos)

# Gráfica Scatter con puntos para cada año perro/gato y línea de puntos que marca la media
plt.figure(figsize=(10, 5))
plt.scatter(anyos, totalPerros, color='tab:blue', label='Perros')
plt.scatter(anyos, totalGatos, color='tab:orange', label='Gatos')
plt.axhline(mediaPerros, color='tab:blue', linestyle='--')
plt.axhline(mediaGatos, color='tab:orange', linestyle='--')
plt.title("Comparación número animales por año")
plt.xlabel("Año")
plt.ylabel("Número total de animales")
plt.legend()
plt.savefig('media_y_totales.png')

# Normalización de los datos por año de perros y gatos
perros_norm = (totalPerros - np.min(totalPerros)) / (np.max(totalPerros) - np.min(totalPerros))
gatos_norm  = (totalGatos - np.min(totalGatos)) / (np.max(totalGatos) - np.min(totalGatos))

# Gráfica con datos normalizados
plt.figure(figsize=(10,5))
plt.plot(anyos, perros_norm, label='Perros (normalizado)', color='tab:green')
plt.plot(anyos, gatos_norm, label='Gatos (normalizado)', color='tab:red')
plt.title('Evolución relativa (normalizada) de perros y gatos')
plt.xlabel('Año')
plt.ylabel('Proporción del máximo anual')
plt.legend()
plt.tight_layout()
plt.savefig('normalizacion.png')
