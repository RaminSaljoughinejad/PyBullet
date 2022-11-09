import pybullet as p
import time
import pybullet_data
import pyrosim.pyrosim as pyrosim
import numpy as np

physicClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF(r"C:\Users\Ramin\Documents\pyBullet\11\body.urdf")

p.setGravity(0, 0, -9.8)
p.loadSDF('11/world.sdf')

backLegSensorValues = np.zeros(1000)
frontLegSensorValues = np.zeros(1000)

pyrosim.Prepare_To_Simulate(robotId)
for i in range(1000):
    p.stepSimulation()
    backLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("BackLeg")
    frontLegSensorValues[i] = pyrosim.Get_Touch_Sensor_Value_For_Link("FrontLeg")
    time.sleep(0.01)
    
with open("11/data/backLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, backLegSensorValues)
with open("11/data/frontLegSensorValues.npy", "wb") as outfile:
    np.save(outfile, frontLegSensorValues)

p.disconnect()