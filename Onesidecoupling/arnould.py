import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.gridspec import GridSpec
from mainscript import OnesidedCoupling
from scipy.signal import spectrogram
import math

# [Parameters]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()

t_step = 0.01
step = 1000
t_last = 200 # 50h -> 1 point represent 1h
t = np.linspace(0, t_last, step, endpoint=False)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
k = [0.1, 4.0, 5.0, 8.0]
gamma = 0.1
mu = 2 # realistic mu value, because the vocal foldds doesnt oscillate sinousidal 
beta = 0.3
alpha = 0.2
par0 = x,y,p,q


# [Frequency]___________________________________________________________________________________________________________________


soli = []
for i in range(len(k)):
    
    sol = OnesidedCoupling(par0, t, keep, i, mu, gamma, alpha, beta).duffvdpsolver()
    par0 = sol[-1]
    soli.append(OnesidedCoupling(par0, t, keep, i, mu, gamma, alpha, beta).y_solv())

fig = plt.figure(figsize=(24, 5))
gs = GridSpec(1, 5, width_ratios=[2,2,2,2, 0.05])
axs = [fig.add_subplot(gs[i]) for i in range(4)]

# Store last mesh for shared colorbar
mesh = None

for i in range(len(k)):
    f, t_spec, Sxx = spectrogram(soli[i], step, nperseg=256, noverlap=128)
    f_scaled = f  # Optional frequency scaling
    Sxx_db = 10 * np.log10(Sxx)  # Convert to dB, avoid log(0)

    mesh = axs[i].pcolormesh(t_spec, f_scaled, Sxx_db, shading='gouraud', cmap='gray')
    axs[i].set_title(f"k = {k[i]:.2f}")
    axs[i].set_xlabel('Time in ms')
    if i == 0:
        axs[i].set_ylabel('Frequency in Hz')

cax = fig.add_subplot(gs[4])
cbar = fig.colorbar(mesh, cax=cax)
cbar.set_label('Intensity in dB')

plt.tight_layout()
plt.show()

