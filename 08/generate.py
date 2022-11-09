import pyrosim.pyrosim as pyrosim

pyrosim.Start_SDF("08/boxes.sdf")

x = 0
y = 0
z = 0.5

main_length = 1
main_width  = 1
main_height = 1
length = 1
width  = 1
height = 1
for i in range(0,10):
    for j in range(0,5):
        for k in range(0,5):
            pyrosim.Send_Cube(name=f"Box{i}",    pos=[x+main_length*j, y+main_width*k    , z+main_height*i] , size=[length, width, height])
        
    length*=0.9
    width*=0.9
    height*=0.9

pyrosim.End()
