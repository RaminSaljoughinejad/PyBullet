import pybullet as p
import time

physicClient = p.connect(p.GUI)

p.loadSDF('02/box.sdf')
for i in range(10000):
    p.stepSimulation()
    time.sleep(0.01)
    print(i)


p.disconnect()