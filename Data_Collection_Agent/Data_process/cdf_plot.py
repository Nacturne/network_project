'''
Created on May 12, 2017

@author: ash
'''
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_xy(data, point_num):
    x = np.linspace(0, max(data), point_num)
    var_size = float(len(data))
    y = []
    for i in x:
        tt=0
        for j in data:
            if j <= i:
                tt+=1                
        frac = tt / var_size
        y.append(frac)

    return (x, y)



c = 'AU'
point_num = 32
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'CA'
point_num = 34
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'CN'
point_num = 30
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'GE'
point_num = 71
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'India'
point_num = 35
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'Japan'
point_num = 30
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'Korea'
point_num = 30
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'UK'
point_num = 37
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)

c = 'US'
point_num = 434
#data = pd.DataFrame.from_csv(, sep='\t')
data = [int(line.rstrip('\r\n')) for line in open('Data/{}/service_number.txt'.format(c))]

x, y = get_xy(data, point_num)

plt.plot(x, y, label=c)


plt.legend(loc='lower right')
plt.ylabel('fraction of websites')
plt.xlabel('Number of origins')
plt.show()
