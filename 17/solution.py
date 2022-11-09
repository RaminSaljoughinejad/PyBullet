import os
import numpy as np
import pyrosim.pyrosim as pyrosim
import constants as c
import random



class SOLUTION:
    def __init__(self):
        self.weights = np.random.rand(3,2)
        self.weights = self.weights * 2 - 1

    def Evaluate(self, directORgui):
        self.Create_World()
        self.Create_Body()
        self.Create_Brain()
        os.system(f"python {c.folder}simulate.py {directORgui}")
        fitnessFile = "fitness.txt"
        with open(f"{c.folder}{fitnessFile}", "r") as f:
            self.fitness = float(f.read())

    def Create_World(self):
        pyrosim.Start_SDF(f"{c.folder}world.sdf")
        x = -2
        y = 2
        z = 0.5
        length = 1
        width  = 1
        height = 1
        pyrosim.Send_Cube(name="Box", pos=[x, y, z] , size=[length, width, height])
        pyrosim.End()

    def Create_Body(self):
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

    def Create_Brain(self):
        pyrosim.Start_NeuralNetwork(f"{c.folder}brain.nndf")
        pyrosim.Send_Sensor_Neuron(name=0, linkName="Torso")
        pyrosim.Send_Sensor_Neuron(name=1, linkName="FrontLeg")
        pyrosim.Send_Sensor_Neuron(name=2, linkName="BackLeg")
        pyrosim.Send_Motor_Neuron( name=3, jointName="Torso_FrontLeg")
        pyrosim.Send_Motor_Neuron( name=4, jointName="Torso_BackLeg")
        for currentRow in range(3):
            for currentColumn in range(2):
                pyrosim.Send_Synapse( sourceNeuronName = currentRow , targetNeuronName = currentColumn+3 , weight = self.weights[currentRow][currentColumn] )
        pyrosim.End()

    def Mutate(self):
        randomRow= random.randint(0,2)
        randomColumn= random.randint(0,1)

        self.weights[randomRow][randomColumn] =  random.random() * 2 - 1