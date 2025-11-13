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

distritos = np.unique(censo['DISTRITO'])

plt.figure(figsize=(10, 5))

primera = True
for d in distritos:
    datos = censo[censo['DISTRITO'] == d]
    plt.plot(datos['ANO'], datos['ESPECIE_CANINA'], color='tab:blue', alpha=0.5, label='Perros' if primera else "_nolegend_")
    plt.plot(datos['ANO'], datos['ESPECIE_FELINA'], color='tab:orange', alpha=0.5,label='Gatos' if primera else "_nolegend_")
    primera = False


plt.title('Evolución por distrito - Colores por especie')
plt.xlabel('Año')
plt.ylabel('Número de animales')
plt.legend()
plt.tight_layout()
plt.savefig('superposicion_totales.png')
