import scipy.io
import pandas as pd
import numpy as np
import math

annots = scipy.io.loadmat('B0-20-17.mat')
con_list = [[element for element in upperElement] for upperElement in annots['A']]
mat = np.array(con_list)
INST = np.copy(mat[:,0])
TIMP = np.copy(mat[:,1])

TIMP = np.ones(len(TIMP))

TIMP = 300*TIMP 


every_n = 2

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_B0-20-17/BC_B0-20-17/TSHROUD_TIMP_B0-20-17", "w") as f:
	print('SR1 TIMP', file=f)
	for i in range(0, math.floor(len(TIMP)/every_n)):
		print(TIMP[every_n*i]+273.15, file=f)
	print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_B0-20-17/BC_B0-20-17/TSHROUD_INST_B0-20-17", "w") as f:
	print('SR1 INST', file=f)
	for i in range(0, math.floor(len(TIMP)/every_n)):
		print(INST[every_n*i], file=f)
	print('TERM', file=f)

with open("/home/andreastatidis/DRACCAR/input_cards/test_cases/dir_B0-20-17/BC_B0-20-17/TSHROUD_H_B0-20-17", "w") as f:
	print('SR1 H', file=f)
	for i in range(0, math.floor(len(TIMP)/every_n)):
		print(5.67e-8*(pow(TIMP[every_n*i]+273.15,4)-pow(300,4))/(TIMP[every_n*i]+273.15-300), file=f)
	print('TERM', file=f)

