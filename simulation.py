import pickle, math, random, os

def people(loc, sizeTreshold):
	infections = {}
	for filename in os.listdir(loc):
		if os.path.getsize(loc + f'\\{filename}') > sizeTreshold:
			infections[int(filename[:filename.index('.')])] = False
	return infections

def distance(long1, lat1, long2, lat2):
	return math.sqrt((long1-long2)**2 + (lat1-lat2)**2)

def closeness(long1, lat1, long2, lat2, treshold):
    return distance(long1, lat1, long2, lat2) < treshold

f = open('COVIDdata.pkl', 'rb')
data = pickle.load(f)

infections = people(os.getcwd() + '\\taxi_log_2008_by_id', 10000)
initial = 10
for i in range(initial):
	infections[random.choice(list(infections.items()))] = True

treshold = 0.000005
close = 0
for key in data:
	values = data[key]
	size = len(values)
	for p1 in range(0, size):
		for p2 in range(p1+1, size):
			long1, lat1 = values[p1][1], values[p1][2]
			long2, lat2 = values[p2][1], values[p2][2]
			close = closeness(long1, lat1, long2, lat2, treshold)

			if close and (infections[values[p1][0]] or infections[values[p2][0]]):
				infections[p1] = True
				infections[p2] = True
	print(infections)