#Jesse Franklin
#SwRI
#B-SSIPP Float Thermal Profile

from PIL import Image 
import sys
import aerocalc.std_atm as sa
import matplotlib.pyplot as plt
import numpy as np

Qs = 1300 #estimated-to be specified
Stefan_Boltzmann = 0.0000000567

Materials = {5 : 'Tape', 4 : 'Kapton', 3 : 'Foam', 2 : 'Kapton', 1 : 'Al'}
Thicknesses = {'Tape' : 0.01, 'Kapton' : 0.0000635, 'Foam' : 0.0381, 'Al' : 0.00254}
Emissivities = {'Tape' : 0.9, 'Kapton' : 0.34, 'Foam' : 0.6, 'Al' : 0.82}
Absorptivities = {'Tape' : 0.3, 'Kapton' : 0.25, 'Foam' : 0., 'Al' : 0.65}
Conductivities = {'Tape' : 0.05, 'Kapton' : 0.05, 'Foam' : 0.03, 'Al' : 205}

Area = input("Area = ")
print "Qs = ",  Qs, "W/m^2"

i = 5

while i == 5:
	Thickness = Thicknesses[Materials[i]] 
	Emissivity = Emissivities[Materials[i]]
	Absorptivity = Absorptivities[Materials[i]]
	Conductivity = Conductivities[Materials[i]]
	def Emit(n):
		"""Returns Emitted Heat"""
		Qemit = Qs*Emissivity
		return Qemit
	Emit(Emissivity)

	def useEmit(passed_Emit):
		"""Allows Qemit to be passed into Abs"""
	
	def Abs(n):
		"""Returns Absorbed Heat from Emitted"""
		Qemit = Emit(Emissivity)
		useEmit(Qemit)
		Qabs = Qs - Qemit
		return Qabs
	Abs(Absorptivity)

	def useAbs(passed_Abs):
		"""Allows Qabs to be passed into T3"""

	def Temp6():
		"""Returns T6"""
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)
		T6 = (Qabs/(Stefan_Boltzmann*Area))**0.25
		return T6
	Temp6()

	def useTemp6(passed_Temp6):
		"""Allows T6 to be passed into T5"""

	def Temp5():
		"""Returns T5"""
		T6 = Temp6()
		useTemp6(T6)
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)
		T5 = ((Conductivity*Area*T6)-(Qabs*Thickness))/(Conductivity*Area)
		return T5
	Temp5()

	i-=1

def use_Temp5(passed_Temp5):
	"""Allows T5 to be passed to T4"""

Thickness = Thicknesses[Materials[i]]
Conductivity = Conductivities[Materials[i]]
while i == 4:
	def Temp4():
		"""Returns T5"""
		T5 = Temp5()
		use_Temp5(T5)
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)
		T4 = ((Conductivity*Area*T5)-(Qabs*Thickness))/(Conductivity*Area)
		return T4
	Temp4()

	def useTemp4(passed_Temp4):
		"""Allows T4 to be passed into T3"""

	i-=1

Thickness = Thicknesses[Materials[i]]
Conductivity = Conductivities[Materials[i]]
while i == 3:
	def Temp3():
		"""Returns T3"""
		T4 = Temp4()
		useTemp4(T4)
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)	
		T3 = ((Conductivity*Area*T4)-(Qabs*Thickness))/(Conductivity*Area)
		return T3
	Temp3()

	def useTemp3(passed_Temp3):
		"""Allows T3 to be passed into T2"""

	i-=1

Thickness = Thicknesses[Materials[i]]
Conductivity = Conductivities[Materials[i]]
while i == 2:
	def Temp2():
		"""Returns T2"""
		T3 = Temp3()
		useTemp3(T3)
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)
		T2 = ((Conductivity*Area*T3)-(Qabs*Thickness))/(Conductivity*Area)
		return T2
	Temp2()

	def useTemp2(passed_Temp2):
		"""Allows T2 to be passed into T1"""

	i-=1

Thickness = Thicknesses[Materials[i]]
Conductivity = Conductivities[Materials[i]]
while i == 1:
	def Temp1():
		"""Returns T1"""
		T2 = Temp2()
		useTemp2(T2)
		Qabs = Abs(Absorptivity)
		useAbs(Qabs)
		T1 = ((Conductivity*Area*T2)-(Qabs*Thickness))/(Conductivity*Area)
		return T1
	Temp1()

	break

E = Emit(Materials[5])
print "Qemit = ", E, "W/m^2"

A = Abs(Emit)
print "Qabs = ", A, "W/m^2"

temp6 = Temp6()
print "Temp 6 = ", temp6 - 273, "c"

temp5 = Temp5()
print "Temp 5 = ", temp5 - 273, "c"

temp4 = Temp4()
print "Temp 4 = ", temp4 - 273, "c"

temp3 = Temp3()
print "Temp 3 = ", temp3 - 273, "c"

temp2 = Temp2()
print "Temp 2 = ", temp2 - 273, "c"

temp1 = Temp1()
print "Temp 1 = ", temp1 -273, "c"

if temp6 < 0 or temp5 < 0 or temp4 < 0 or temp3 < 0 or temp2 < 0 or temp1 < 0:
	sys.exit("There is an error")

#Plots the Data
x = [6, 5, 4, 3, 2, 1]
y = [temp6, temp5, temp4, temp3, temp2, temp1]

plt.scatter(6,temp6)
plt.scatter(5,temp5)
plt.scatter(4,temp4)
plt.scatter(3, temp3)
plt.scatter(2,temp2)
plt.scatter(1,temp1)
plt.plot(x,y,'-o')
plt.grid(True)
plt.title("Temperature Profile for B-SSIPP at Float")
plt.xlabel('Temp Value') 
plt.ylabel('Temperature  [k]')
plt.gca().invert_xaxis()

plt.show()

img = Image.open('Thermal Profile.png')
img.show()