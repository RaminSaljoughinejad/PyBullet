import constants as c
import numpy as np
import pyrosim.pyrosim as pyrosim

class SENSOR:
    def __init__(self, linkName):
        self.linkName = linkName
        self.values = np.zeros(c.steps)
        
    def Get_Value(self, time_step):
        self.values[time_step] = pyrosim.Get_Touch_Sensor_Value_For_Link(self.linkName)
        # if time_step+1==c.steps:
        #     print(self.values)

    def Save_Values(self):
        with open(f"16/data/{self.linkName}.npy", "wb") as outfile:
            np.save(outfile, self.values)