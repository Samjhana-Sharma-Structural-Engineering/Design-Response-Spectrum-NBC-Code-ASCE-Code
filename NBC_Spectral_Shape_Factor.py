""" Samjhana Sharma
"""
import numpy as np
import matplotlib.pyplot as plt
# Dictionary defining soil types and their parameters  
Soil_Type = {
    "A": {"Ta": 0.1, "Tc": 0.5, "alpha": 2.5, "k": 1.8}, # Soil Type A parameters
    "B": {"Ta": 0.1, "Tc": 0.7, "alpha": 2.5, "k": 1.8}, # Soil Type B parameters
    "C": {"Ta": 0.1, "Tc": 1.0, "alpha": 2.5, "k": 1.8}, # Soil Type C parameters
    "D": {"Ta": 0.5, "Tc": 2.0, "alpha": 2.25, "k": 0.8}, # Soil Type D parameters
}

# Creating an array of time periods from 0 to 6 seconds with a step size of 0.1 seconds
T = np.arange(0, 6.1, 0.1)  # Start from 0
plt.figure(figsize=(10, 6))  # Set figure size

# Looping through each soil type and its parameters to plot the response spectrum
for soil_type, params in Soil_Type.items():
    Ta = params["Ta"] # Assignment of Ta value for the current soil type
    Tc = params["Tc"] # Assignment of Tc value for the current soil type
    alpha = params["alpha"] # Assignment of alpha value for the current soil type
    k = params["k"] # Assignment of k value for the current soil type
    
    Ch_t = [1]  # Start with Ch_t = 1 for t=0
    
    # Looping through each period value in T array
    for Ti in T[1:]:  # Start from index 1 to avoid modifying the initial value at index 0
        # Calculating Ch(T) based on different conditions
        if Ti < Ta:
            Ch = (1 + (alpha - 1) * (Ti / Ta)) # Ch formula for Ti < Ta
        elif Ta <= Ti < Tc:
            Ch = alpha # Ch formula for Ta <= Ti < Tc
        elif Tc <= Ti <= 6:
            Ch = alpha * (k + (1 - k) * (Tc / Ti)**2) * (Tc / Ti)**2
        else:
            Ch = 0  # Default value if none of the conditions are satisfied
        Ch_t.append(Ch) # Appending calculated Ch value to Ch_t list
   
    # Plotting the response spectrum for the current soil type
    plt.plot(T, Ch_t, label=f"Soil Type {soil_type}")
plt.xlim(0,6)
plt.ylim(0,3)
plt.xlabel('Period (sec)')
plt.ylabel('Spectral Shape Factor Ch(T))')
plt.title('Response Spectrum for Different Soil Types')
plt.grid(True)
plt.legend()
plt.show()
