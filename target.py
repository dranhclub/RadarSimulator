from utils.helper import rphi_to_xy, xy_to_rphi
from noise import Noise
import numpy as np

class Target():
    def __init__(self, r, a, dir, v) -> None:
        """
        Params:
            r: distance to radar
            a: azimuth
            dir: hướng di chuyển
            v: vận tốc di chuyển
        """

        self.dir = dir
        self.v = v
        self.set_ra(r, a)

        self.FADING_RATE = 0.99
        self.alpha = 0

        self.noises = self.gen_noise()

    def gen_noise(self):
        noises = []
        N = np.random.randint(low=5, high=10 + 1)
        R = 8
        for i in range(N):
            noise = Noise(0, 0, self.dir, self.v)
            dx = np.random.randn() * R
            dy = np.random.rand() * R
            noise.set_xy(self.x + dx, self.y + dy)
            noises.append(noise)
        return noises

    def set_xy(self, x, y):
        self.x = x
        self.y = y
        r, a = xy_to_rphi(x, y)
        self.r = r
        self.a = a % 360

    def set_ra(self, r, a):
        self.r = r
        self.a = a % 360
        self.x, self.y = rphi_to_xy(r, a)

    def update(self):
        dx, dy = rphi_to_xy(self.v, self.dir)
        self.set_xy(self.x + dx, self.y + dy)
        self.alpha *= self.FADING_RATE