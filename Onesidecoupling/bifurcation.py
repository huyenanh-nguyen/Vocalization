import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling


# [Parameters]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()

t_step = 0.01
t_last = 200 # 50h -> 1 point represent 1h
t = np.arange(0, 200, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
k = 0.1
gamma = 0.1
mu = 10 # realistic mu value, because the vocal foldds doesnt oscillate sinousidal 
beta = 0.3
alpha = [0.2]
par0 = x,y,p,q
k_up = np.arange(0, 10, 0.01)
k_down = k_up[::-1]


# [Functions]____________________________________________________________________________________________________________________

def compute_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'][-10:]
    return amp

def compute_all_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).getting_all_peaks()[1][1]['peak_heights'][-10:]
    return amp

def compute_periodic_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).y_periodic_peak()
    return amp

# [Bifurcation Duffing_ kchanges, maximal peaks]____________________________________________________________________________________________________________________


# amplitudes_up = []
# amplitudes_down = []
# for i in range(len(alpha)):
#     for f in k_up:
#         sol = OnesidedCoupling(par0, t, keep, f, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]
#         amplitudes_up.append(compute_amplitude(par0, t, keep, f, mu, gamma,alpha[i], beta))


#     par0 = sol[-1]

#     for j in k_down:
#         sol = OnesidedCoupling(par0, t, keep, j, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]  
#         amplitudes_down.append(compute_amplitude(par0, t, keep, j, mu, gamma, alpha[i], beta))

#     for e,k in enumerate(k_up):
#         try:
#             plt.plot([k]*len(amplitudes_up[e]), amplitudes_up[e], "k.", markersize = 0.5)
#             print(amplitudes_up[e])
#         except:
#             None

#     for j,w in enumerate(k_down):
#         try:
#             plt.plot([w]*len(amplitudes_down[j]), amplitudes_down[j],"r.", markersize = 0.5)
#         except:
#             None



#     plt.xlabel("k", fontsize = 20)
#     plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
#     plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
#     plt.title(label = "$\\alpha$ = " + f"{alpha[i]:.4f}" + ", $\\omega$ = " + f"{np.sqrt(alpha[i]):.4f}", fontsize = 20)
#     plt.xticks(np.linspace(round(min(k_up),2),round(max(k_up),2), 5), fontsize = 20)
#     plt.title(label = "$\\alpha$ = " + f"{alpha[i]:.2f}" + ", $\\omega$ = " + f"{np.sqrt(alpha[i]):.2f}", fontsize = 20)

#     plt.yticks(np.linspace(-4,6,6), fontsize = 20)
#     plt.savefig(path +"Bifurcation_max" + "alpha06"+  ".png", dpi =  300, bbox_inches = "tight")
#     # plt.show()

# [Bifurcation all peaks]__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# amplitudes_up = []
# amplitudes_down = []
# for i in range(len(alpha)):
#     for f in k_up:
#         sol = OnesidedCoupling(par0, t, keep, f, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]
#         amplitudes_up.append(compute_all_amplitude(par0, t, keep, f, mu, gamma,alpha[i], beta))


#     par0 = sol[-1]

#     for j in k_down:
#         sol = OnesidedCoupling(par0, t, keep, j, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]  
#         amplitudes_down.append(compute_all_amplitude(par0, t, keep, j, mu, gamma, alpha[i], beta))

#     for e,k in enumerate(k_up):
#         try:
#             plt.plot([k]*len(amplitudes_up[e]), amplitudes_up[e], "k.", markersize = 0.5)
#         except:
#             None

#     for j,w in enumerate(k_down):
#         try:
#             plt.plot([w]*len(amplitudes_down[j]), amplitudes_down[j],"r.", markersize = 0.5)

#         except:
#             None



#     plt.xlabel("k", fontsize = 14)
#     plt.ylabel("A$_{y}$ in cm", fontsize = 14)
#     plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

#     plt.xticks(np.linspace(round(min(k_up),2),round(max(k_up),2), 5), fontsize = 12)
#     # plt.title(label = "$\\mu$ = " + f"{mu:.2f}" + ", $\\gamma$ = " + f"{gamma:.2f}" + ", $\\alpha$ = " + f"{alpha[i]:.2f}" + ", $\\beta$ = " + f"{beta:.2f}", fontsize = 14)
    
