import pickle

def closeness(long1, lat1, long2, lat2):
    distance = math.sqrt((long1-long2)**2 + (lat1-lat2)**2)
    if distance < 0.5:
        return True
    else:
        return False

with open('taxi_track_by_time.pkl', 'rb') as f:
    data = pickle.load(f)
    f.close()
