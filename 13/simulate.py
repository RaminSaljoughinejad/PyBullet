import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np
from random import randint as rnd
import matplotlib.pyplot as plt

physicClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF(r"C:\Users\Ramin\Documents\pyBullet\13\body.urdf")

p.setGravity(0, 0, -9.8)
p.loadSDF('13/world.sdf')

backLegSensorValues = np.zeros(100000)
frontLegSensorValues = np.zeros(100000)

pyrosim.Prepare_To_Simulate(robotId)

backleg_amplitude = np.pi/4
backleg_frequency = 0.120
backleg_phaseOffset = 0

FrontLeg_amplitude = np.pi/4
FrontLeg_frequency = 0.120
FrontLeg_phaseOffset = np.pi/4

BackLeg = [backleg_amplitude * np.sin(backleg_frequency * i + backleg_phaseOffset) for i in range(1000)]
FrontLeg = [FrontLeg_amplitude * np.sin(FrontLeg_frequency * i + FrontLeg_phaseOffset) for i in range(1000)]
# plt.plot(range(len(BackLeg)), BackLeg)
# plt.plot(range(len(FrontLeg)), FrontLeg)
# plt.show()
# exit()
for i in range(100000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b"Torso_BackLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = 2,
                maxForce = 90)
    pyrosim.Set_Motor_For_Joint(
                bodyIndex = robotId,
                jointName = b"Torso_FrontLeg",
                controlMode = p.POSITION_CONTROL,
                targetPosition = FrontLeg[i],
                maxForce = 90)

    time.sleep(0.0001)
    
with open("13/data/backLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, backLegSensorValues)
with open("13/data/frontLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, frontLegSensorValues)

p.disconnect()