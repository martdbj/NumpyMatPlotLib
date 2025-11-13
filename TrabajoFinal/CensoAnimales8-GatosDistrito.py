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

print(animales.dtype)

animales2024 = animales[animales['ANO'] == 2024]
distrito = animales2024['DISTRITO']
numero_gatos = animales2024['ESPECIE_FELINA']

#https://python-charts.com/es/ranking/grafico-barras-matplotlib/
fig, ax = plt.subplots()
plt.xticks(rotation=45, ha='right')
ax.bar(x=distrito, height=numero_gatos)
plt.xlabel('Distrito')
plt.ylabel('Número de gatos')
plt.title('Número de gatos por distrito 2024 MADRID')
plt.show()

print(distrito)
print(numero_gatos)


