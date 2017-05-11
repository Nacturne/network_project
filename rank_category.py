import pandas as pd
import matplotlib.pylab as plt
import numpy as np

data = pd.DataFrame.from_csv('data/stats_new.txt', sep='\t')

group_size = 50

average_dict = {'image_size': [],
                 'javascript_size': [],
                 'css_size': [],
                 'html_size': [],
                 'audio_size': [],
                 'vedio_size': [],
                 'total_size': [],
                 'image_number': [],
                 'javascript_number': [],
                 'css_number': [],
                 'html_number': [],
                 'audio_number': [],
                 'vedio_number': [],
                 'total_number': []}

for i in range(0, len(data), group_size):
    for col in data.columns.tolist():
        mean = data[i:i + group_size][col].median()
        average_dict[col].append(mean)



plt.figure()
for col in ['image_number', 'javascript_number', 'css_number', 'html_number', 'total_number']:
    plt.plot(average_dict[col], marker='*', label=col)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.xlabel('Popularity Level')
    plt.ylabel('Mean of Object Number')


plt.figure()
for col in ['image_size', 'javascript_size', 'css_size', 'html_size', 'total_size']:
    plt.plot(average_dict[col], marker='*', label=col)
    plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc=3, ncol=2, mode="expand", borderaxespad=0.)
    plt.title('')
    plt.xlabel('Popularity Level')
    plt.ylabel('Mean of Object Size')

plt.show()



