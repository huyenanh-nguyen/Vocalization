import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import TwosidedCoupling

 
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
mu = 2.0 # realistic mu value, because the vocal foldds doesnt oscillate sinousidal
beta = 0.3
alpha = 0.2
par0 = x,y,p,q

 
ysolv = []
 
# # [k_up]_________________________________________________________________________________________________________________________________________________
 
# k_up = [0.01, 0.1, 0.2, 0.4, 0.8]
# cmap = plt.get_cmap('viridis', len(k_up))


# for k in k_up:
#   ysolv.append(TwosidedCoupling(par0, t, keep, k, mu, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(k_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(k_up)):
#   axs[i].plot(t[:keep], ysolv[i][:keep], label = "k = " + f"{k_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center left', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
# fig.supylabel("x in a.u.", fontsize = 20)
# fig.supxlabel("t in ms", fontsize = 20)
# plt.savefig(path +"x_ß03_a02_mu2_y01" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()
 
# # [mu_up]_________________________________________________________________________________________________________________________________
 
# mu_up = [0.5, 1.0, 2.0, 3.0, 5.0, 10.0, 20 ]
 
# cmap = plt.get_cmap('viridis', len(mu_up))
 
# xsolv = []

# kk = 0.1
# for m in mu_up:
#   xsolv.append(TwosidedCoupling(par0, t, keep, kk, m, gamma, alpha, beta).x_solv())
 
# fig, axs = plt.subplots(len(mu_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(mu_up)):
#   axs[i].plot(t[:keep], xsolv[i][:keep], label = "$\\mu$ = " + f"{mu_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center left', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
# fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, k = " + f"{kk:.2f}")
# fig.supylabel("x in a.u.", fontsize = 20)
# fig.supxlabel("t in ms", fontsize = 20)
 
# plt.savefig(path +"mu_variation_k01" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()
 

# [alpha_up]_________________________________________________________________________________________________________________________________
 
# alpha_up = [0.0, 0.2, 0.4, 0.8, 1.0]
# ko = 0.4
# cmap = plt.get_cmap('viridis', len(alpha_up))
 
# y_alph_solv = []
 
# for h in alpha_up:
#   y_alph_solv.append(TwosidedCoupling(par0, t, keep, ko, mu, gamma, h, beta).y_solv())
 
# fig, axs = plt.subplots(len(alpha_up), sharex = True, sharey = True, constrained_layout=True)
 
# for i in range(len(alpha_up)):
#   axs[i].plot(t[:keep], y_alph_solv[i][:keep], label = "$\\alpha$ = " + f"{alpha_up[i]:.2f}", color = cmap(i))
#   axs[i].legend(loc='center left', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
# fig.supylabel("y in a.u.", fontsize = 20)
# fig.supxlabel("t in ms", fontsize = 20)
 
# fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, k = " + f"{ko:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
# plt.savefig(path +"alpha_variation_k04" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()

# [beta_up]_________________________________________________________________________________________________________________________________
 
beta_up = [0.0, 0.01, 0.05, 0.1, 0.2 ,0.3]
ko = 0.3
cmap = plt.get_cmap('viridis', len(beta_up))
 
y_alph_solv = []
 
for h in beta_up:
  y_alph_solv.append(TwosidedCoupling(par0, t, keep, ko, mu, gamma, alpha, h).y_solv())
 
fig, axs = plt.subplots(len(beta_up), sharex = True, sharey = True, constrained_layout=True)
 
for i in range(len(beta_up)):
  axs[i].plot(t[:keep], y_alph_solv[i][:keep], label = "$\\beta$ = " + f"{beta_up[i]:.2f}", color = cmap(i))
  axs[i].legend(loc='center left', bbox_to_anchor=(1, 0.5)).get_frame().set_alpha(None)
 
fig.supylabel("y in a.u.", fontsize = 20)
fig.supxlabel("t in ms", fontsize = 20)
 
fig.suptitle("$\gamma$ = " + f"{gamma:.2f}, $\\alpha$ = " + f"{beta:.2f}, k = " + f"{ko:.2f}, $\\mu$ = " + f"{mu:.2f}")
 
plt.savefig(path +"beta_variation_k03" + ".png", dpi =  400, bbox_inches = "tight")
plt.show()