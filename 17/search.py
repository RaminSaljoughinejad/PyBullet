import os
from hillclimber import HILL_CLIMBER
import constants as c

# for i in range(2):
#     os.system(f"python {c.folder}generate.py")
#     os.system(f"python {c.folder}simulate.py")
print("**********************************************************************************")
print("**********************************************************************************")
print()
print(f"Number of Iteration: {c.steps}       Number of Generation: {c.numberOfGenerations}")
print()
print("**********************************************************************************")
print("**********************************************************************************")
if input("Start? "):
    hc = HILL_CLIMBER()
    hc.Evolve()
    hc.Show_Best()