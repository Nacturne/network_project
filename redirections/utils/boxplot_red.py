import pandas as pd
import matplotlib.pyplot as plt

country_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']

data_list = []

for c in country_list:
    data = pd.read_csv('../Data/{}/redirect_ad.txt'.format(c),
                       names=['red_number_frac', 'red_time_frac'],
                       index_col=0)

    data_list.append(data['red_number_frac'].copy())

data = pd.DataFrame.from_csv('../Data/total/red_ad_block.txt', sep='\t')
data_list.append(data['red_number_frac'].copy())
country_list.append('total')



plt.boxplot(data_list)
plt.xticks(range(1,len(country_list)+1), country_list)
plt.xlabel('Country')
plt.ylabel('Fraction of Redirection Records')
plt.title('Box Plot for Fraction of Redirection Records\nwith_ad_block')
plt.show()