import os, time, pickle

def formatData(loc, sizeTreshold):
	files = os.listdir(loc)
	data = {}
	i = 0
	for filename in files:
		i += 1
		print(i)
		filename = loc + f'\\{filename}'
		if os.path.getsize(filename) > sizeTreshold:
			f = open(filename, 'r').read().strip().split('\n')
			for fi in f:
				uid, date, lat, lon = fi.split(',')
				uid, date, lat, lon = int(uid), time.strftime(date[:-3]), float(lat), float(lon)

				if date not in data:
					data[date] = [(uid, lat, lon)]
				else:
					data[date].append((uid, lat, lon))
	return data

data = formatData(os.getcwd() + '\\taxi_log_2008_by_id', 10000)

f = open('COVIDdata.pkl', 'wb')
pickle.dump(data, f)
f.close()
