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
    Computes the amplitude of the y-values in a Duffing oscillator time series.

    This function calculates the mean amplitude of the last 10 highest peaks 
    in the simulated Duffing oscillator's y-component over a given timespan.

    Args:
        par (tuple): Initial values for (x, y, p, q).
        t (list or np.ndarray): Time span of the simulation.
        keep (float): Fraction of the total time points to analyze.
        k (float): Coupling strength.
        mu (float): Nonlinear damping constant.
        gamma (float): Linear damping constant.
        alpha (float): Linear restoring force coefficient.
        beta (float): Nonlinear restoring force coefficient.

    Returns:
        np.ndarray or float: Mean amplitude of the last 10 highest peaks of the time series.
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
        """
        Checks whether the system undergoes hysteresis.

        This function tests if the system exhibits hysteresis behavior when the parameter 
        `alpha` changes. For each new value of `alpha`, the final state from the previous 
        iteration is used as the initial condition for the next one.

        Note:
            The values of `alpha` are converted to `np.sqrt(alpha)` for plotting.

        Args:
            alpha_up (list or np.ndarray): Sequence of alpha values to test.
            vertikaline (bool): If True, plots a vertical line for a specific alpha value.
            where_vertikalline (float): The alpha value (before taking the square root) 
                where the vertical line is drawn, e.g., 0.4 → line at `np.sqrt(0.4)`.
            verticalcolor (str): Color of the vertical line. Can be a named color 
                (e.g., 'red', 'blue') or any Matplotlib-compatible color code.
            filename (str): Name of the output plot file.

        Returns:
        matplotlib.figure.Figure: The generated hysteresis plot.
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