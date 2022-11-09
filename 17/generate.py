import pyrosim.pyrosim as pyrosim
import random
import constants as c

def Create_World():
    pyrosim.Start_SDF(f"{c.folder}world.sdf")
    x = -2
    y = 2
    z = 0.5
    length = 1
    width  = 1
    height = 1
    pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
    pyrosim.End()


def Create_Robot():
    pass

def Generate_Body():
    pyrosim.Start_URDF(f"{c.folder}body.urdf")
    length = 1
    width  = 1
    height = 1
    pyrosim.Send_Cube(name="Torso",   pos=[1.5, 0, 1.5] , size=[length, width, height])
    pyrosim.Send_Joint(name = "Torso_BackLeg" , parent= "Torso" ,
     child = "BackLeg" , type = "revolute", position = [1,0,1])
    pyrosim.Send_Cube(name="BackLeg",   pos=[-0.5, 0, -0.5] , size=[length, width, height])
    pyrosim.Send_Joint(name = "Torso_FrontLeg" , parent= "Torso" ,
     child = "FrontLeg" , type = "revolute", position = [2,0,1])
    pyrosim.Send_Cube(name="FrontLeg",   pos=[0.5, 0, -0.5] , size=[length, width, height])
    pyrosim.End()


def Generate_Brain():
    pyrosim.Start_NeuralNetwork(f"{c.folder}brain.nndf")
    pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
    pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
    pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
    pyrosim.Send_Motor_Neuron( name=3, jointName="Torso_FrontLeg")
    pyrosim.Send_Motor_Neuron( name=4, jointName="Torso_BackLeg")
    for i in range(3):
        for j in range(3,5):
            pyrosim.Send_Synapse( sourceNeuronName = i , targetNeuronName = j , weight = -1 + (1-(-1)) * random.random() )
    pyrosim.End()


Create_World()
Generate_Body()
Generate_Brain()


