# Import necessary libraries
import matplotlib.pyplot as plt
import numpy as np
from math import pi

# Define data for the Kiviat chart
# Countries
countries = ['India', 'Japan', 'South Korea', 'USA']

# Factors for internet diffusion (e.g., broadband access, mobile penetration, internet speed, affordability, digital literacy)
factors = ['Broadband Access', 'Mobile Penetration', 'Internet Speed', 'Affordability', 'Digital Literacy']

# Data for each country based on the factors (normalised between 0 and 1)
data = {
    'India': [0.6, 0.7, 0.5, 0.8, 0.6],
    'Japan': [0.9, 0.8, 0.9, 0.7, 0.9],
    'South Korea': [0.95, 0.9, 1.0, 0.85, 0.95],
    'USA': [0.8, 0.85, 0.9, 0.75, 0.85]
}

# Number of variables (factors)
 
num_vars = len(factors)

# Compute angle for each axis

angles = [n / float(num_vars) * 2 * pi for n in range(num_vars)]

angles += angles[:1]  # Complete the loop to close the radar

# Initialize the radar chart

fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

# Plot each country's data on the radar chart
for country, values in data.items():

    values += values[:1]  # Complete the loop to close the radar

    ax.plot(angles, values, linewidth=2, linestyle='solid', label=country)

    ax.fill(angles, values, alpha=0.25)

# Add labels for each factor

ax.set_xticks(angles[:-1])

ax.set_xticklabels(factors)

# Set the range of the radar chart

ax.set_rlabel_position(30)

plt.yticks([0.2, 0.4, 0.6, 0.8], ["0.2", "0.4", "0.6", "0.8"], color="grey", size=7)

plt.ylim(0, 1)

# Add title and legend
plt.title('Internet Diffusion Comparison: India, Japan, South Korea, USA', size=15, color='blue', y=1.1)

plt.legend(loc='upper right', bbox_to_anchor=(0.1, 0.1))

# Display the radar chart
plt.show()
