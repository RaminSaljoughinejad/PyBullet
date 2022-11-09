import pybullet as p
import time
import pybullet_data

physicClient = p.connect(p.GUI)
p.setAdditionalSearchPath(pybullet_data.getDataPath())

planeId = p.loadURDF("plane.urdf")
robotId = p.loadURDF(r"C:\Users\Ramin\Documents\pyBullet\10\body.urdf")

p.setGravity(0, 0, -9.8)
p.loadSDF('10/world.sdf')

for i in range(100000):
    p.stepSimulation()
    time.sleep(0.01)
    print(i)


p.disconnect()