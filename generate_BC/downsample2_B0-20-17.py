import scipy.io
import pandas as pd
import numpy as np
import math
from pyXSteam.XSteam import XSteam
steamTable = XSteam(XSteam.UNIT_SYSTEM_MKS)


filename = 'BC_B0-20-17.csv'
experiment = 'B0-20-17'

df = pd.read_csv(filename, sep="\t")

arr = df.values
time_size = 1604			# 1492 for B0-03-50, and 1604 for B0-20-17
pump_delay =  5/0.089  			# 14

TIME = np.zeros(time_size)
FLMV = np.zeros(time_size)
KWTS = np.zeros(time_size)
KWSHRD = np.zeros(time_size)
PRBTC = np.zeros(time_size)
TFLOW = np.zeros(time_size)
TFSC1 = np.zeros(time_size)
TSHROUD = np.zeros(time_size)

for i in range(0,len(arr)):
	tmp=arr[i, 0].split(';')
	TIME[i]    = tmp[0]
	FLMV[i]    = tmp[1]
	KWTS[i]    = tmp[2]
	KWSHRD[i]  = tmp[3] if float(tmp[3]) > 0 else 0 
	PRBTC[i]   = tmp[4]
	TFLOW[i]   = tmp[5]
	TFSC1[i]   = tmp[6]
	TSHROUD[i] = 300 		# tmp[7]	# thermocouple broke for the B0-XX-YY experiments, therefore the temperature is set to a constant 300.C.


every_n = 2
omit_zeroes = 1100
water_filled =  steamTable.rho_pt(20, 192)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/TSHROUD_INST_"+str(experiment), "w") as f:
        print('SR1 INST', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(TIME[every_n*i], file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/FLMV_"+str(experiment), "w") as f:
	print('SR1 q_m_liq', file=f)
	print(str(float(TIME[0]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[1]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[2]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[3]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[4]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[5]))+"\t"+str(0.0)+"kg/s", file=f)
	print(str(float(TIME[6]))+"\t"+str(0.0)+"kg/s", file=f)
	for i in range(0, math.floor(len(TIME))):
		if omit_zeroes < i:
			if (sum(FLMV[0:i]) ) > 5*water_filled/1000:
				print(str(float(TIME[i]))+"\t"+str(FLMV[i])+"kg/s", file=f)
			else:
				print(str(float(TIME[i]))+"\t"+str(0.0)+"kg/s", file=f)
	print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/KWTS_"+str(experiment), "w") as f:
        print('SR1 POWE', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(str(TIME[every_n*i])+"\t"+str(KWTS[every_n*i]*1000/46), file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/KWSHRD_"+str(experiment), "w") as f:
        print('SR1 POWE', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(str(TIME[every_n*i])+"\t"+str(KWSHRD[every_n*i]*1000), file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/PRBTC_"+str(experiment), "w") as f:
        print('SR1 P', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(str(TIME[every_n*i])+"\t"+str(PRBTC[every_n*i]), file=f)
        print('TERM', file=f)


with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/TFLOW_"+str(experiment), "w") as f:
        print('SR1 T_liq', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(str(TIME[every_n*i])+"\t"+str(TFLOW[every_n*i]+273.15), file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/TFSC1_"+str(experiment), "w") as f:
        print('SR1 T_liq', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(str(TIME[every_n*i])+"\t"+str(TFSC1[every_n*i]+273.15), file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/TSHROUD_TIMP_"+str(experiment), "w") as f:
        print('SR1 TIMP', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(TSHROUD[every_n*i]+273.15, file=f)
        print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_"+str(experiment)+"/BC_"+str(experiment)+"/TSHROUD_H_"+str(experiment), "w") as f:
        print('SR1 H', file=f)
        for i in range(0, math.floor(len(TIME)/every_n)):
                print(5.67e-8*(pow(TSHROUD[every_n*i]+273.15,4)-pow(300,4))/(TSHROUD[every_n*i]+273.15-300)+42, file=f)
        print('TERM', file=f)



