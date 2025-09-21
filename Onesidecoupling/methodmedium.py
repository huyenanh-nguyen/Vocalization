from mainscript import OnesidedCoupling
import numpy as np
from pathlib import Path
from scipy.integrate import odeint
from scipy.signal import find_peaks
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter

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