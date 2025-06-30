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
t = np.arange(0, 100, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par0 = x,y,p,q
k_up = np.arange(0.01, 15, 0.01)
k_down = k_up[::-1]

gamma = 0.1
mu = 0.2
beta = 1
alpha = 0.3


# [Functions]____________________________________________________________________________________________________________________

def compute_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'][-10:]
    return amp

# [Bifurcation Duffing_ kchanges]____________________________________________________________________________________________________________________


amplitudes_up = []
amplitudes_down = []

for f in k_up:
    sol = OnesidedCoupling(par0, t, keep, f, mu, gamma, alpha, beta).duffvdpsolver()
    par0 = sol[-1]
    amplitudes_up.append(compute_amplitude(par0, t, keep, f, mu, gamma,alpha, beta))


par0 = sol[-1]

for j in k_down:
    sol = OnesidedCoupling(par0, t, keep, j, mu, gamma, alpha, beta).duffvdpsolver()
    par0 = sol[-1]  
    amplitudes_down.append(compute_amplitude(par0, t, keep, j, mu, gamma, alpha, beta))

for e,k in enumerate(k_up):
    try:
        plt.plot([k]*10, amplitudes_up[e], "k.")
        print(amplitudes_up[e])
    except:
        None

for j,w in enumerate(k_down):
    try:
        plt.plot([w]*10, amplitudes_down[j],"k.")
    except:
        None



plt.xlabel("k", fontsize = 20)
plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

plt.xticks(np.linspace(round(min(k_up),2),round(max(k_up),2), 5), fontsize = 20)
plt.title(label = "$\\alpha$ = " + f"{alpha:.4f}" + ", $\\omega$ = " + f"{np.sqrt(alpha):.4f}", fontsize = 20)

plt.yticks(fontsize = 20)
plt.savefig(path +"Bifurcation_biginterval_y01_dots" +  ".png", dpi =  300, bbox_inches = "tight")
plt.show()


# [Bifurcation Duffing_ omega changes]____________________________________________________________________________________________________________________

# with open(str(Path.cwd()) + "/path.txt") as f:
#   path = f.read()

# t_step = 0.01
# t_last = 100 # 50h -> 1 point represent 1h
# t = np.arange(0, 100, t_step)
# keep = int(t_last / t_step)
# x = 1
# y = 1
# q = 1
# p = 1
# par0 = x,y,p,q
# k = 7.5


# gamma = 0.1
# mu = 0.2
# beta = 1
# alpha_up = np.arange(0.01, 4, 0.01)
# alpha_down = alpha_up[::-1]

# amplitudes_up = []
# amplitudes_down = []

# for f in alpha_up:
#     sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, f, beta).duffvdpsolver()
#     par0 = sol[-1]
#     amplitudes_up.append(compute_amplitude(par0, t, keep, k, mu, gamma, f, beta))


# par0 = sol[-1]

# for j in alpha_down:
#     sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, j, beta).duffvdpsolver()
#     par0 = sol[-1]  
#     amplitudes_down.append(compute_amplitude(par0, t, keep, k, mu, gamma, j, beta))

# for e,k in enumerate(alpha_up):
#     try:
#         plt.plot([k]*10, amplitudes_up[e], "-", color = "#431F6A", markersize= 1)
#         print(amplitudes_up[e])
#     except:
#         None

# for j,w in enumerate(alpha_down):
#     try:
#         plt.plot([w]*10, amplitudes_down[j],'-', color = "#588F75",  markersize= 1, alpha = 0.8)
#     except:
#         None



# plt.xlabel("$\\omega _y$ in Hz", fontsize = 20)
# plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# plt.xticks(np.linspace(round(min(alpha_up),2),round(max(alpha_up),2), 5), fontsize = 20)
# plt.title(label = "k= " + f"{k:.2f}", fontsize = 20)

# plt.yticks(fontsize = 20)
# plt.savefig(path +"Bifurcation_biginterval_y01_k_konstant" +  ".png", dpi =  300, bbox_inches = "tight")
# plt.show()
