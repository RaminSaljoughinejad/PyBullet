import pybullet as p

class WORLD:
    def __init__(self):
        self.planeId = p.loadURDF("plane.urdf")
        p.loadSDF('16/world.sdf')