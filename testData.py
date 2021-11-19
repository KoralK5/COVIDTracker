import pickle

f = open('COVIDdata.pkl', 'rb')
data = pickle.load(f)
print(data)
