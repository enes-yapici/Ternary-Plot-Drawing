import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpltern

# gridicin
from mpltern.datasets import get_triangular_grid
t, l, r = get_triangular_grid()

df = pd.read_excel("tielinedahilveri.xlsx")
df1 = pd.read_excel('labveri.xlsx')

# DataFrame'i numpy serisi olarak dönüştür
veri_np = df.to_numpy()
veri1_np = df1.to_numpy()

# Verileri ayrıştır
t0, l0, r0 = veri_np.T
# ikinci verileri gir -
t1, l1, r1 = veri1_np.T

# Ternary plot
fig = plt.figure()
ax = fig.add_subplot(projection="ternary")
ax.triplot(t, l, r, color='k', lw='0.2')
ax.scatter(t0, l0, r0, alpha=0.5, label='given data')
ax.scatter(t1, l1, r1, alpha=0.5, label='lab data')
ax.set_tlabel('Acetic acid (W/W,%)')
ax.set_llabel('Water \n(W/W,%)')
ax.set_rlabel('Butyl acetate \n(W/W,%)')

#tie line
ax.plot([0.101, 0.0538], [0.88, 0.0262], [0.019, 0.92], marker='o', color='red')
ax.plot([0.1826, 0.1091], [0.7980, 0.0459], [0.0194, 0.845], marker='o', color='red')
ax.plot([0.2468, 0.1591], [0.7250, 0.0609], [0.0282, 0.78], marker='o', color='red')
ax.plot([0.3066, 0.2154], [0.6510, 0.0896], [0.0424, 0.6950], marker='o', color='red')
ax.plot([0.3671, 0.2764], [0.5550, 0.1236], [0.0779, 0.6000], marker='o', color='red')
ax.plot([0.3671, 0.2764], [0.5550, 0.1236], [0.0779, 0.6000], marker='o', color='red')
ax.plot([0.4001, 0.3275], [0.4900, 0.1795], [0.1099, 0.4930], marker='o', color='red', label='tie line')

# Curve for given data
x, y, z = np.array(list(zip(t0, l0, r0))).T
ax.plot(x, y, z, color='k', alpha=0.8, lw='1', label='curve for given data')

# print legent
ax.legend()

plt.show()
