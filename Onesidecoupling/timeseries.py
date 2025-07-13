import numpy as np
import matplotlib.pyplot as plt
from pathlib import Path

from mainscript import OnesidedCoupling


# [Parameters]________________________________________________________________________________________________________________________________________________

# with open(str(Path.cwd()) + "/path.txt") as f:
#   path = f.read()

# t_step = 0.01
# t_last = 100 # 50h -> 1 point represent 1h
# t = np.arange(0, 5000, t_step)
# keep = int(t_last / t_step)
# x = 1
# y = 1
# q = 1
# p = 1
# par = x,y,p,q
# k = 0
# gamma = 0.1
# mu = 2.0
# beta = 0.2
# alpha = 0.2
# lilie = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta)

# xsol = lilie.x_solv()
# ysol = lilie.y_solv()
# psol = lilie.p_solv()
# qsol = lilie.q_solv()


# # [Plots]________________________________________________________________________________________________________________________________________________
# """
# showing the timeseries only for the x and y solutions (x -> Van der Pol, y -> Duffing)
# """

# # [x-timeseries]

# plt.plot(t, xsol, label = f"k: {k:.2f}")
# plt.ylabel("x in a.u.", fontsize = 20)
# x_title = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
# # plt.legend(fontsize = 16, loc = "upper right")
# plt.xlabel("t in ms", fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim([-3, 3])
# plt.xlim([0,200])
# plt.savefig(path + "x_timeseries_mu2" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()

# # [y-timeseries]

# plt.plot(t, ysol, label = f"k: {k:.2f}")
# plt.ylabel("y in a.u.", fontsize = 20)
# y_title = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
# # plt.legend(fontsize = 16, loc = "upper left")
# plt.xlabel("t in ms", fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim([-3, 3])
# plt.xlim([0,200])
# plt.savefig(path + "y_timeseries_k0_ß02" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()



# [Calculating Frequency, Period, stable Amplitude]________________________________________________________________________________________________________________________________________________

# app = 3

# # [van der Pol]

# period_vdp = lilie.period(10)[0]
# f_vdp = 1/period_vdp
# w_vdp = 2 * np.pi * f_vdp
# amp_vdp = np.mean(lilie.find_peaks_max()[0][1]['peak_heights'])
# time_amp_vdp = [t[i] for i in lilie.find_peaks_max()[0][0][-10:]]

# print("Period van der Pol: ", round(period_vdp, app))
# print("frequency van der Pol: ", round(f_vdp, app))
# print("angular frequency van der Pol: ", round(w_vdp, app))
# print("amplitude van der Pol: ", round(amp_vdp, app))
# # print("time van der Pol: ", time_amp_vdp)
# print(" ")

# # [Duffing]

# period_duff = lilie.period(10)[1]
# f_duff = 1/period_duff
# w_duff = 2 * np.pi * f_duff
# amp_duff = np.mean(lilie.find_peaks_max()[1][1]['peak_heights'])
# time_amp_duff = [t[i] for i in lilie.find_peaks_max()[1][0][-10:]]

# print("Period Duffing: ", round(period_duff, app))
# print("frequency Duffing: ", round(f_duff, app))
# print("angular Duffing: ", round(w_duff, app))
# print("amplitude Duffing: ", round(amp_duff, app))
# # print("time Duffing: ", time_amp_duff)


# [multiple plots Duffing]_______________________________________________________________________________________________________________________________________________________________________________________________________

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
k_up = [0.1, 2.5, 3, 4, 5, 8]
gamma = 0.1
mu = 2.0
beta = 0.3
alpha = 0.2

app = 3

for index, k in enumerate(k_up):

  y_mul_sol = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).y_solv()

  period = OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).period(10)[1]
  f = 1/period
  w = 2 * np.pi * f
  amp = np.mean(OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][1]['peak_heights'])
  time_amp = [t[i] for i in OnesidedCoupling(par, t, keep, k, mu, gamma, alpha, beta).find_peaks_max()[1][0][-10:]]

  print(str(k))
  print("Period Duffing: ", round(period, app))
  print("frequency Duffing: ", round(f, app))
  print("angular frequency Duffing: ", round(w, app))
  print("amplitude Duffing: ", round(amp, app))
  print(" ")

#   plt.plot(t, y_mul_sol, label = f"ß: {b:.2f}")
# plt.ylabel("y in a.u.", fontsize = 20)
# # y_title = "$\gamma$ = " + f"{gamma:.2f}, ß = " + f"{beta:.2f}, $\\alpha$ = " + f"{alpha:.2f}, $\mu$ = " + f"{mu:.2f}, x$_0$ = " + f"{par[0]:.2f}, y$_0$ = "+ f"{par[1]:.2f}, p$_0$ = "+ f"{par[2]:.2f}, q$_0$ = "+ f"{par[3]:.2f}"
# plt.legend(fontsize = 16, loc = "upper right")
# plt.xlabel("t in ms", fontsize = 20)
# plt.xticks(fontsize = 20)
# plt.yticks(fontsize = 20)
# plt.ylim([-3, 3])
# plt.xlim([0,150])
# plt.savefig(path + "y_timeseries_k01_ßhigh" + ".png", dpi =  300, bbox_inches = "tight")
# plt.show()





# [multiple plots Van der Pol]_______________________________________________________________________________________________________________________________________________________________________________________________________

# with open(str(Path.cwd()) + "/path.txt") as f:
#   path = f.read()

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
# mu = [0.5,1.0,2.0,3.0,5.0,10.0,20.0]
# beta = 0.3
# alpha = 0.2

# app = 3

# for index, m in enumerate(mu):

#   x_mul_sol = OnesidedCoupling(par, t, keep, k, m, gamma, alpha, beta).x_solv()

#   period_vdp = OnesidedCoupling(par, t, keep, k, m, gamma, alpha, beta).period(10)[0]
#   f_vdp = 1/period_vdp
#   w_vdp = 2 * np.pi * f_vdp
#   amp_vdp = np.mean(OnesidedCoupling(par, t, keep, k, m, gamma, alpha, beta).find_peaks_max()[0][1]['peak_heights'])
#   time_amp = [t[i] for i in OnesidedCoupling(par, t, keep, k, m, gamma, alpha, beta).find_peaks_max()[0][0][-10:]]

#   print("Period vdp: ", round(period_vdp, app))
#   print("frequency vdp: ", round(f_vdp, app))
#   print("angular frequency vdp: ", round(w_vdp, app))
#   print("amplitude vdp: ", round(amp_vdp, app))
#   print(" ")