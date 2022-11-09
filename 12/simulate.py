import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from random import randint as rnd

physicClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF(r"C:\Users\Ramin\Documents\pyBullet\12\body.urdf")

p.setGravity(0, 0, -9.8)
p.loadSDF('12/world.sdf')

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

pyrosim.Prepare_To_Simulate(robotId)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b"Torso_BackLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = rnd(-2,2),
                maxForce = 90)
    pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b"Torso_FrontLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = rnd(-2,2),
                maxForce = 90)
    time.sleep(0.01)
    
with open("12/data/backLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, backLegSensorValues)
with open("12/data/frontLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, frontLegSensorValues)

p.disconnect()