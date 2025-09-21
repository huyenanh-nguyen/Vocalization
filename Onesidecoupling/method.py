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
    

    def metadata_from_timeseries(self, variable : str, rounding : int):
        """
        Printing out the period, frequency, angular frequency and the mean of the last 10 peaks as Amplitude.
        its empiric measured.

        Args:
            variable (str): "x", "y", "p" or "q" 
            rounding (int): digit to round, if rounding is 3, the value will get rounded 3 digit

        Returns:
            Metadata: print out the Period, frequency, angular frequency and the mean of the last 10 Amplitudes of the timeseries
        """
        par = self.par
        t = self.t
        k = self.k
        keep = self.t_keep
        gamma = self.gamma
        alpha = self.alpha
        mu = self.mu
        beta = self.beta

        if variable == "x":
            x_period = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).period(10)[0]
            x_amp_vdp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[0][1]['peak_heights'])
            print("x Period van der Pol: ", round(x_period, rounding))
            print("x Frequency van der Pol: ", round(1/x_period, rounding))
            print("x Angular frequency van der Pol: ", round(2 * np.pi * (1/x_period), rounding))
            print("x Amplitude van der Pol: ", round(x_amp_vdp, rounding))


        elif variable == "y":
            y_period = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).period(10)[1]
            y_amp_vdp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'])
            print("y Period Duffing: ", round(y_period, rounding))
            print("y Frequency Duffing: ", round(1/y_period, rounding))
            print("y Angular frequency Duffing: ", round(2 * np.pi * (1/y_period), rounding))
            print("y Amplitude Duffing: ", round(y_amp_vdp, rounding))

        elif variable == "p":
            p_period = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).period(10)[2]
            p_amp_vdp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[2][1]['peak_heights'])
            print("p Period van der Pol: ", round(p_period, rounding))
            print("p Frequency van der Pol: ", round(1/p_period, rounding))
            print("p Angular frequency van der Pol: ", round(2 * np.pi * (1/p_period), rounding))
            print("p Amplitude van der Pol: ", round(p_amp_vdp, rounding))
 
        elif variable == "q":
            q_period = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).period(10)[3]
            q_amp_vdp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[3][1]['peak_heights'])
            print("q Period Duffing: ", round(q_period, rounding))
            print("q Frequency Duffing: ", round(1/q_period, rounding))
            print("q Angular frequency Duffing: ", round(2 * np.pi * (1/q_period), rounding))
            print("q Amplitude Duffing: ", round(q_amp_vdp, rounding))

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

print(hm.metadata_from_timeseries("y", 3))
