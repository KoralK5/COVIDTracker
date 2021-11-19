import pickle, math

def distance(long1, lat1, long2, lat2):
	return math.sqrt((long1-long2)**2 + (lat1-lat2)**2)

def closeness(long1, lat1, long2, lat2, treshold):
    return distance(long1, lat1, long2, lat2) < treshold

f = open('COVIDdata.pkl', 'rb')
data = pickle.load(f)

treshold = 0.0005
close = 0
for key in data:
	values = data[key]
	size = len(values)
	for p1 in range(0, size):
		for p2 in range(p1+1, size):
			long1 = values[p1][1]
			lat1  = values[p1][2]
			long2 = values[p2][1]
			lat2  = values[p2][2]
			close += closeness(long1, lat1, long2, lat2, treshold)
	print(key, close)

