import numpy as np
import matplotlib.pyplot as plt

#Es la misma
#https://numpy.org/doc/stable/reference/generated/numpy.genfromtxt.html
animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8'
)

animales2024 = animales[animales['\ufeffAÑO'] ==  2024]
animales2023 = animales[animales['\ufeffAÑO'] ==  2023]
animales2022 = animales[animales['\ufeffAÑO'] ==  2022]
animales2021 = animales[animales['\ufeffAÑO'] ==  2021]

numero_perros2024 = animales2024['ESPECIE_CANINA'].mean()
numero_perros2023 = animales2023['ESPECIE_CANINA'].mean()
numero_perros2022 = animales2022['ESPECIE_CANINA'].mean()
numero_perros2021 = animales2021['ESPECIE_CANINA'].mean()


plt.plot([2021, 2022, 2023, 2024], [numero_perros2021, numero_perros2022, numero_perros2023, numero_perros2024])
plt.xlabel('Año')
plt.ylabel('Número de perros')
plt.title('Media de perros (Distrito) por año MADRID')
plt.show()


