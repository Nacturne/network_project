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


country_list = ['AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US', 'total']
point_num = 500

for c in country_list:
    for n_s in ['number', 'size']:

        fig = plt.figure()
        for ad in ['with_ad_block', 'without_ad_block']:
            data = pd.DataFrame.from_csv('../../data/{}/{}_total.txt'.format(c, ad), sep='\t')

            if n_s == 'number':
                data = data['total_number'] + data['others_app_number'] + data['others_text_number']
            elif n_s == 'size':
                data = data['total_size'] + data['others_app_size'] + data['others_text_size']
                data = data/(1024)

            x, y = get_xy(data, point_num)

            plt.plot(x, y, label=ad)
        plt.legend(loc='lower right')
        plt.title('Country: {0} \nCDF for total object {1}'.format(c, n_s))
        plt.ylabel('Fraction of Websites')
        plt.xlabel('Total Object {}'.format(n_s.upper()))

        fig.savefig('{0}/{1}.png'.format(c, n_s))

        plt.close()
