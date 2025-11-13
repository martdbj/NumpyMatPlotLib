import numpy as np
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

animales = np.genfromtxt(
    './censo_animales.csv',
    delimiter=';',
    dtype=None,
    names=True,
    encoding='utf-8-sig'
)

print(animales.dtype)