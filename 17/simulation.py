from world import WORLD
from robot import ROBOT
import pybullet as p
import pybullet_data
import pyrosim.pyrosim as pyrosim
import constants as c
import time

class SIMULATION:
    def __init__(self, directOrGUI):
        if directOrGUI=="DIRECT":
            self.physicClient = p.connect(p.DIRECT)
        else:
            self.physicClient = p.connect(p.GUI)
        p.setAdditionalSearchPath(pybullet_data.getDataPath())
        self.world = WORLD()
        self.robot = ROBOT()
        p.setGravity(0, 0, -9.8)
        

    def Run(self):
        for i in range(c.steps):
            p.stepSimulation()
            self.robot.Sense(i)
            self.robot.Think()
            self.robot.act(i)
            # print(i)
            #time.sleep(0.001)
    def __del__(self):
        p.disconnect()

    def Get_Fitness(self):
        self.robot.Get_Fitness()

