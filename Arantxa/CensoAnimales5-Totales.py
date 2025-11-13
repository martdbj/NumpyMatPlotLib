import numpy as np
import matplotlib.pyplot as plt

censo = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    names=True,
    dtype=None,
    encoding='utf-8-sig',
    usecols=(0, 1, 2, 3)
)

# Sumar por año
anyos = np.unique(censo['ANO'])
perros_totales = []
gatos_totales = []

for a in anyos:
    datos = censo[censo['ANO'] == a]
    perros_totales.append(np.sum(datos['ESPECIE_CANINA']))
    gatos_totales.append(np.sum(datos['ESPECIE_FELINA']))

# Graficar totales
plt.figure(figsize=(10, 5))
plt.plot(anyos, perros_totales, label='Perros', color='tab:blue', linewidth=2)
plt.plot(anyos, gatos_totales, label='Gatos', color='tab:orange', linewidth=2)
plt.title('Evolución total del censo - Perros vs Gatos')
plt.xlabel('Año')
plt.ylabel('Número total de animales')
plt.legend()
plt.tight_layout()
plt.savefig('grafica_totales.png')
