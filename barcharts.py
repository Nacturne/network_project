import pandas as pd
import matplotlib.pyplot as plt
from pprint import pprint



for c in ['AU', 'CA', 'GE', 'India', 'UK']:

    data = pd.DataFrame.from_csv('data/{}/without_ad_block_median.txt'.format(c), sep='\t')
    #data.drop(data.index[[184,343,386, 255]], inplace=True)

    #data.to_csv('data/valid_stats.txt', sep='\t')


    #var_list = ['image_size', 'javascript_size', 'css_size', 'html_size', 'audio_size', 'vedio_size']
    var_list = ['image_number', 'javascript_number', 'css_number', 'html_number', 'audio_number', 'vedio_number']


    for col in var_list:
        data[col] = data[col] / data['total_number'].astype(float)
    plt.figure(c)
    plt.boxplot(data[var_list].as_matrix())
    plt.xticks(range(1,len(var_list)+1), var_list)
    plt.ylabel('Fraction of Object Size')
    plt.ylim([0,1.0])
    plt.title('Distribution for the Fraction of Object Size')
plt.show()