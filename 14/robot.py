from os import link
import pybullet as p
import pyrosim.pyrosim as pyrosim
from sensor import SENSOR
from motor import MOTOR
class ROBOT:
    def __init__(self):
        self.robotId = p.loadURDF("14/body.urdf")
        pyrosim.Prepare_To_Simulate(self.robotId)
        self.Prepare_To_Sense()
        self.Prepare_To_Act()

    def Prepare_To_Sense(self):
        self.sensors = {}
        for linkName in pyrosim.linkNamesToIndices:
            self.sensors[linkName] = SENSOR(linkName) 

    def Sense(self, time_step):
        for i in self.sensors:
            self.sensors[i].Get_Value(time_step)

    def Prepare_To_Act(self):
        self.motors  = {}
        for linkName in pyrosim.jointNamesToIndices:
            self.motors[linkName] = MOTOR(linkName)

    def act(self, time_step):
        for i in self.motors:
            self.motors[i].Set_Value(time_step, self.robotId)