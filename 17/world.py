import pybullet as p
import constants as c

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF(f'{c.folder}world.sdf')