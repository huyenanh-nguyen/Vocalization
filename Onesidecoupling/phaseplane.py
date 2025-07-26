import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling


# [Parameters]________________________________________________________________________________________________________________________________________________


# t_step = 0.01
# t_last = 100 # 50h -> 1 point represent 1h
# t = np.arange(0, 5000, t_step)
# keep = int(t_last / t_step)
# x = 1
# y = 1
# q = 1
# p = 1
# par = x,y,p,q
# k = 0.1
# gamma = 0.1
# mu = 2.0
# beta = 0.5
# alpha = 0.2
# lilie = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta)

# xsol = lilie.x_solv()
# ysol = lilie.y_solv()
# psol = lilie.p_solv()
# qsol = lilie.q_solv()

# #[van der Pol]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()


# plt.plot(xsol[:keep],psol[:keep])   # with transient

# plt.xlabel("x in a.u.",fontsize = 20)
# plt.ylabel("p in a.u.",fontsize = 20)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# plt.xticks(np.linspace(round(min(xsol),2),round(max(xsol),2), 5), fontsize = 20)
# plt.yticks(np.linspace(round(min(psol),2),round(max(psol),2), 5),fontsize = 20)
# plt.savefig( path + "x_phaseplane" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()

#[Duffing]________________________________________________________________________________________________________________________________________________

# plt.plot(ysol[-keep:],qsol[-keep:])   # with transient
# plt.xlabel("y in a.u.",fontsize = 20)
# plt.ylabel("q in a.u.",fontsize = 20)
# plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.1f'))
# plt.xticks(np.linspace(round(min(ysol),2),round(max(ysol),2), 5), fontsize = 20)
# plt.yticks(np.linspace(round(min(qsol),2),round(max(qsol),2), 5), fontsize = 20)
# plt.savefig(path +"y_phaseplane_withouttransient" + ".png", dpi =  300, bbox_inches = "tight")
# # plt.show()

# multiple Duffing

t_step = 0.01
t_last = 100 # 50h -> 1 point represent 1h
t = np.arange(0, 500, t_step)
keep = int(t_last / t_step)
x = 1
y = 1
q = 1
p = 1
par = x,y,p,q
k = [1.3, 1.5, 8.0]
gamma = 0.1
mu = 10.0
beta = 0.3
alpha = 0.2




fig, axs = plt.subplots(1, 3, figsize=(12, 4))

for index, h in enumerate(k):
  y_sol = OnesidedCoupling(par, t, keep, h, mu, gamma, alpha, beta).y_solv()[-keep:]
  q_sol = OnesidedCoupling(par, t, keep, h, mu, gamma, alpha, beta).q_solv()[-keep:]
  axs[index].plot(y_sol, q_sol)
  axs[index].set_title(f"k = {k[index]:.2f}", fontsize=20)
  axs[index].set_xlabel('y in cm', fontsize=22)
  axs[index].set_ylabel('q in cm', fontsize=22)
  axs[index].tick_params( axis='both', labelsize=20)
  axs[index].set_xticks(np.linspace(-5,5,3))

plt.tight_layout()
plt.savefig(path +"mulitplephaseplane_mu10" + ".png", dpi =  300, bbox_inches = "tight")
plt.show()
