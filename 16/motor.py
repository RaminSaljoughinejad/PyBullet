import numpy as np
import constants as c
import pyrosim.pyrosim as pyrosim
import pybullet as p

class MOTOR:
    def __init__(self, jointName):
        self.jointName = jointName
        self.values = np.zeros(c.steps)   

    def Set_Value(self, desiredAngle, robotId):
        pyrosim.Set_Motor_For_Joint(
                        bodyIndex = robotId,
                        jointName = self.jointName,
                        controlMode = p.POSITION_CONTROL,
                        targetPosition = desiredAngle,
                        maxForce = 50)
