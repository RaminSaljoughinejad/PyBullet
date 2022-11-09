import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.steps)
        self.Prepare_To_Act()

    def Prepare_To_Act(self):
        self.amplitude = c.amplitude
        self.frequency = c.frequency
        self.offset = c.phaseOffset
        self.motorValues = [self.amplitude * np.sin(self.frequency * i + self.offset) for i in range(c.steps)]
        #self.FrontLeg = [self.amplitude * np.sin(self.frequency * i + self.offset) for i in range(c.steps)]
        

    def Set_Value(self, time_step, robotId):
        pyrosim.Set_Motor_For_Joint(
                        bodyIndex = robotId,
                        jointName = self.jointName,
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = self.motorValues[time_step],
                        maxForce = 90)

    def Save_Values(self):
        with open(f"14/data/{self.jointName}.npy", "wb") as outfile:
            np.save(outfile, self.motorValues)