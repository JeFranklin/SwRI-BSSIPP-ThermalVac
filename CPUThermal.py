#Jesse Franklin
#SwRI
#CPU Heat Sink

import sys
import aerocalc.std_atm as sa
import matplotlib.pyplot as plt
import numpy as np

#s = thickness
#K = conduvtivity 

Materials = {0 : 'CPU', 1 : 'A.S.1', 2 : 'Fan', 3 : 'A.S.2', 4 : 'Al', 5 : 'A.S.3', 6 : '80/20', 7 : 'A.S.4'}
Thickness = {'CPU' : 0, 'A.S.1' : 0.001, 'A.S.2' : 0.001, 'A.S.3' : 0.001,  'A.S.4' : 0.001, 'Al' : 0.110, '80/20' : 0.050, 'Fan' : 0.0013}
Conductivities = {'CPU' : 0, 'A.S.1' : 8.7, 'A.S.2' : 8.7,  'A.S.3' : 8.7,  'A.S.4' : 8.7, 'Al' : 205, '80/20' : 205, 'Fan' : 205}
Areas = {'CPU' : 0.00064516, 'A.S.1' : 0.00175, 'Al' : 0.03, 'A.S.2' : 0.00175, '80/20' : 0.00064516, 'A.S.3' : 0.00048752, 'Fan' : 0.00064516, 'A.S.4' : 0.00175} 

Tcpu = 78
Tcold = 16.5
Qcpu = 50

### q = (T1 - Tn) / ((s1 / k1 A) + (s2 / k2 A) + ... + (sn / kn A)) 

ThermalRes = 	((Thickness['A.S.1'] / (Conductivities['A.S.1'] * Areas['A.S.1'])) 			\
				+ (Thickness['Fan'] / (Conductivities['Fan'] * Areas['Fan']))  			\
				+ (Thickness['A.S.2'] / (Conductivities['A.S.2'] * Areas['A.S.2']))  	\
				+ (Thickness['Al'] / (Conductivities['Al'] * Areas['Al'])) 				\
				+ (Thickness['A.S.3'] / (Conductivities['A.S.3'] * Areas['A.S.3'])) 	\
				+ (Thickness['80/20'] / (Conductivities['80/20'] * Areas['80/20'])) 	\
				+ (Thickness['A.S.4'] / (Conductivities['A.S.4'] * Areas['A.S.4']))) 

q = (Tcpu - Tcold) / ThermalRes

print "Thermal Resistance = ", ThermalRes				
print "Total Flux = ", q, "W"

### q = (KAdT)/s

#CPU-Paste
print "Tcpu = ", Tcpu
i = 1
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T0 = ((K*Area*Tcpu)-(Qcpu*s))/(K*Area)
print "Temp 0 = ", T0, "c"

#Paste-Fan
i = 2
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T1 = ((K*Area*T0)-(Qcpu*s))/(K*Area)
print "Temp 1 = ", T1, "c"

#Fan-Paste
i = 3
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T2 = ((K*Area*T1)-(Qcpu*s))/(K*Area)
print "Temp 2 = ", T2, "c"


#Paste-Al
i = 4
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T3 = ((K*Area*T2)-(Qcpu*s))/(K*Area)
print "Temp 3 = ", T3, "c"


#Al-Paste
i = 5
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T4 = ((K*Area*T3)-(Qcpu*s))/(K*Area)
print "Temp 4 = ", T4, "c"


#Paste-80/20
i = 6
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T5 = ((K*Area*T4)-(Qcpu*s))/(K*Area)
print "Temp 5 = ", T5, "c"


#80/20-Paste
i = 7
s = Thickness[Materials[i]] 
K = Conductivities[Materials[i]]
Area = Areas[Materials[i]]

T6 = ((K*Area*T5)-(Qcpu*s))/(K*Area)
print "Temp 6 = ", T6, "c"

print "Tframe = ", Tcold 


###sinking paths Tcpu recalculator
ThermalRes80 = 	  (Thickness['A.S.1'] / (Conductivities['A.S.1'] * Areas['A.S.1'])) 	\
				+ (Thickness['Fan'] / (Conductivities['Fan'] * Areas['Fan']))  			\
				+ (Thickness['A.S.2'] / (Conductivities['A.S.2'] * Areas['A.S.2']))  	\
				+ (Thickness['Al'] / (Conductivities['Al'] * Areas['Al']))

print "Thermal Resistance - 80/20 = ", ThermalRes80 
CTcpu = ( Qcpu * ThermalRes80) + 30
print "Calculated Tcpu = ", CTcpu, "c"

if T0 < 0 or T1 < 0 or T2 < 0 or T3 < 0 or T4 < 0 or T5 < 0 or T6 < 0:
	sys.exit("There is an error")

#Plots the Data
x = [0, 1, 2, 3, 4, 5, 6]
y = [T0, T1, T2, T3, T4, T5, T6]

plt.scatter(0,T0)
plt.scatter(1,T1)
plt.scatter(2,T2)
plt.scatter(3, T3)
plt.scatter(4,T4)
plt.scatter(5,T5)
plt.scatter(6,T6)
plt.plot(x,y,'-o')
plt.grid(True)
plt.title("Temperature Profile for B-SSIPP CPU Heat Sink")
plt.xlabel('Temp Value') 
plt.ylabel('Temperature  [k]')


plt.show()