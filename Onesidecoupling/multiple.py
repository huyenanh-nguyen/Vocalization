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
mu = 5 # realistic mu value, because the vocal foldds doesnt oscillate sinousidal
beta = 0.3
alpha = 0.2
par0 = x,y,p,q

 
ysolv = []
 
# # [k_up]_________________________________________________________________________________________________________________________________________________
 
k_up = [0.04, 0.1, 0.376, 1.4, 1.5,2.3]
cmap = plt.get_cmap('viridis', len(k_up))


for k in k_up:
  ysolv.append(OnesidedCoupling(par0, t, keep, k, mu, gamma, alpha, beta).y_solv())
 
fig, axs = plt.subplots(len(k_up), sharex = True, sharey = True, constrained_layout=True)
 
for i in range(len(k_up)):
  axs[i].plot(t[:keep], ysolv[i][:keep], label = "k = " + f"{k_up[i]:.2f}", color = cmap(i))
  axs[i].legend(loc='center right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
fig.supylabel("y in a.u.", fontsize = 20)
fig.supxlabel("t in ms", fontsize = 20)
plt.savefig(path +"ß03_a02_mu10_y01" + ".png", dpi =  400, bbox_inches = "tight")
plt.show()
 
# # [mu_up]_________________________________________________________________________________________________________________________________
 
mu_up = [0.5, 2.0,5.0, 10.0]
 
cmap = plt.get_cmap('viridis', len(mu_up))
 
xsolv = []
 
# for m in mu_up:
#   xsolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(mu_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(mu_up)):
#   axs[i].plot(t[:keep], xsolv[i][:keep], label = "$\\mu$ = " + f"{mu_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("x in a.u.", fontsize = 14)
# fig.supxlabel("t in ms", fontsize = 14)
 
# plt.savefig(path +"timeseries_mu_variation" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()

######## Phaseplane #######
# xsolv = []
# psolv = []
# for m in mu_up:
#   psolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).p_solv())
#   xsolv.append(OnesidedCoupling(par0, t, keep, 0, m, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(mu_up), sharey = True, sharex = True, constrained_layout=True)
 
# for i in range(len(mu_up)):
#   axs[i].plot(psolv[i][:keep], xsolv[i][:keep], label = "$\\mu$ = " + f"{mu_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='upper right', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("x in a.u.", fontsize = 14)
# fig.supxlabel("p in a.u.", fontsize = 14)
 
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