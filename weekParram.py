#  (\___/)
#  (='.'=)
#  (")_(")

# ---*** IMPORT LIBRARIES ***---

import numpy as np
#import scipy as sp
import matplotlib.pyplot as plt
#import math import *
#from random import uniform
#import random as *
#import glob

# ---*** GLOBAL VARIABLES ***---
moveAvg = 1
win = 50
overlay = 1
# ---*** DEFINE FUNCTIONS ***---


# ---*** SCRIPT ***---
days = ["monday","tuesday","wednesday","thursday","friday","saturday","sunday"]
dir = "data/"
dataArr = []

for i in np.arange(0,7,1):
	dataArr.append([])
	fileName = dir+days[i]+".csv"
	dataArr[i]=(np.loadtxt(fileName,delimiter = ",",skiprows=1,usecols=(1,2,3,4)))

rawDataArr = dataArr

#a = 1
#b = 21
#print(np.mean(rawDataArr[0][a:b,0]))

if moveAvg == 1:
	for Q in np.arange(0,7,1):
		for R in np.arange(0,4,1):
			for S in np.arange(0,len(dataArr[0]),1):
				if (S < win):
					dataArr[Q][S,R] = np.mean(rawDataArr[Q][:(S+win),R])
					#print("LOW :" + str(S))
					#print(np.mean(rawDataArr[Q][:S,R]))
				elif (S > len(dataArr[0])-win):
					dataArr[Q][S,R] = np.mean(rawDataArr[Q][(S-win):,R])
					#print("UP: " + str(S))
					#print(np.mean(rawDataArr[Q][S:,R]))
				else:
					minVal = S - win
					maxVal = S + win
					#print(minVal)
					#print(maxVal)
					#print("S: " + str(S))
					#print(rawDataArr[Q][minVal:maxVal,R])
					dataArr[Q][S,R] = np.mean(rawDataArr[Q][minVal:maxVal,R])

if overlay == 1:
	for k in np.arange(1,5,1):
		plt.figure(k)
		for j in np.arange(0,7,1):
			plt.plot(dataArr[j][:,k-1])
			plt.legend(days)

	plt.figure(1)
	plt.xlabel("Time [min]")
	plt.ylabel("Temp [$^\circ$C]")
	plt.xlim([0,len(dataArr[0])-1])
	plt.title("Temperatures during each day of the week")


	plt.figure(2)
	plt.xlabel("Time [min]")
	plt.ylabel("Pressure [bar]")
	plt.xlim([0,len(dataArr[0])-1])
	plt.title("Pressure during each day of the week")


	plt.figure(3)
	plt.xlabel("Time [min]")
	plt.ylabel("Wind velocity [knots]")
	plt.xlim([0,len(dataArr[0])-1])
	plt.title("Wind velocity during each day of the week")


	plt.figure(4)
	plt.xlabel("Time [min]")
	plt.ylabel("Wind heading [$^\circ$]")
	plt.xlim([0,len(dataArr[0])-1])
	plt.title("Wind heading during each day of the week")

	plt.show()

#else:
#        for k in np.arange(1,5,1):
#                plt.figure(k)
#                for j in np.arange(0,7,1):
#                        plt.plot(rawDataArr[j][:,k-1])
#                        plt.legend(days)
#
#	plt.show()

print("Data filtered with moving filter")
