import os

def locRange(loc, sizeTreshold):
	files = os.listdir(loc)
	for filename in files:
		latMax, lonMax, latMin, lonMin = float('-inf'), float('-inf'), float('inf'), float('inf')

		filename = loc + f'\\{filename}'
		f = open(filename, 'r').read().strip().split('\n')
		if os.path.getsize(filename) > sizeTreshold:
			for fi in f:
				uid, date, lat, lon = fi.split(',')
				lat, lon = float(lat), float(lon)

				latMax = max(latMax, lat)
				lonMax = max(lonMax, lon)
				latMin = min(latMin, lat)
				lonMin = min(lonMin, lon)
	return latMax, lonMax, latMin, lonMin

data = locRange(os.getcwd() + '\\taxi_log_2008_by_id', 10000)

print(data)
