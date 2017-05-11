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


country_list = ['KR']
#country_list = ['AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']
var = 'load_time'


point_num = 500

for c in country_list:
    fig = plt.figure()
    for ad in ['with_ad_block', 'without_ad_block']:
        data = pd.DataFrame.from_csv('../../data/{}/{}_total.txt'.format(c, ad), sep='\t')

        data = data[var].copy()

        x, y = get_xy(data, point_num)

        plt.plot(x, y, label=ad)
    plt.legend(loc='lower right')
    plt.title('Country: {0} \nCDF for total object {1}'.format(c, var))
    plt.ylabel('Fraction of Websites')
    plt.xlabel('{}'.format(var))

    #fig.savefig('{0}/{1}.png'.format(c, n_s))

    #plt.close()
plt.show()