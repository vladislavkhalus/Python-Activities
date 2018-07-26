import math
import pandas as panda
import matplotlib.pyplot as plt

data_field1 = panda.read_csv('sensor.csv')
x_value = data_field1['ORIENTATIONX']
y_value = data_field1['ORIENTATIONY']
a_value = data_field1['LIGHT']
z_value = data_field1['ORIENTATIONZ']
time = []
multiplicationxy = list()
for i in range(0, 392, 1):
    multiplicationxy.append(math.sqrt(math.pow(x_value[i], 2) +
                            math.pow(y_value[i], 2))*10)
for j in range(0, 392, 1):
    time.append(j)
plt.plot(time, multiplicationxy, 'r', label='XY Orientation')
plt.plot(time, a_value, 'b', label='Light')
plt.xlabel('Number of Samples')
plt.ylabel('Light and Orientation')
plt.title('Orientation of the Phone vs. Light')
plt.legend(loc='upper left')
plt.show()



