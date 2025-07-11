import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling


# [Parameters]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()

t_step = 0.01
t_last = 100 # 50h -> 1 point represent 1h
t = np.arange(0, 500, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
k_up = np.arange(0.01,10, 0.1)
gamma = 0.1
mu = 2.0
beta = 1.0
alpha = 0.2
reso_alpha = np.arange(0, 4, 0.1)
omega = [np.sqrt(i) for i in reso_alpha]



# [arnolds tongue]________________________________________________________________________________________________________________________________________________


period_vdp = OnesidedCoupling(par, t, keep, 0, mu, gamma, alpha, beta).period(10)[0]
time_amp_vdp = [t[i] for i in OnesidedCoupling(par, t, keep, 0, mu, gamma, alpha, beta).find_peaks_max()[1][0][-10:]]

phase = []
for k_value in k_up:
    time_amp = [t[k] for k in [OnesidedCoupling(par, t, keep, k_value, mu, gamma, i, beta).find_peaks_max()[1][0][-10:] for i in reso_alpha]]
    print(time_amp)
    phaseamp = [2 * np.pi * (time_amp_vdp[0]-i[0])/period_vdp for i in time_amp]
    phase.append(phaseamp)

plt.imshow(np.array(phase),
           cmap = "viridis", 
           origin='lower',
           interpolation='none',
           aspect='equal')
plt.xticks( np.linspace(round(min(np.sqrt(reso_alpha)),2),round(max(np.sqrt(reso_alpha)),2), 6), fontsize = 18)
plt.xlabel("$\\omega _y$ in kHz.",fontsize = 20)
plt.ylabel("k",fontsize = 20)
plt.colorbar().ax.set_ylabel("$\\varphi$", fontsize = 18)
plt.yticks(np.linspace(min(k_up),max(k_up), 5),fontsize = 18)
plt.show()

# plt.plot(omega, phaseamp)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# plt.xticks(np.linspace(min(omega),max(omega), 5), fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel("$\omega$", fontsize = 20)
# plt.ylabel("$\\varphi$",fontsize = 20)
# plt.savefig( path + "phaseshift_k01" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()

