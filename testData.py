import pickle

f = open('COVIDdata.pkl', 'rb')
data = pickle.load(f)
print(data)

def closeness(long1, lat1, long2, lat2):
    distance = math.sqrt((long1-long2)**2 + (lat1-lat2)**2)
    if distance < 0.5:
        return True
    else:
        return False