#     # lines = [0.1,4.0, 5.0, 8.0]
#     # cmap = plt.get_cmap('viridis', len(lines))
#     # for g, z in enumerate(lines):
#     #     plt.axvline(x = z, color = cmap(g)) 
#     plt.yticks(fontsize = 12)
#     plt.savefig(path +"Bifurkation_ß03_y01_mu10" + "alpha02"+  ".png", dpi =  400, bbox_inches = "tight")
#     plt.show()

######## Multiple bifurcation

# beta_change = [0.001, 0.05, 0.1]
# fig, axs = plt.subplots(len(beta_change), constrained_layout=True)

# for b_index, b in enumerate(beta_change):
#     amplitudes_up = []
#     amplitudes_down = []
#     for i,_ in enumerate(alpha):
#         for f in k_up:
#             sol = OnesidedCoupling(par0, t, keep, f, mu, b, alpha[i], beta).duffvdpsolver()
#             par0 = sol[-1]
#             amplitudes_up.append(compute_all_amplitude(par0, t, keep, f, mu, b, alpha[i], beta))

#         for e,k in enumerate(k_up):
#             try:
#                 axs[b_index].plot([k]*len(amplitudes_up[e]), amplitudes_up[e], "k.", markersize = 0.5)
                
#             except:
#                 None

#     axs[b_index].set_title("$\\gamma$ = " + f"{b:.3f}")
    
# fig.supxlabel("k", fontsize = 14)
# fig.supylabel("A$_{y}$ in cm", fontsize = 14)
# plt.savefig(path +"bifurcation_mu_variation" + ".png", dpi =  400, bbox_inches = "tight")
# plt.show()



# [Bifurcation periodic peaks]__________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________________


# amplitudes_up = []
# amplitudes_down = []
# for i in range(len(alpha)):
#     for f in k_up:
#         sol = OnesidedCoupling(par0, t, keep, f, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]
#         amplitudes_up.append(compute_periodic_amplitude(par0, t, keep, f, mu, gamma,alpha[i], beta))


#     par0 = sol[-1]

#     for j in k_down:
#         sol = OnesidedCoupling(par0, t, keep, j, mu, gamma, alpha[i], beta).duffvdpsolver()
#         par0 = sol[-1]  
#         amplitudes_down.append(compute_periodic_amplitude(par0, t, keep, j, mu, gamma, alpha[i], beta))

#     for e,k in enumerate(k_up):
#         try:
#             plt.plot([k]*len(amplitudes_up[e]), amplitudes_up[e], "k.", markersize = 0.5)
#             print(amplitudes_up[e])
#         except:
#             None

#     for j,w in enumerate(k_down):
#         try:
#             plt.plot([w]*len(amplitudes_down[j]), amplitudes_down[j],"r.", markersize = 0.5)
#         except:
#             None



#     plt.xlabel("k", fontsize = 20)
#     plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
#     plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
#     plt.title(label = "$\\alpha$ = " + f"{alpha[i]:.4f}" + ", $\\omega$ = " + f"{np.sqrt(alpha[i]):.4f}", fontsize = 20)
#     plt.xticks(np.linspace(round(min(k_up),2),round(max(k_up),2), 5), fontsize = 20)
#     plt.title(label = "$\\alpha$ = " + f"{alpha[i]:.2f}" + ", $\\omega$ = " + f"{np.sqrt(alpha[i]):.2f}", fontsize = 20)

#     plt.yticks(fontsize = 20)
#     plt.savefig(path +"Bifurcation_periodic_" + "alpha1"+  ".png", dpi =  300, bbox_inches = "tight")
#     print(alpha[i])




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



# plt.xlabel("$\\omega _y$ in kHz", fontsize = 20)
# plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))

# plt.xticks(np.linspace(round(min(alpha_up),2),round(max(alpha_up),2), 5), fontsize = 20)
# plt.title(label = "k= " + f"{k:.2f}", fontsize = 20)

# plt.yticks(fontsize = 20)
# plt.savefig(path +"Bifurcation_biginterval_y01_k_konstant" +  ".png", dpi =  300, bbox_inches = "tight")
# plt.show()
