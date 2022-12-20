import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Constants
gamma = 1.4  # ratio of specific heats

# Initial conditions
rho_left = 1.0  # density on the left side
rho_right = 0.125  # density on the right side
p_left = 1.0  # pressure on the left side
p_right = 0.1  # pressure on the right side
v_left = 0.0  # velocity on the left side
v_right = 0.0  # velocity on the right side
x_min = 0.0  # minimum x value
x_max = 1.0  # maximum x value
nx = 100  # number of grid points

# Set up grid
dx = (x_max - x_min) / nx  # grid spacing
x = np.linspace(x_min, x_max, nx)  # grid

# Set up empty arrays to store the solution
rho = np.empty(nx)
p = np.empty(nx)
v = np.empty(nx)

# Set the initial conditions
rho[:int(nx/2)] = rho_left  # density on the left side
rho[int(nx/2):] = rho_right  # density on the right side
p[:int(nx/2)] = p_left  # pressure on the left side
p[int(nx/2):] = p_right  # pressure on the right side
v[:int(nx/2)] = v_left  # velocity on the left side
v[int(nx/2):] = v_right  # velocity on the right side

# Set up the figure and axis
fig, ax = plt.subplots()
line1, = ax.plot(x, rho, label="Density")
line2, = ax.plot(x, p, label="Pressure")
line3, = ax.plot(x, v, label="Velocity")
ax.legend()

def animate(i):
    # Calculate the intermediate states
    for j in range(i):
        rho_star = rho[j] * (v[j] - v[j+1] + v[j] * (rho[j+1]/rho[j] - 1)) / (v[j] - v[j+1] + v[j] * (rho[j]/rho[j+1] - 1))
        p_star = p[j] * ((2*gamma*v[j] - v[j+1] + v[j]*(rho[j]/rho[j+1] - 1)) / (2*gamma - v[j+1] + v[j]*(rho[j]/rho[j+1] - 1)))**(2*gamma / (gamma - 1))
        v_star = (p_star / p[j]) * (v[j] - v[j+1] + v[j] * (rho[j]/rho[j+1] - 1))

        # Calculate the states at the next time step
        if v_star > 0:
            rho[j+1] = rho[j] * (v[j] - v_star) / (v[j] - v[j+1])
            p[j+1] = p[j] * (v[j] - v[j+1]) / (v[j] - v_star)
            v[j+1] = v_star
        else:
            rho[j+1] = rho[j+1] * (v[j+1] - v_star) / (v[j+1] - v[j])
            p[j+1] = p[j+1] * (v[j+1] - v[j]) / (v[j+1] - v_star)
            v[j+1] = v_star

    # Update the plots
    line1.set_ydata(rho)
    line2.set_ydata(p)
    line3.set_ydata(v)



# Set up the animation
ani = animation.FuncAnimation(fig, animate, frames=nx, interval=50)

# Show the animation
plt.show()
