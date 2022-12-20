import numpy as np
import matplotlib.pyplot as plt

def lane_emden(n, xi_max, tolerance=1e-6):
    # Initialize the solution array and the first two terms
    θ = np.zeros(xi_max)
    θ[0] = 1
    θ[1] = (1 / n) ** (1 / (n - 1))

    # Initialize the radius array and the first two terms
    xi = np.zeros(xi_max)
    xi[0] = 0
    xi[1] = θ[1] ** (1 / n)

    # Iterate over the remaining terms
    for i in range(2, xi_max):
        # Calculate the next term using the relaxation method
        θ_new = (θ[i - 1] ** n + (2 / (i - 1)) * θ[i - 2]) / (1 + (2 / (i - 1)))
        # Check the tolerance and exit the loop if it is met
        if abs(θ_new - θ[i - 1]) < tolerance:
            break
        # Update the solution array
        θ[i] = θ_new
        # Calculate the radius array
        xi[i] = xi[i - 1] + θ[i] ** (1 / n)

    # Return the solution and radius arrays
    return θ, xi



# Solve the Lane-Emden equation for n = 3
θ, xi = lane_emden(3, 1000)

# Plot the solution
plt.plot(xi, θ)
plt.xlabel('Radius (xi)')
plt.ylabel('Dimensionless density (θ)')
plt.title('Solution to the Lane-Emden equation')
plt.show()

