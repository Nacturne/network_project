import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
import pandas as pd

data = pd.DataFrame.from_csv('data/valid_stats.txt', sep='\t')
data = data[data['load_time'] < 40]

drop_quantile = 0.05
low_bound = data.quantile(drop_quantile)
high_bound = data.quantile(1-drop_quantile)

'''
for item in ['image_number', 'javascript_number', 'css_number', 'html_number', 'total_number']:
    data = data[(data[item] > low_bound[item]) & (data[item] < high_bound[item])]

Y = data.index.tolist()
X = np.column_stack((data['image_number'],
                     data['javascript_number'],
                     data['css_number'],
                     data['html_number'],
                     data['total_number']))
'''

for item in ['image_size', 'javascript_size', 'css_size', 'html_size', 'total_size']:
    data = data[(data[item] > low_bound[item]) & (data[item] < high_bound[item])]

for item in ['image_number', 'javascript_number', 'css_number', 'html_number', 'total_number']:
    data = data[(data[item] > low_bound[item]) & (data[item] < high_bound[item])]




Y = data['load_time_std']


X = np.column_stack((data['image_size'],
                     data['javascript_size'],
                     data['css_size'],
                     data['html_size'],
                     data['total_size'],
                     data['image_number'],
                     data['javascript_number'],
                     data['css_number'],
                     data['html_number'],
                     data['total_number'],
                     ))

'''

X = np.column_stack((data['html_number'],
                     data['image_number'],
                     data['javascript_size'],
                     data['server_number']
                     ))
'''

X = sm.add_constant(X)
model = sm.OLS(Y, X)
results = model.fit()
print(results.summary())



'''
plt.plot(x, Y, 'r.')
plt.plot(x, results.fittedvalues, 'b--')
plt.show()
'''



