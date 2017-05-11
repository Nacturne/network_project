import pandas as pd
import matplotlib.pyplot as plt



var = 'loadtime'
country_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']

data_list = []

for c in country_list:
    data = pd.read_csv('../Data/{}/origin_fraction.txt'.format(c),
                     names=['byte', 'objetc_number', 'loadtime'],
                     )

    data_list.append(data[var].dropna().copy())


data = pd.DataFrame.from_csv('../Data/total/origin_fraction.txt', sep='\t')
data_list.append(data[var].dropna().copy())
country_list.append('total')



plt.boxplot(data_list)
plt.xticks(range(1,len(country_list)+1), country_list)
plt.xlabel('Country')
plt.ylabel('Fraction of non-original {}'.format(var))
plt.title('Box Plot for Fraction of non-original {}'.format(var))
plt.ylim([0,1.0])
plt.show()