import numpy as np
import matplotlib.pyplot as plt

parques_caninos = np.genfromtxt(
    './areas_caninas202511.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8-sig'
)
censo = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    names=True,
    dtype=None,
    encoding='utf-8-sig',
    usecols=(0, 1, 2, 3)
)
# Eliminamos dobles comillas repetitivas del set de datos de parques caninos
parques_caninos['DISTRITO'] = np.char.strip(np.char.replace(parques_caninos['DISTRITO'], '"', ""))

# Ordenamos las listas para que coincidan
distritos_parques = np.unique(parques_caninos['DISTRITO'])
distritos_censo = np.unique(censo['DISTRITO'])
distritos = np.array(sorted(set(distritos_parques) & set(distritos_censo)))

# Parques por distritos
cuenta_parques = np.array([np.sum(parques_caninos['DISTRITO'] == d) for d in distritos])

# Perros 2024 por distrito
cuenta_perros = np.array([
    np.sum(censo[(censo['ANO'] == 2024) & (censo['DISTRITO'] == d)]['ESPECIE_CANINA'])
    for d in distritos
])
cuenta_perros_norm = cuenta_perros / 1000

x = np.arange(len(distritos))
ancho = 0.35

fig, ax = plt.subplots(figsize=(12,6))

ax.bar(x - ancho/2, cuenta_parques, width=ancho, label='Parques Caninos', color='steelblue')
ax.bar(x + ancho/2, cuenta_perros_norm, width=ancho, label='Perros (x1000)', color='tomato')

ax.set_xticks(x)
ax.set_xticklabels(distritos, rotation=45, ha='right')

ax.set_ylabel('Cantidad')
ax.set_title('Parques Caninos vs Perros Normalizados por Distrito')
ax.legend()

plt.tight_layout()
plt.savefig('comp-parques-perros.png')
plt.show()

