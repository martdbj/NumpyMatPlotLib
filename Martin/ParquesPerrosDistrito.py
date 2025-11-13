import numpy as np
import matplotlib.pyplot as plt

parques_caninos = np.genfromtxt(
    './areas_caninas202511.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)

#https://numpy.org/devdocs/reference/generated/numpy.unique_counts.html
distrito, cantidad = np.unique(parques_caninos['DISTRITO'], return_counts=True)

fig, ax = plt.subplots()
plt.xticks(rotation=45, ha='right')
ax.bar(x=distrito, height=cantidad)
plt.show()

print(distrito)
print(cantidad)

