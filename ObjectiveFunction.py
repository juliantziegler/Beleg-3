from Floorball_Model import ModelFloorball
from scipy.optimize import minimize
import numpy as np
import matplotlib.pyplot as plt
from statistics import median


def floorball_objective(theta, v0):
    dt = 0.001
    model = ModelFloorball(theta[0], v0, dt)
    model.run()
    data = model.data
    return 1/data[1, -1]


def optimize_angle(v0: float):
    # function to optimize the release angle given a specific initial velocity
    theta = np.array([45])
    result = minimize(floorball_objective, theta, args=(v0,), method='Nelder-Mead')
    if result.success:
        return result.x
    else:
        print('Minimization failed')
        print(result.message)
        return None


def get_angle_results(v0):
    values = np.arange(20, 60, 0.5)
    for theta in values:
        theta = np.array([theta])
        print(theta, 1/floorball_objective(theta, v0))


def get_angle_for_velocities(start_vel: int, end_vel: int):
    initial_vels = np.arange(start_vel, end_vel, 1)
    best_angles = []
    for v0 in initial_vels:
        i = 0
        volatile_list = []
        for i in range(10):
            volatile_list.append(optimize_angle(v0))
            i += 1
        best_angles.append(median(volatile_list))
        print('Got result for v0={}'.format(v0))

    plt.plot(initial_vels, best_angles)
    plt.xlabel('Initial velocity')
    plt.ylabel('Optimum angle')
    plt.show()


if __name__ == '__main__':
    #get_angle_results(30)
    print(optimize_angle(60))
    #get_angle_for_velocities(1, 100)
