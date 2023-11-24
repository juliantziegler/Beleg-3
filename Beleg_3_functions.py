import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def diff_s_x(s_x: float,  t: float, theta: float, v0: float):
    cw = 0.2 # have to find a credible source for a cw value for the floor ball
    A = 0.01 # find dimensions of a floor ball
    m = 0.01 # find mass of a floorball
    if t == 0.0:
        return 0
    dsxdt = - (4 * m)/(cw * A * t**2)* s_x + (4*np.cos(theta)*v0*m)/(cw*A*t)
    return dsxdt

def diff_s_y(s_y: float,  t: float, theta: float, v0: float):
    # constants of nature
    g = 9.81
    # constants of the object
    cw = 0.2 # have to find a credible source for a cw value for the floor ball
    A = 0.01 # find dimensions of a floor ball
    m = 0.01 # find mass of a floorball
    if t == 0.0:
        return 0
    dsydt = - (4 * m)/(cw * A * t**2)* s_y - (2*m*g)/(cw*A) + (4*np.sin(theta)*v0*m)/(cw*A*t)
    return dsydt
def main():
    # initial parameters 
    s_x0 = 0
    s_y0 = 0

    # run specific parameters
    theta: float = 1/6 * np.pi
    v0: float = 20

    t = np.linspace(0, 5, 100)


    s_x = odeint(diff_s_x, s_x0, t, args=(theta, v0))

    s_y = odeint(diff_s_y, s_y0, t, args=(theta, v0))

    plt.plot(s_x[:, 0], s_y[:, 0])
    plt.xlabel('Weite')
    plt.ylabel('Höhe')
    plt.title('Lösung des nichtlinearen Differentialgleichungssystems für die gegenbenen Werte')
    plt.show()

if __name__=='__main__':
    main()