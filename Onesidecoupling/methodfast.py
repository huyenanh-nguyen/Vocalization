from .mainscript import OnesidedCoupling
import numpy as np
from pathlib import Path
from scipy.integrate import odeint
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

class Fastplots(OnesidedCoupling):
    """
    The runtime for those plots are approximatetly 10 seconds (depending on the time intervals t).
    Timeseries and phase plane have a short runtime.
    Also with this class we can get the metadata like period, frequency, angular frequency and Amplitude of the timeseries.
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
        Plots the time series of a chosen variable (x, y, p, or q).

        The variables `x` and `p` correspond to the Van der Pol oscillator,
        while `y` and `q` correspond to the Duffing oscillator. This function
        plots the specified variable over time and optionally saves the plot
        to the given path.

        Args:
            variable (str): The variable to plot — one of 'x', 'y', 'p', or 'q'.
            filename (str): Name of the file to save the plot as.
            xintervall (list or None): Range of x-axis values to display, e.g., [0, 400]. 
                If None, the full range is plotted.
            yintervall (list or None): Range of y-axis values to display, e.g., [-4, 4]. 
                If None, the full range is plotted.
            title (bool): If True, displays the variable name as the plot title. 
                If False, no title is shown.

        Returns:
            matplotlib.figure.Figure: The generated plot.

        Example:
            >>> t_step = 0.01
            >>> t_last = 100  # 50h -> 1 point represents 1h
            >>> t = np.arange(0, 5000, t_step)
            >>> keep = int(t_last / t_step)
            >>> par = (1, 1, 1, 1)
            >>> k = 1.3
            >>> gamma = 0.1
            >>> mu = 2
            >>> beta = 0.3
            >>> alpha = 0.2
            >>> hm = Fastplots(par, t, keep, k, mu, gamma, alpha, beta, path)
            >>> hm.timeseries_singleplot("x", "test", [0, 400], None, False)
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
        Prints the period, frequency, angular frequency, and mean amplitude of the last 10 peaks.

        The values are empirically measured from the given time series data.

        Args:
            variable (str): The variable to analyze — one of 'x', 'y', 'p', or 'q'.
            rounding (int): Number of decimal places to round the results to.
                For example, if `rounding=3`, values are rounded to three digits.

        Returns:
            None: Prints the period, frequency, angular frequency, and mean amplitude
            of the last 10 peaks of the time series to the console.
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
    

    def phaseplane(self, variable, filename : str):
        keep = self.t_keep
        xsol = self.x_solv()[:keep]
        ysol = self.y_solv()[:keep]
        psol = self.p_solv()[:keep]
        qsol = self.q_solv()[:keep]

        if variable == "x":
            plt.plot(xsol,psol)
            plt.xlabel("x in a.u.",fontsize = 20)
            plt.ylabel("p in a.u.",fontsize = 20)
            plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            plt.xticks(np.linspace(round(min(xsol),2),round(max(xsol),2), 5), fontsize = 20)
            plt.yticks(np.linspace(round(min(psol),2),round(max(psol),2), 5),fontsize = 20)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()

        elif variable == "y":
            plt.plot(ysol,qsol)
            plt.xlabel("y in a.u.",fontsize = 20)
            plt.ylabel("q in a.u.",fontsize = 20)
            plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.1f'))
            plt.gca().yaxis.set_major_formatter(FormatStrFormatter('%.2f'))
            plt.xticks(np.linspace(round(min(ysol),2),round(max(ysol),2), 5), fontsize = 20)
            plt.yticks(np.linspace(round(min(qsol),2),round(max(qsol),2), 5),fontsize = 20)
            plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
            plt.show()
            
        return None
    





# [Example]_________________________________________________


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

print(hm.phaseplane("y", "test"))
