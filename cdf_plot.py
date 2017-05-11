import pandas as pd
import matplotlib.pyplot as plt
import numpy as np


def get_xy(data, point_num):
    x = np.linspace(0, data.max(), point_num)
    var_size = float(data.size)
    y = []
    for i in x:
        frac = data[data <= i].size / var_size
        y.append(frac)

    return (x, y)



c = 'US'
point_num = 500

var = 'load_time'


for ad in ['with_ad_block', 'without_ad_block']:
    data = pd.DataFrame.from_csv('data/{}/{}_total.txt'.format(c, ad), sep='\t')


    data = data[var].copy()
    #data = data['total_number'] + data['others_app_number'] + data['others_text_number']
    #data = data['total_size'] + data['others_app_size'] + data['others_text_size']

    x, y = get_xy(data, point_num)

    plt.plot(x, y, label=ad)
plt.legend(loc='lower right')
plt.ylabel('fraction of websites')
plt.xlabel('load time')
plt.show()
