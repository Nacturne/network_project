import pandas as pd
import matplotlib.pyplot as plt



status = '303'
country_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']

data_list = []

for c in country_list:
    data = pd.read_csv('../Data/{}/redirect_code.txt'.format(c),
                       names=['301', '302', '303', '307'],
                       index_col=0)

    data_list.append(data[status].copy())



data = pd.DataFrame.from_csv('../Data/total/redirect_code.txt', sep='\t')
data_list.append(data[status].copy())
country_list.append('total')



plt.boxplot(data_list)
plt.xticks(range(1,len(country_list)+1), country_list)
plt.xlabel('Country')
plt.ylabel('Fraction of {} Redirections'.format(status))
plt.title('Box Plot for Fraction of {} Redirection Records'.format(status))
plt.ylim([0,1.0])
plt.show()