import numpy as np
import matplotlib.pyplot as plt


X, Y = np.meshgrid(np.linspace(-3, 3, 256), np.linspace(-5, 5, 256))
Z = (1 - 0.5*X + X**5 + Y**3) * np.exp(-X**2 - Y**2)

fig, axs = plt.subplots(1, 2)

pc = axs[0].pcolormesh(X, Y, Z, vmin=-1, vmax=1, cmap='RdBu_r')
fig.colorbar(pc, ax=axs[0])
axs[0].set_title('pcolormesh()')

co = axs[1].contour(X, Y, Z, levels=np.linspace(-1.25, 1.25, 11), colors=[
    '#98FB98',  # PaleGreen
    '#8FBC8F',  # DarkSeaGreen
    '#66CDAA',  # MediumAquamarine
    '#20B2AA',  # LightSeaGreen
    '#5F9EA0',  # CadetBlue
    '#4682B4',  # SteelBlue
    '#87CEEB',  # SkyBlue
    '#00BFFF',  # DeepSkyBlue
    '#1E90FF',  # DodgerBlue
    '#6495ED',  # CornflowerBlue
    '#ADD8E6'   # LightBlue
])
axs[1].clabel(co, inline=True, fontsize=8)
fig.colorbar(co, ax=axs[1])
axs[1].set_title('contour()')

plt.show()
