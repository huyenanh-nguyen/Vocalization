import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path
from matplotlib.ticker import FormatStrFormatter
from mainscript import OnesidedCoupling
import math

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
par0 = x,y,p,q
k_up = np.arange(0.01,2.5, 0.01)
k_down = k_up[::-1]

gamma = 0.2
mu = 0.2
beta = 1
alpha = np.arange(0.01, 3, 0.1)

# [Functions]____________________________________________________________________________________________________________________

def compute_amplitude(par, t, keep, k, mu, gamma, alpha, beta):
    amp = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).peak()[1][1]['peak_heights'][-10:]

    return amp

def approx(listofnum, tol):
     mean = np.mean(listofnum)
     boolean = [abs(i - mean) / mean * 100 for i in listofnum]
     
     for num in boolean:
          if num > tol:
               return math.nan
          else:
               return mean
          

par0 = 1,1.4,1.4,1

y,q = np.meshgrid(k_up, alpha)
up = np.zeros_like(y)
down = np.zeros_like(y)

index = []
for l in range(len(alpha)):
        for m in range(len(k_up)):
            sol = OnesidedCoupling(par0, t, keep, k_up[m], mu, gamma, alpha[l], beta).duffvdpsolver()
            par0 = sol[-1]
            amp = approx(compute_amplitude(par0, t, keep, k_up[m], mu, gamma, alpha[l], beta), 0.1)
            print(amp)
            try:
                if math.isnan(amp) == True:
                    index.append(("alpha: ", alpha[l],"k: ",k_up[m]))
            except:
                print(amp)
                index.append(("alpha: ", alpha[l],"k: ",k_up[m]))
            up[l,m] = amp
    
plt.figure(figsize= (10,10))
plt.imshow(up, extent=[min(k_up),max(k_up),min(alpha),max(alpha)], cmap = "viridis", origin='lower')
plt.xlabel("k in a.u.",fontsize = 25)
plt.ylabel("$\\omega _y$ in Hz",fontsize = 25)
plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.3f'))
plt.xticks( np.linspace(round(min(k_up),2),round(max(k_up),2), 3), fontsize = 18)
plt.yticks(np.linspace(min(alpha),max(alpha), 5),fontsize = 18)
plt.colorbar().ax.set_ylabel('A$_y$ in a.u.', fontsize = 20)

plt.savefig(path + "omegaagainstk_highk" + ".png", dpi =  300, bbox_inches = "tight")

print(index)   

