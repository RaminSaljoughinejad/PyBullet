import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("07/boxes.sdf")

x = 0
y = 0
z = 0.5

length = 1
width  = 1
height = 1
for i in range(1,25):
    length*=0.9
    width*=0.9
    height*=0.9
    pyrosim.Send_Cube(name=f"Box{i}", pos=[x, y, z*2*i] , size=[length, width, height])


pyrosim.End()
