import pickle
import random
import os
from math import sqrt

def people(loc, sizeTreshold):
	people = {}
	for filename in os.listdir(loc):
		if os.path.getsize(loc + f'\\{filename}') > sizeTreshold:
			f = open(loc + f'\\{filename}', 'r').read().strip()
			f = f[:f.index('\n')]
			uid, date, lat, lon = f.split(',')
			people[int(filename[:filename.index('.')])] = [False, float(lat), float(lon)]
	return people

def distance(long1, lat1, long2, lat2):
	return sqrt((long1-long2)**2 + (lat1-lat2)**2)

def store(folder, data, time):
	f = open(f'{folder}\\{time.replace(":", " ")}.pkl', 'wb')
	pickle.dump(data, f)
	f.close()

print('Formatting Data...\n')
f = open('COVIDdata.pkl', 'rb')
data = pickle.load(f)
data = {i:data[i] for i in sorted(data)}

print('Initializing Infections...\n')
people = people(os.getcwd() + '\\taxi_log_2008_by_id', 10000)
infections = 10
for i in range(infections):
	people[random.choice(list(people.keys()))][0] = True

dataFolder = os.getcwd() + '\\chanceSpreadData'

print('Starting Simulation...\n')
treshold = 0.00005
for time in data:
	for p1 in data[time]:
		long1, lat1 = p1[1], p1[2]
		people[p1[0]][1] = long1
		people[p1[0]][2] = lat1

		for p2 in people:
			if (p1[0] != p2) and (people[p1[0]][0] ^ people[p2][0]) and (random.random() < 0.3):
				long2, lat2 = people[p2][1], people[p2][2]
				dist = distance(long1, lat1, long2, lat2)

				if dist < treshold:
					people[p1[0]][0] = True
					people[p2][0] = True
					infections += 1
	store(dataFolder, people, time)
	print(f'{time}: {infections} infections')
