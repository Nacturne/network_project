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


#country_list = ['CH', 'KR']
#country_list = ['AU', 'CA', 'GE', 'IN', 'JP']
country_list = ['UK', 'US']
var = 'red_number_frac'


point_num = 500


for c in country_list:
    data = pd.read_csv('../Data/{}/redirect.txt'.format(c), names=['red_number_frac', 'red_time_frac'], index_col=0)

    data = data[var].copy()

    x, y = get_xy(data, point_num)

    plt.plot(x, y, label=c)


    plt.legend(loc='lower right')
    plt.title('CDF for redirection')
    plt.ylabel('Fraction of Websites')
    plt.xlabel('{}'.format(var))

    #fig.savefig('{0}/{1}.png'.format(c, n_s))

    #plt.close()
plt.show()