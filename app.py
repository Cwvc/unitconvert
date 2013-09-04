#------------------------------------# 
# Application:           unitconvert |
#------------------------------------#
# Author:               Austin Welsh |
# Date Started:           08.03.2013 |
# Last Update:            08.03.2013 |
#                                    |
#         Help or questions?         |
#           Contact me at:           |
#        crosswavc@gmail.com         |
#                                    |
#------------------------------------#

import os

def clear():
	os.system('clear')

def main():
	print('')
	print(" #----------------#")
	print(" | Unit Converter |")
	print(" #----------------#")

#TabCheckers
def metricCheck(x):
	print(" #-----------------------------------------------#")
	if x == '1':
		print(" | Enter the number in: milimeters (mm)          |")
        elif x == '2':
                print(" | Enter the number in: centimeters (cm)         |")
        elif x == '3':
                print(" | Enter the number in: decimeters (d)           |")
        elif x == '4':
                print(" | Enter the number in: meters (m)               |")
        elif x == '5':
                print(" | Enter the number in: decameters (da)          |")
        elif x == '6':
                print(" | Enter the number in: hectometers (h)          |")
        elif x == '7':
		print(" | Enter the number in: kilometers (k)           |")
	inp = input(" |  > ")
	
	if x == '1':
		mm = inp
		cm = inp / 10
		d = inp / 100
		m = inp / 1000
		da = inp / 10000
		h = inp / 100000
		k = inp / 1000000
		display('metric',mm,cm,d,m,da,h,k)
	elif x == '2':
		mm = inp * 10
                cm = inp
                d = inp / 10
                m = inp / 100
                da = inp / 1000
                h = inp / 10000
                k = inp / 100000
                display('metric',mm,cm,d,m,da,h,k)
	elif x == '3':
		mm = inp * 100
                cm = inp * 10
                d = inp 
                m = inp / 10
                da = inp / 100
                h = inp / 1000
                k = inp / 10000
                display('metric',mm,cm,d,m,da,h,k)
	elif x == '4':
		mm = inp * 1000
                cm = inp * 100
                d = inp * 10
                m = inp 
                da = inp / 10
                h = inp / 100
                k = inp / 1000
                display('metric',mm,cm,d,m,da,h,k)
	elif x == '5':
		mm = inp * 10000
                cm = inp * 1000
                d = inp * 100
                m = inp * 10     
                da = inp   
                h = inp / 10  
                k = inp / 100
                display('metric',mm,cm,d,m,da,h,k)
	elif x == '6':
		mm = inp * 100000
                cm = inp * 10000
                d = inp * 1000
                m = inp * 100      
                da = inp * 10
                h = inp  
                k = inp / 10
                display('metric',mm,cm,d,m,da,h,k)
	elif x == '7':
		mm = inp * 1000000
                cm = inp * 100000
                d = inp * 10000
                m = inp * 1000
                da = inp * 100  
                h = inp * 10        
                k = inp  
                display('metric',mm,cm,d,m,da,h,k)
#TABS
def metric():
	print('')
	print(" #---------------#")
	print(" | Metric System |")
	print(" |-----------------------------------------------#")
	print(" |                                               |")
	print(" |  1 | Convert milimeters                       |")
	print(" |  2 | Convert centimeters                      |")
	print(" |  3 | Convert decimeters                       |")
	print(" |  4 | Convert meters                           |")
	print(" |  5 | Convert dekameters                       |")
	print(" |  6 | Convert hectometers                      |")
	print(" |  7 | Convert kilometers                       |")
	print(" |                                               |")
	print(" #-----------------------------------------------#")
	print(" | Select an option by the corresponding number: |")
	inputvar = raw_input(" |  > ")
	metricCheck(inputvar)
#Display
def display(type,A,B,C,D,E,F,G):
	clear()
	if type == "metric":
		print('')
		print(" #---------------#")
        	print(" | Metric System |")
        	print(" |-----------------------------------------------#")
        	print(" |                                               |")
		print(' | Millimeters: ' + str(A))
		print(' | Centimeters: ' + str(B))
		print(' | Decimeters : ' + str(C))
		print(' | Meters     : ' + str(D))
		print(' | Dekameters : ' + str(E))
		print(' | Hectometers: ' + str(F))
		print(' | Kilometers : ' + str(G))
		print(" |                                               |")
		print(" #-----------------------------------------------#")
		null = raw_input(' | Press enter to continue.')
		clear()
		main()
		metric()
#START APPLICATION
clear()
main()
metric()
