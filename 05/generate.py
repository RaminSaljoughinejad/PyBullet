import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("05/boxes.sdf")

x = 0
y = 0
z = 0.5

length = 1
width  = 1
height = 1

pyrosim.Send_Cube(name="Box1", pos=[x, y, z] , size=[length, width, height])
pyrosim.Send_Cube(name="Box2", pos=[x+length, y, z+height] , size=[length, width, height])

pyrosim.End()
