import numpy as np
import matplotlib.pyplot as plt

poblacion = np.genfromtxt(
    './poblacion_1_enero.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8',
    max_rows=21
)

distrito = poblacion['distrito']
num_personas = poblacion['num_personas']

fig, ax = plt.subplots()
plt.xticks(rotation=45, ha='right')
ax.bar(x=distrito, height=num_personas)
plt.show()

