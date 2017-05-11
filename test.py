import pandas as pd

country_list = ['AU', 'CA', 'CH', 'GE', 'IN', 'JP', 'KR', 'UK', 'US', 'total']
for c in country_list:
    data = pd.DataFrame.from_csv('data/{}/without_ad_block_total.txt'.format(c), sep='\t')
    data = data[['html_number', 'html_size']]
    print(data.corr())


