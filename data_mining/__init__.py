import tibber
import numpy as np
import pickle

# Text file with numpy?
x = np.linspace(0, 1, 201)
y = np.random.random(201)
data = np.column_stack((x, y))
header = "X-Column, Y-Column"
np.savetxt('AB_data.txt', data, header=header)

data = np.loadtxt('AB_data.txt')
x = data[:, 0]
y = data[:, 1]

print(x)
print(y)

# pickle
DataPickle = {'Energy' : 'DataEnergy',
              'HP'     : 'DataHP',
              'Weather': 'WeatherLog'}

f = open('data.pkl', "wb")
pickle.dump(DataPickle, f)
f.close()


##############

# Hva slags data trenger jeg?