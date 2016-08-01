##Jesse Franklin
##SwRI
##ThermalVacc Test Data Plot

#Notes on use:
#1) must have matplotlib, pandas and datetime
#2) must have SPUTNIK ETDP (1 and 2) 6.23.2016.xlsx and htr_shell.log (as a csv)

import matplotlib.pyplot as plt
import pandas as pd
import datetime as dt

df = pd.read_excel('SPUTNIK ETDP 6.23.2016.xlsx')
df1 = pd.read_excel('SPUTNIK ETDP2 6.23.2016.xlsx')
df2 = pd.read_csv('htr_shell.log')

Controls = ['TC1', 'TC3', 'Altitude']
Batteries = ['28.6 V 10 Ah', '18.5 V 10 Ah', '7.4 V 1.4 Ah', '7.4 V 10 Ah', '14.8 V 10 Ah', '29.6 V 10 Ah', '7.4 V 4.8 Ah', '18.5 V 1.75 Ah']
Electronics = ['Inst. Comp. Conduc. Path', 'Inst. Power Conditioning', '20 V Converter', 'FSM Controller', 'Stepper Motor', 'IMU']
Optics = ['FSM Case', 'Optics Bench', 'Detector']
Heaters = ['Heater Zone 1', 'Heater Zone 2', 'Heater Zone 3']
Times = df2.Time
Zone1 = df2.Temp1 #, df2.Status1]
Zone2 = df2.Temp2 #, df2.Status2]
Zone3 = df2.Temp3 #, df2.Status3]
Zone4 = df2.Temp4 #, df2.Status4]

##Converts Unix Time to Human Time
for index,row in df2.iterrows():
	df2.loc[index,'Time'] = dt.datetime.fromtimestamp(int(df2.Time[index]) + 48935).strftime('%H:%M:%S')

##plots the data

def style():
	plt.xlabel('Time')
	plt.ylabel('Temp [c]')
	plt.grid(True)
	axes = plt.gca()
	axes.set_ylim([-20,70])


#controlz
df.plot(title='Controls vs Time', y = Controls, x = 'Time', subplots=True)
style()

#batteriez
df1.plot(title='Batteries vs Time', y=  Batteries, x = 'Time', subplots=False)
style()

#electronix
df1.plot(title='Electronics vs Time', y = Electronics, x = 'Time', subplots=False)
style()

#optix
df1.plot(title='Optics vs Time', y = Optics, x = 'Time', subplots=False)
style()

#heaterz
df1.plot(title='Heaters vs Time', y = Heaters, x = 'Time', subplots=False)
style()
df2.plot(title='Panels vs Time', y = ['Temp1', 'Temp2', 'Temp3', 'Temp4'], x = 'Time', subplots=False)
style()

plt.show()