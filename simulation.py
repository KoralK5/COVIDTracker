import pickle
import random
import os
import pandas as pd
import numpy as np

def people(loc, sizeTreshold):
	people = {}
	for filename in os.listdir(loc):
		if os.path.getsize(loc + f'\\{filename}') > sizeTreshold:
			f = open(loc + f'\\{filename}', 'r').read().strip()
			f = f[:f.index('\n')]
			uid, date, lon, lat = f.split(',')
			people[int(filename[:filename.index('.')])] = [False, float(lon), float(lat)]
	return people

def store(folder, data, time):
	with open(f'{folder}\\{time.replace(":", " ")}.pkl', 'wb') as f:
		pickle.dump(data, f)
		f.close()

print('Formatting Data...\n')
with open('COVIDdata2.pkl', 'rb') as f:
	df = pickle.load(f).sort_index(axis = 0)
	df.ffill(inplace = True)
	f.close()

with open('allInteractions.pkl', 'rb') as f:
	dfTime = pickle.load(f).sort_index(axis = 0)
	f.close()

#print(df)

print('Initializing Infections...\n')
df = df.T
people = df.to_dict()
for key in people:
	for k in people[key]:
		appList = list(people[key][k])
		appList.append(False)
		#print(appList)
		people[key][k] = appList
		#print(people[key])

infections = 10
for i in range(infections):
	people['2008-02-02 13:30'][random.randint(0, 3000)][2] = True

dataFolder = os.getcwd() + '\\spreadData'

print('Starting Simulation...\n')
#treshold = 0.00005

dfTime = dfTime.T

for i in range(len(dfTime.columns.values.tolist())):
	time = dfTime.columns[i]
	iIdx = np.where(dfTime.iloc[:, i] != False & dfTime.iloc[:, i].eq(dfTime.iloc[:, i].shift(axis = 'index')), dfTime.iloc[:, i], False)
	print(iIdx)

	for j in range(len(iIdx)):
		if people[time][j][2] and iIdx[j] != False:
			people[time][j][2] = True
			people[time][iIdx[j]][2] = True
			infections += 1
	
	store(dataFolder, people[time], time)
	print(f'{time}: {infections} infections')
