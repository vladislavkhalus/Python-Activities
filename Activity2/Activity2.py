import math
import pandas as panda
import matplotlib.pyplot as plt

data_field1 = panda.read_csv('sensor.csv')


# Importing the fields to arrays
#signals = data_field1['strenght10']
#time1 = data_field1['time10'] 
x_value = data_field1['ORIENTATIONX']
y_value = data_field1['ORIENTATIONY'] 
a_value = data_field1['LIGHT'] 
z_value = data_field1['ORIENTATIONZ'] 
time = []

#z_value = data_field1[ORIENTATIONZ]

#multiplicationxy = (x_value**2+y_value**2)**(1.0/2)

multiplicationxy = list()
 
for i in range(0,392,1):
    multiplicationxy.append(math.sqrt(math.pow(x_value[i],2) + math.pow(y_value[i],2) )*10) #magnitude * 10

for j in range(0,392,1):
    time.append(j)
    
# Visualizing the data
#plot(X,Y,specifiers)
#plt.plot(time2,speed,'b')
plt.plot( time, multiplicationxy, 'r', label='XY Orientation')
plt.plot( time, a_value, 'b', label='Light')
plt.xlabel('Number of Samples')
plt.ylabel('Light and Orientation') 
# Insert title ('My Title - Speed vs Time') ?? 
# Legend ??? 
plt.title('Orientation of the Phone vs. Light')
plt.legend(loc='upper left')
plt.show()

