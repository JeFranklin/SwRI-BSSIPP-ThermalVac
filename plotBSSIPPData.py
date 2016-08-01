## Python Plotting of BSSIPP Az Pointer Data
## Jed Diller
## SwRI

import pandas as pd
import matplotlib.pyplot as plt

# Sample Data
# 638.470009,  +12.53,   -0.20,   -0.25,   +0.00,   +0.00,   +0.00,  +90.00,   +0.00,   +0.00,  +18.40,  +82.77

# Columns:
columns = [	"gpsTime","ypr.c0","ypr.c1","ypr.c2","angularRate.c0","angularRate.c1",
			"angularRate.c2","attitudeUncertainty","positionUncertainty","velocityUncertainty",
			"temperature","pressure" ]

df = pd.read_csv("disturbanceTest_90deg.data", names=columns, header=None)

# Adjust GPS time to start at 0
first_time = df['gpsTime'][0] 
for index,row in df.iterrows():
	df.loc[index,'gpsTime'] -= first_time 


print df['gpsTime'] 


plot = df.plot(title='Yaw vs Time', y='ypr.c0',x='gpsTime', subplots=True)
plt.grid(True)
plt.show()