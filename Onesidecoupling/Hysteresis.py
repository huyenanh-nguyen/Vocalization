import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches

# [Parameters]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()

t_step = 0.01
t_last = 100 # 50h -> 1 point represent 1h
t = np.arange(0, 5000, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
k = 0.1
gamma = 0.2
mu = 0.2
beta = 1
alpha_up = np.arange(0, 3, 0.01)
alpha_down = alpha_up[::-1]

# [Functions]____________________________________________________________________________________________________________________

def compute_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'][-10:])
    return amp



# [Hysteresis]___________________________________________________________________________________________________________________

# par0 = 1,1,1,1
# amplitudes_up = []
# amplitudes_down = []

# for f in alpha_up:
#     sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, f, beta).duffvdpsolver()
#     par0 = sol[-1]
#     print(par0)
#     amplitudes_up.append(compute_amplitude(par0, t, keep, k, mu, gamma, f, beta))


# par0 = sol[-1]
# for j in alpha_down:
#     sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, j, beta).duffvdpsolver()
#     par0 = sol[-1]  
#     print(par0)
#     amplitudes_down.append(compute_amplitude(par0, t, keep, k, mu, gamma, j, beta))


# plt.plot(np.sqrt(alpha_up), amplitudes_up, label="Increasing ω", color = "#431F6A")
# plt.plot(np.sqrt(alpha_down), amplitudes_down, label="Decreasing ω", color = "#88C960")
# plt.xlabel("$\omega _y$ in Hz", fontsize = 20)
# plt.ylabel("A$_{y}$ in a.u.", fontsize = 20)
# plt.axvline(x = np.sqrt(0.3), color = "r")
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
# plt.xticks(np.linspace(min(np.sqrt(alpha_up)),max(np.sqrt(alpha_up)),5), fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.legend(fontsize = 16)
# plt.savefig( path + "Hysteresis_k01_vline" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()

# [Basin of Attractor]___________________________________________________________________________________________________________________

alpha = [0.3]


colours = ["#283D3B", "#F8D794"]

cmap = ListedColormap(colours)
for i in range(len(alpha)):
    x_par = 1
    y_par = np.arange(-3,3,0.1)
    p_par = 1
    q_par = np.arange(-3,3, 0.1)
  

    q,y = np.meshgrid(q_par,y_par)
    attractor = np.zeros_like(y)
    y_amplitude_matrix = np.zeros_like(y)

    for l in range(len(q_par)):
        for m in range(len(y_par)):

            par0 = [x_par, y_par[m], p_par, q_par[l]]
            y_amplitude = compute_amplitude(par0, t, keep, k, mu, gamma, alpha[i], beta)
            y_amplitude_matrix[l,m] = round(y_amplitude, 2)
    
    print(y_amplitude_matrix)
    
    plt.imshow(y_amplitude_matrix, extent=[-3,3,-3,3], cmap = cmap, origin='lower')
    plt.xlabel("y in a.u.",fontsize = 25)
    plt.ylabel("q in a.u.",fontsize = 25)
    plt.title(label = "$\\alpha$ = " + f"{alpha[i]:.4f}" + ", $\\omega$ = " + f"{np.sqrt(alpha[i]):.4f}", fontsize = 20)
    plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
    plt.xticks( np.linspace(-3,3, 5), fontsize = 18)
    plt.yticks(np.linspace(-3,3, 5),fontsize = 18)
    
    labels = ["$\overline{A}_{10}$ =" + f"{np.nanmin(y_amplitude_matrix):.2f}", "$\overline{A}_{10}$ =" + f"{np.nanmax(y_amplitude_matrix):.2f}"]
    patches = [mpatches.Patch(color=colours[i], label=labels[i]) for i in range(len(colours))]
    plt.legend(handles=patches, loc='upper right', fontsize = 14)
    
    plt.savefig(path + "Basin" + ".png", dpi =  300, bbox_inches = "tight")
            