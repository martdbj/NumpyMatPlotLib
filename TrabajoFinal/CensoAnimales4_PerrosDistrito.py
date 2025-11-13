import numpy as np
import matplotlib.pyplot as plt

#https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html
animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8-sig'
)

animales2024 = animales[animales['ANO'] > 2023]
distrito = animales2024['DISTRITO']
numero_perros = animales2024['ESPECIE_CANINA']

#https://python-charts.com/es/ranking/grafico-barras-matplotlib/
fig, ax = plt.subplots()
plt.xticks(rotation=45, ha='right')
ax.bar(x=distrito, height=numero_perros)
plt.xlabel('Distrito')
plt.ylabel('Número de perros')
plt.title('Número de perros por distrito 2024 MADRID')
plt.tight_layout()
plt.savefig('numero_perros_distrito2024.png')
plt.show()




