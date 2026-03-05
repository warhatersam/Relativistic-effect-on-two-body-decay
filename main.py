# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import matplotlib.pyplot as plt
import numpy as np


# units in the entire calculations are natural units, mass and energy have the same unit
c = 1
# set up masses and energy of the two body decay
# example:pion decaying into muon and muon neutrino
m1 = 105.66
m2 = 10**-6
Q = 33.9




v = np.linspace(0, 2.9*10**8)
Escale_1 = np.linspace(10**-9, 10**5 * m1, 999999)
logEscale_1 = np.log10(Escale_1)
Escale_2 = np.linspace(10**-9, 10**5 * m1, 999999)
logEscale_2 = np.log10(Escale_2)

def relativity_gamma(v):

    return 1/(np.sqrt(1-(v**2/c**2)))

def energy(m, v):

    return relativity_gamma(v) * m * c**2

def velocity(m, E):
    return np.sqrt(c**2 * (1 - (m*c**2 / E)**2))  # clip negatives to 0

def energy_distribution_after_decay(m1, m2, Q):
    M = m1 + m2 + Q
    E1 = (M**2+m1**2-m2**2)/(2*M)
    E2 = (M**2+m2**2-m1**2)/(2*M)
    return E1, E2

E1, E2 = energy_distribution_after_decay(m1, m2, Q)

logE1, logE2 = np.log10([E1, E2])
v1 = velocity(m1, E1)
v2 = velocity(m2, E2)

print(f"E1 is {E1}, E2 is {E2}")
print(f"v1 is {v1}, v2 is {v2}")

# plt.plot(v, relativity_gamma(v))
# plt.plot(v, energy(1, v))
plt.plot(logEscale_1, velocity(m1, Escale_1))
plt.plot(logEscale_2, velocity(m2, Escale_2))

plt.scatter(logE1, v1)
plt.annotate(
    "m1",
    (logE1, v1),
    textcoords="offset points",
    xytext=(0, 0),
    ha="left"
)
plt.scatter(logE2, v2)
plt.annotate(
    "m2",
    (logE2, v2),
    textcoords="offset points",
    xytext=(0, 0),
    ha="left"
)
plt.xlabel("logE")
plt.ylabel("velocity(c^-1)")
plt.title("Velocity after decay")
plt.show()




# See PyCharm help at https://www.jetbrains.com/help/pycharm/
