from mainscript import OnesidedCoupling
import numpy as np
from pathlib import Path
from scipy.integrate import odeint
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

def compute_amplitude(par : tuple, t : float, keep : float, k : float, mu : float, gamma : float, alpha : float, beta : float):
    """
    computing the amplitude of the y value (Duffing time series)

    Args:
        par (tuple): initial value for x, y, p, q
        t (List): Timespan
        keep (float) : how many timepoints to look at
        k (float): coupling strenght
        mu (float): non-linear damping constant
        gamma (float): damping constant
        alpha (float): linear restoring force
        beta (float): non linear restoring force

    Returns:
       array: mean Amplitude of the last 10 highest Peak of the time series
    """
    amp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'][-10:])
    return amp


class Mediumplots(OnesidedCoupling):
    """
    The runtime for those plots will take a bit.
    the runtime for resonance, Hysteresis and bifurcation plots are at least 3 minutes.
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


    
    def hysteresis_plot(self, alpha_up : list, vertikaline : bool, where_vertikalline : float, verticalcolor : str, filename : str):
        """_summary_

        Args:
            alpha_up (list): _description_
            vertikaline (bool): _description_
            where_vertikalline (float): _description_
            verticalcolor (str): _description_
            filename (str): _description_

        Returns:
            _type_: _description_
        """
        alpha_down = alpha_up[::-1]
        amplitudes_up = []
        amplitudes_down = []

        t = self.t
        k = self.k
        keep = self.t_keep
        gamma = self.gamma
        mu = self.mu
        beta = self.beta

        for f in alpha_up:
            sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, f, beta).duffvdpsolver()
            par0 = sol[-1]
            print(par0)
            amplitudes_up.append(compute_amplitude(par0, t, keep, k, mu, gamma, f, beta))

        par0 = sol[-1]
        for j in alpha_down:
            sol = OnesidedCoupling(par0, t, keep, k, mu, gamma, j, beta).duffvdpsolver()
            par0 = sol[-1]  
            print(par0)
            amplitudes_down.append(compute_amplitude(par0, t, keep, k, mu, gamma, j, beta))

        cmap = plt.get_cmap('viridis', 2)
        plt.plot(np.sqrt(alpha_up), amplitudes_up, label="Increasing ω$_y$",  color = "#431F6A")
        plt.plot(np.sqrt(alpha_down), amplitudes_down, label="Decreasing ω$_y$", color = "#88C960")
        plt.xlabel("$\omega _y$ in kHz", fontsize = 14)
        plt.ylabel("A$_{y, max}$ in cm", fontsize = 14)

        if vertikaline == True:
            plt.axvline(x = np.sqrt(where_vertikalline), color = verticalcolor)
        else:
            pass

        plt.gca().xaxis.set_major_formatter(FormatStrFormatter('%.2f'))
        plt.xticks(np.linspace(min(np.sqrt(alpha_up)),max(np.sqrt(alpha_up)),5), fontsize = 12)
        plt.yticks(fontsize = 12)
        plt.legend(fontsize = 14)
        plt.savefig(self.path + filename + ".png", dpi =  300, bbox_inches = "tight")
        plt.show()

        return None