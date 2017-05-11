import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

data = pd.DataFrame.from_csv('data/valid_stats.txt', sep='\t')


print data[['image_size', 'javascript_size', 'css_size', 'html_size', 'total_size', 'load_time']].corr()

print('-'*30)
print('\n')
print data[['image_number', 'javascript_number', 'css_number', 'html_number', 'total_number', 'server_number', 'service_number', 'load_time']].corr()





'''
for t in ['image_size', 'javascript_size', 'css_size', 'html_size',
          'audio_size', 'vedio_size', 'total_size']:
    plt.figure()
    plt.plot(data.index, data[t]/data['total_size'], label=t)
    plt.legend()

plt.show()


for t in ['image_number', 'javascript_number', 'css_number', 'html_number',
          'audio_number', 'vedio_number', 'total_number']:
    plt.figure()
    plt.plot(data.index, data[t]/data['total_size'], label=t)
    plt.legend()

plt.show()
'''
