import pandas as pd
import matplotlib.pyplot as plt



var_list = [ 'AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US']

data_list = []

data = pd.DataFrame.from_csv('../Data/total/origin_content.txt', sep='\t')

for var in data.columns:
    data_list.append(data[var].dropna().copy())



plt.boxplot(data_list)
plt.xticks(range(1,len(data.columns)+1), data.columns.tolist())
plt.xlabel('MIME-type')
plt.ylabel('Fraction of non-original contents')
plt.title('Box Plot for Fraction of non-original contents')
plt.ylim([0,1.0])
plt.show()