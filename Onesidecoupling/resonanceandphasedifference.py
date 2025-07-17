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
k = 0.01
gamma = 0.1
mu = 2.0
beta = 0.3
alpha = 0.2
reso_alpha = np.arange(0, 4, 0.01)
omega = [np.sqrt(i) for i in reso_alpha]

# [Resonance Duffing]____________________________________________________________________________________________________________________________________


# cmap = plt.get_cmap('viridis', len([0.1,0.3,1.0,5.0]))
# for b_index, b in enumerate([0.3,1.0,5.0]):
#   amp = [np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, i, b).find_peaks_max()[1][1]['peak_heights'][-10:]) for i in reso_alpha]
#   plt.plot(omega, amp, label = "$\\beta$ = " + f"{b:.2f}", color = cmap(b_index))
# plt.legend(loc = "best", fontsize = 14)

# # amp = [np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, i, beta).find_peaks_max()[1][1]['peak_heights'][-10:]) for i in reso_alpha]
# # plt.plot(omega, amp)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# plt.xticks(np.linspace(min(omega),max(omega), 5), fontsize = 12)
# plt.yticks(fontsize = 12)
# plt.xlabel("$\omega _y$ in kHz", fontsize = 14)
# plt.ylabel("A$_y$ in a.u.",fontsize = 14)
# plt.savefig( path + "resonance_k001_multipleß" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()



# [Resonance_Lorentzcurve (van der Pol)]____________________________________________________________________________________________________________________________________

def lorenz(x, omega, gamma):
    return 0.02 / np.sqrt((x**2 - omega ** 2)**2 + gamma ** 2 * x ** 2)

lorenz_sol = [lorenz(i, 0.82, 0.1) for i in omega]
amp = [np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, i, beta).find_peaks_max()[1][1]['peak_heights'][-10:]) for i in reso_alpha]

plt.plot(omega, amp, label = "Simulation")
plt.plot(omega, lorenz_sol, label = "Lorentz Curve")

plt.legend(fontsize = 14, loc = "lower right")
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.xticks(np.linspace(min(omega),max(omega), 5),fontsize = 12)
plt.yticks(fontsize = 12)
plt.xlabel("$\omega _y$ in kHz", fontsize = 14)
plt.ylabel("A$_y$,A$_{Lorentz}$ in cm",fontsize = 14)
plt.savefig( path + "resonance_lorentz_k001" + ".png", dpi =  300, bbox_inches = "tight")
plt.show()

# [Phaseshift Duffing]___________________________________________________________________________________________________________________________________



# period_vdp = OnesidedCoupling(par, t, keep, k, mu, gamma, 0.2, beta).period(10)[0]
# time_amp_vdp = [t[i] for i in OnesidedCoupling(par, t, keep, k, mu, gamma, 0.2, beta).find_peaks_max()[1][0][-10:]]

# time_amp = [t[k] for k in [OnesidedCoupling(par, t, keep, k, mu, gamma, i, beta).find_peaks_max()[1][0][-10:] for i in reso_alpha]]
# phaseamp = [2 * np.pi * (time_amp_vdp[0]-i[0])/period_vdp for i in time_amp]

# plt.plot(omega, phaseamp)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# plt.xticks(np.linspace(min(omega),max(omega), 5), fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.xlabel("$\omega$", fontsize = 20)
# plt.ylabel("$\\varphi$",fontsize = 20)
# plt.savefig( path + "phaseshift_k01" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()