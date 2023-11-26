import numpy as np
import matplotlib.pyplot as plt


class ModelFloorball:

    def __init__(self, theta, v0, dt):
        # save initialization attributes
        self.dt = dt
        self.theta = theta * np.pi / 180
        self.v0 = v0
        self.v0x = v0 * np.cos(self.theta)
        self.v0y = v0 * np.sin(self.theta)
        # initialize parameters
        self.state = 0, 0, 0, 0

        # model parameters
        self.g = -9.81
        cw = 0.45  # have to find a credible source for a cw value for the floor ball
        A = (36 / 1000) ** 2 * np.pi  # find dimensions of a floor ball
        m = 0.023  # find mass of a floor ball
        rho = 1.225  # kg/m**3
        self.factor = (cw * rho * A) / (4 * m)
        self.data = []

    def run(self):
        self._run_simulation()
        self.data = np.array(self.data).T

    def _run_simulation(self):
        i = 0
        while self.state[1] >= 0:
            if not (i == 0):
                t = self.data[i - 1][0] + self.dt
            else:
                t = 0
            data_array = np.array([t, self.state[0], self.state[1]])
            self.data.append(data_array)
            if i == 0:
                self.state = 0, 0, self.v0x, self.v0y
            self.state = self.rk4_step(self.state, t, self.dt)
            i += 1

        # Trim the data array to the actual number of steps taken

    def model(self, state, t) -> tuple:
        s_x, s_y, v_x, v_y = state

        # Acceleration due to gravity and drag
        a_x = -self.factor * v_x * np.abs(v_x)
        a_y = self.g - self.factor * v_y * np.abs(v_y)

        # Return derivatives
        return v_x, v_y, a_x, a_y

    def rk4_step(self, state, t, dt):
        k1 = np.array(self.model(state, t))
        k2 = np.array(self.model(state + dt / 2 * k1, t + dt / 2))
        k3 = np.array(self.model(state + dt / 2 * k2, t + dt / 2))
        k4 = np.array(self.model(state + dt * k3, t + dt))

        new_state = state + dt / 6 * (k1 + 2 * k2 + 2 * k3 + k4)
        return new_state

    def plot(self):
        t = self.data[0, :]
        s_x = self.data[1, :]
        s_y = self.data[2, :]

        plt.plot(s_x, s_y)
        plt.title('Floorball mit Luftwiderstand, quadratisch Abhängig')
        plt.xlabel('Weite')
        plt.ylabel('Höhe')
        plt.show()

        '''# Corrected plotting code
        plt.figure(figsize=(10, 5))

        # Plot for s_x
        plt.subplot(1, 2, 1)  # 1 row, 2 columns, 1st subplot
        plt.plot(t, s_x)
        plt.xlabel('Zeit')
        plt.ylabel('Weite')
        plt.title('Horizontale Bewegung')

        # Plot for s_y
        plt.subplot(1, 2, 2)  # 1 row, 2 columns, 2nd subplot
        plt.plot(t, s_y)
        plt.xlabel('Zeit')
        plt.ylabel('Höhe')
        plt.title('Vertikale Bewegung')

        plt.suptitle('Lösung des nichtlinearen Differentialgleichungssystems für die gegebenen Werte')
        plt.show()'''


if __name__ == '__main__':
    model = ModelFloorball(theta=35, v0=30, dt=0.01)
    model.run()
    model.plot()
