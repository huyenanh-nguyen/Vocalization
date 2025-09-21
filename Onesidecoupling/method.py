from mainscript import OnesidedCoupling
import numpy as np
from pathlib import Path
from scipy.integrate import odeint
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt


class Fastplots(OnesidedCoupling):
    """
    The runtime for those plots are approximatetly 10 seconds (depending on the time intervals t).
    Timeseries and phase plane having a short runtime.
    """

    def __init__(self, par, t, keep, k, mu, gamma, alpha, beta, path):
        """
        Args:
            path (str): where to save the plots
        """
        self.par = par
        self.t = t
        self.t_keep = keep
        self.k = k
        self.mu = mu
        self.gamma = gamma
        self.alpha = alpha
        self.beta = beta
        self.path = path
        # super().__init__(par, self.t, self.t_keep, self. k,self. mu, self. gamma, self. alpha, self.beta)

    def timeseries_singleplot(self, variable : str, filename : str, xintervall : list, yintervall : list, title : bool):
        """
        Plotting the timeseries of the choosen variable x,y,p and q.
        x and p are the variables for the van der Pol ODE and y and q are for the Duffing ODE

        Args:
            variable (str): either x, y, p or q
            filename (str): name of the plot to save to path
            xintervall (list): x intervall to plot -> example [0,400] from 0 to 400, can also be None
            yintervall (list): y intervall to plot -> example [-4,4] height from -3 to 3, can also be None
            title (bool): True or False, if True, the variables will printed out as title. If False, then nothing will be displayed as title

        Returns:
            Plot: Show plot and save the plot in the path with the filename as name
        
        Example:
            t_step = 0.01\n
            t_last = 100 # 50h -> 1 point represent 1h\n
            t = np.arange(0, 5000, t_step)\n
            keep = int(t_last / t_step)\n
            x = 1\n
            y = 1\n
            q = 1\n
            p = 1\n
            par = x,y,p,q\n
            k = 1.3\n
            gamma = 0.1\n
            mu = 2\n
            beta = 0.3\n
            alpha = 0.2\n
            hm = Fastplots(par, t, keep, k, mu, gamma, alpha, beta, path)\n
            hm.timeseries_singleplot("x", "test", [0, 400], None, False)
        """
        par = self.par
        t = self.t
        k = self.k
        keep = self.t_keep
        gamma = self.gamma
        alpha = self.alpha
        mu = self.mu
        beta = self.beta
        xsol = self.x_solv()
        ysol = self.y_solv()
        psol = self.p_solv()
        qsol = self.q_solv()

        if variable == "x":
            plt.plot(t, xsol, label = f"k: {k: .2f}")
            plt.ylabel("x in a.u.", fontsize = 20)
            if title == True:
                headtitle = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
                plt.title(headtitle , fontsize = 20)
            else:
                None
            plt.xlabel("t in ms", fontsize = 20)
            plt.xticks(fontsize = 20)
            plt.xlim(xintervall)
            plt.yticks(fontsize = 20)
            plt.ylim(yintervall)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()

        elif variable == "y":
            plt.plot(t, ysol, label = f"k: {k: .2f}")
            plt.ylabel("y in a.u.", fontsize = 20)
            if title == True:
                headtitle = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
                plt.title(headtitle , fontsize = 20)
            else:
                None
            plt.xlabel("t in ms", fontsize = 20)
            plt.xticks(fontsize = 20)
            plt.xlim(xintervall)
            plt.yticks(fontsize = 20)
            plt.ylim(yintervall)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()

        elif variable == "p":
            plt.plot(t, psol, label = f"k: {k: .2f}")
            plt.ylabel("p in a.u.", fontsize = 20)
            if title == True:
                headtitle = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
                plt.title(headtitle , fontsize = 20)
            else:
                None
            plt.xlabel("t in ms", fontsize = 20)
            plt.xticks(fontsize = 20)
            plt.xlim(xintervall)
            plt.yticks(fontsize = 20)
            plt.ylim(yintervall)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()
        
        elif variable == "q":
            plt.plot(t, qsol, label = f"k: {k: .2f}")
            plt.ylabel("p in a.u.", fontsize = 20)
            if title == True:
                headtitle = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
                plt.title(headtitle , fontsize = 20)
            else:
                None
            plt.xlabel("t in ms", fontsize = 20)
            plt.xticks(fontsize = 20)
            plt.xlim(xintervall)
            plt.yticks(fontsize = 20)
            plt.ylim(yintervall)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()
        
        return None



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
k = 1.3
gamma = 0.1
mu = 2
beta = 0.3
alpha = 0.2

hm = Fastplots(par, t, keep, k, mu, gamma, alpha, beta, path)

print(hm.timeseries_singleplot("p", "test", [0, 400], None, False))
