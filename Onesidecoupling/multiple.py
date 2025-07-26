import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling
 
with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()
 
t_step = 0.01
t_last = 100 # 50h -> 1 point represent 1h
t = np.arange(0, 200, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
gamma = 0.1
mu = 10 # realistic mu value, because the vocal foldds doesnt oscillate sinousidal
beta = 0.3
alpha = [0.2]
par0 = x,y,p,q

 
ysolv = []
 
# # [k_up]_________________________________________________________________________________________________________________________________________________
 
# k_up = [0.1,4.0, 5.0, 8.0]
# cmap = plt.get_cmap('viridis', len(k_up))


# for k in k_up:
#   ysolv.append(OnesidedCoupling(par0, t, keep, k, mu, gamma, alpha, beta).y_solv())
 
# fig, axs = plt.subplots(len(k_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(k_up)):
#   axs[i].plot(t[:keep], ysolv[i][:keep], label = "k = " + f"{k_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# # fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
# fig.supylabel("y in cm", fontsize = 14)
# fig.supxlabel("t in ms", fontsize = 14)
# plt.savefig(path +"timeseries_differentk" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()
 
# # # [mu_up]_________________________________________________________________________________________________________________________________
 
# mu_up = [0.5, 2.0,5.0, 10.0]
 
# cmap = plt.get_cmap('viridis', len(mu_up))
 
# xsolv = []
 
# for m in mu_up:
#   xsolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(mu_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(mu_up)):
#   axs[i].plot(t[:keep], xsolv[i][:keep], label = "$\\mu$ = " + f"{mu_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("x in cm", fontsize = 14)
# fig.supxlabel("t in ms", fontsize = 14)
 
# plt.savefig(path +"timeseries_mu_variation" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()

# ######## Phaseplane #######
# xsolv = []
# psolv = []
# for m in mu_up:
#   psolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).p_solv())
#   xsolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(mu_up), sharey = True, sharex = True, constrained_layout=True)
 
# for i in range(len(mu_up)):
#   axs[i].plot(psolv[i][:keep], xsolv[i][:keep], label = "$\\mu$ = " + f"{mu_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='upper right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("x in cm", fontsize = 14)
# fig.supxlabel("p in cm", fontsize = 14)
 
# plt.savefig(path +"phaseplane_mu_variation" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()
 

# [alpha_up]_________________________________________________________________________________________________________________________________
 
# alpha_up = [0.0, 0.2, 0.4, 0.8, 1.0]
# ko = 5.0
 
# cmap = plt.get_cmap('viridis', len(alpha_up))
 
# y_alph_solv = []
 
# for h in alpha_up:
#   y_alph_solv.append(OnesidedCoupling(par0, t, keep, ko, mu, gamma, h, beta).y_solv())
 
# fig, axs = plt.subplots(len(alpha_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(alpha_up)):
#   axs[i].plot(t[:keep], y_alph_solv[i][:keep], label = "$\\alpha$ = " + f"{alpha_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("y in a.u.", fontsize = 20)
# fig.supxlabel("t in ms", fontsize = 20)
 
# fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, k = " + f"{ko:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
# plt.savefig(path +"alpha_variation_k5" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()




# [bifurcation and timeseries]_____________________________________________________________________________

def compute_all_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).getting_all_peaks()[1][1]['peak_heights'][-10:]
    return amp
 
k_up = [0.1,1.3, 1.5, 8.0]
cmap = plt.get_cmap('viridis', len(k_up)+2)


for k in k_up:
  ysolv.append(OnesidedCoupling(par0, t, keep, k, mu, gamma, alpha[0], beta).y_solv())
 
fig = plt.figure(figsize=(12, 8), constrained_layout=True)
gs = fig.add_gridspec(len(k_up), 2, width_ratios=[2, 1])

ax_big = fig.add_subplot(gs[:, 0])
amplitudes_up = []

par0 = x,y,p,q

for i in range(len(alpha)):
    for f in np.arange(0, 10, 0.01):
        sol = OnesidedCoupling(par0, t, keep, f, mu, gamma, alpha[i], beta).duffvdpsolver()
        par0 = sol[-1]
        amplitudes_up.append(compute_all_amplitude(par0, t, keep, f, mu, gamma, alpha[i], beta))

    for e, k in enumerate(np.arange(0, 10, 0.01)):
        try:
            ax_big.plot([k]*len(amplitudes_up[e]), amplitudes_up[e], "k.", markersize=0.5)
        except:
            pass
        
ax_big.set_xlabel("k", fontsize=22)
ax_big.set_ylabel("A$_{y}$ in cm", fontsize=22)
ax_big.xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
ax_big.set_xticks(np.linspace(round(min(k_up), 2), round(max(k_up), 2), 5))
ax_big.tick_params(axis='x', labelsize=20)
ax_big.tick_params(axis='y', labelsize=20)
for g, z in enumerate(k_up):
    ax_big.axvline(x=z, color=cmap(g))

# stacked timeseries on the right
axs_right = []
for i in range(len(k_up)):
    ax = fig.add_subplot(gs[i, 1])
    ax.plot(t[:keep], ysolv[i][:keep], label=f"k = {k_up[i]:.2f}", color=cmap(i))
    ax.legend(loc='center right', bbox_to_anchor=(1.0, 0.5), fontsize = 16).get_frame().set_alpha(None)
    if i == len(k_up) - 1:
        ax.set_xlabel("t in ms", fontsize=22)
    if i == 1:
        ax.set_ylabel("y in cm", fontsize=22)
    axs_right.append(ax)
    

    ax.tick_params(axis='both', labelsize=20)

plt.savefig(path +"Mu10alpha5_bifurcation_timeseries" + ".png", dpi =  400, bbox_inches = "tight")
plt.show()
 