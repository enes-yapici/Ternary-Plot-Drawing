import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import mpltern

# gridicin
from mpltern.datasets import get_triangular_grid
t, l, r = get_triangular_grid()

df = pd.read_excel("veriler.xlsx")
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
#ax.plot([0.1, 0.2], [0.0, 0.6], [0.1, 0.2], marker='o')

# Curve for given data
x, y, z = np.array(list(zip(t0, l0, r0))).T
ax.plot(x, y, z, color='k', alpha=0.8, lw='1', label='curve for given data')

# print legent
ax.legend()

plt.show()