"""
Samjhana Sharma
"""
import numpy as np
import matplotlib.pyplot as plt

T = np.arange(0.01, 10, 0.1)  # Start from 0

Site_Class = {
    "A": {"<= 0.25": 0.8, "== 0.5": 0.8, "== 0.75": 0.8, "== 1": 0.8, ">= 1.25": 0.8},
    "B": {"<= 0.25": 1, "== 0.5": 1, "== 0.75": 1, "== 1": 1, ">= 1.25": 1},
    "C": {"<= 0.25": 1.2, "== 0.5": 1.2, "== 0.75": 1.1, "== 1": 1.0 ,">= 1.25": 1.0},
    "D": {"<= 0.25": 1.6, "== 0.5": 1.4, "== 0.75": 1.2, "== 1": 1.1, ">= 1.25": 1.0},
    "E": {"<= 0.25": 2.5, "== 0.5": 1.7, "== 0.75": 1.2, "== 1": 0.9, ">= 1.25": 0.9},
}

Site_Class_S1 = {
    "A": {"<= 0.1": 0.8, "== 0.2": 0.8, "== 0.3": 0.8, "== 0.4": 0.8, ">= 0.5": 0.8},
    "B": {"<= 0.1": 1.0, "== 0.2": 1.0, "== 0.3": 1.0, "== 0.4": 1.0, ">= 0.5": 1.0},
    "C": {"<= 0.1": 1.7, "== 0.2": 1.6, "== 0.3": 1.5, "== 0.4": 1.4, ">= 0.5": 1.3},
    "D": {"<= 0.1": 2.4, "== 0.2": 2.0, "== 0.3": 1.8, "== 0.4": 1.6, ">= 0.5": 1.5},
    "E": {"<= 0.1": 3.5, "== 0.2": 3.2, "== 0.3": 2.8, "== 0.4": 2.4, ">= 0.5": 2.4},
}

# Prompt user to input site class, Ss, and S1 values
site_class_input = input("Enter the Site_Class (A, B, C, D, or E): ")
Ss_input = float(input("Enter the value of Ss: "))
S1_input = float(input("Enter the value of S1: "))

# Define interpolation function to interpolate values based on conditions
def interpolate(value, conditions):
    for condition, val in conditions.items():
        if condition.startswith('<='):
            threshold = float(condition.split('<= ')[1])
            if value <= threshold:
                return val
        elif condition.startswith('<'):
            threshold = float(condition.split('< ')[1])
            if value < threshold:
                return val
        elif condition.startswith('=='):
            threshold = float(condition.split('== ')[1])
            if value == threshold:
                return val
        elif condition.startswith('>='):
            threshold = float(condition.split('>= ')[1])
            if value >= threshold:
                return val
    raise ValueError("Invalid input")

# Define function to interpolate Fa based on site class and Ss
def interpolate_Site_Class(site_class_input, value):
    if site_class_input in Site_Class:
        return interpolate(value, Site_Class[site_class_input])
    else:
        raise ValueError("Invalid Site_Class")
# Define function to interpolate Fv based on site class and S1
def interpolate_Site_Class_S1(site_class_input, value):
    if site_class_input in Site_Class_S1:
        return interpolate(value, Site_Class_S1[site_class_input])
    else:
        raise ValueError("Invalid Site_Class")
        
# Interpolate Fa and Fv based on user input
Fa = interpolate_Site_Class(site_class_input, Ss_input)
Fv = interpolate_Site_Class_S1(site_class_input, S1_input)

# Calculate spectral acceleration values (Sds and Sd1) and other parameters (Ta, Tb, Tl)
Sds = Ss_input * Fa
Sd1 = S1_input * Fv
Ta = 0.2 * Sd1 / Sds
Tb = Sd1 / Sds
Tl = 6

# Calculate the design response spectrum (Sae) for each period (Ti) based on specified conditions
Sae = []
for Ti in T:
    if Ti > 0 and Ti <= Ta:
        Saei = (0.4 + 0.6 * Ti / Ta) * Sds
    elif Ti > Ta and Ti <= Tb:
        Saei = Sds
    elif Ti > Tb and Ti <= Tl:
        Saei = Sd1 / Ti
    else:
        Saei = Sd1 * Tl / Ti ** 2
    Sae.append(Saei)

# Print interpolated Fa and Fv values
print("Fa:", Fa)
print("Fv:", Fv)

# Plot the design response spectrum using Matplotlib
plt.plot(T, Sae)
plt.xlim(0, 10)
plt.ylim(0, 1.5)
plt.xlabel('Period (sec)')
plt.ylabel('Spectral Response Acceleration, Sa(g)')
plt.title('Design Response Spectrum')
plt.grid(True)
plt.show()