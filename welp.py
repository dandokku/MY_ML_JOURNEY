import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 40, 1000) #Start, finish, n points 
d_r = 2.5 * t
d_s = 3 * (t-5)

# Creating a subplot
fig, ax = plt.subplots()

# Setting plot title and axis labels
plt.title("Robber no sabi drive, na why them catch am")
plt.xlabel("Time (mins)")
plt.ylabel("Distance (km)")

# Setting x and y axis limits
ax.set_xlim([0, 40])
ax.set_ylim([0, 100])

# Plotting the distance of the robber and sheriff over time
ax.plot(t, d_r, c='green', label='robber')  # Robber's distance over time (green line)
ax.plot(t, d_s, c='blue', label='sheriff')  # Sheriff's distance over time (blue line)

# Adding vertical and horizontal dashed lines to indicate a specific event (e.g., capture)
plt.axvline(x=30, color='red', linestyle='--')  # Vertical dashed line at x=30
_ = plt.axhline(y=75, color='red', linestyle='--')  # Horizontal dashed line at y=75

# Adding a legend to the plot
plt.legend()

# Displaying the plot
plt.show()
