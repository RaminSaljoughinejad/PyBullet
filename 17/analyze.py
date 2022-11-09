import matplotlib.pyplot as plt
import numpy as np
import constants as c

with open(f"{c.folder}data/backLegSensorValues.npy", "rb") as f:
    backLegSensorValues = np.load(f)
with open(f"{c.folder}data/frontLegSensorValues.npy", "rb") as f:
    frontLegSensorValues = np.load(f)

plt.figure(figsize=(15,5))
plt.plot(backLegSensorValues, linewidth=2, label="BackLeg")
plt.plot(frontLegSensorValues, linewidth=0.5, label="FrontLeg")
plt.legend()
plt.show()