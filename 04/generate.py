import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("04/box.sdf")

x = 0
y = 0
z = 0.5

length = 1
width  = 1
height = 3

pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])

pyrosim.End()
