import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling


# [Parameters]________________________________________________________________________________________________________________________________________________


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
gamma = 0.1
mu = 2
beta = 0.2
alpha = 0.2
lilie = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta)

xsol = lilie.x_solv()
ysol = lilie.y_solv()
psol = lilie.p_solv()
qsol = lilie.q_solv()

#[van der Pol]________________________________________________________________________________________________________________________________________________

with open(str(Path.cwd()) + "/path.txt") as f:
  path = f.read()


plt.plot(xsol[:keep],psol[:keep])   # with transient

plt.xlabel("x in a.u.",fontsize = 20)
plt.ylabel("p in a.u.",fontsize = 20)
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.xticks(np.linspace(round(min(xsol),2),round(max(xsol),2), 5), fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig( path + "x_phaseplane" + ".png", dpi =  300, bbox_inches = "tight")
plt.show()

#[Duffing]________________________________________________________________________________________________________________________________________________

plt.plot(ysol[:keep],qsol[:keep])   # with transient
plt.xlabel("y in a.u.",fontsize = 20)
plt.ylabel("q in a.u.",fontsize = 20)
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
plt.xticks(np.linspace(round(min(ysol),2),round(max(ysol),2), 5), fontsize = 20)
plt.yticks(fontsize = 20)
plt.savefig(path +"y_phaseplane" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()