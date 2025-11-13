import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

poblacion = np.genfromtxt(
    './poblacion_1_enero.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8',
    max_rows=21
)

animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)
poblacion['distrito'] = np.char.strip(poblacion['distrito'])
poblacion['distrito'] = np.char.upper(poblacion['distrito'])
distrito_personas = poblacion['distrito']
num_personas = poblacion['num_personas']


animales2024 = animales[animales['\ufeffAÑO'] > 2023]
distrito_perros = animales2024['DISTRITO']
num_perros = animales2024['ESPECIE_CANINA']

max_personas = num_personas.max()
min_personas = num_personas.min()
max_perros = num_perros.max()
min_perros = num_perros.min()

num_personas_normalizado = (num_personas - min_personas) / (max_personas - min_personas)
num_perros_normalizado = (num_perros - min_perros) / (max_perros - min_perros)

colors_21 = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
    "#393b79",
    "#637939",
    "#8c6d31",
    "#843c39",
    "#7b4173",
    "#3182bd",
    "#e6550d",
    "#31a354",
    "#756bb1",
    "#636363",
    "#bdb76b"
]

distritos_unicos = np.unique(distrito_personas)

cmap_21 = ListedColormap(colors_21)
colores = {distrito: cmap_21(i) for i, distrito in enumerate(distritos_unicos)}
classes = np.arange(21)

size = num_personas / 2

plt.figure(figsize=(8,6))
for distrito in distritos_unicos:
    mask = distrito_personas == distrito
    plt.scatter(
        num_personas_normalizado[mask],
        num_perros_normalizado[mask],
        s=size[mask],
        color=colores[distrito],
        label=distrito
    )

plt.xlabel('Número de personas (normalizado)')
plt.ylabel('Número de perros (normalizado)')
plt.title('Relación entre personas y perros por distrito (normalizado)')
plt.legend(title="Distrito", bbox_to_anchor=(1, 1), loc='upper left')
plt.tight_layout()
plt.show()

