from utils.get_stats_main import get_stats_main
from utils.get_stats_others import get_stats_others
import pandas as pd
# ---------------------------------------------------------------
c = 'CH'
block_flag = True
web_number = 30

if block_flag:
    ad = 'with_ad_block'
else:
    ad = 'without_ad_block'



data_results = get_stats_main(folder_in='har_files/{0}/{1}/'.format(c, ad), web_number=web_number, group_number=10)
# data cleaning
data_results.dropna(how='all', inplace=True)
data_results.to_csv('data/{0}/{1}_main.txt'.format(c, ad), sep='\t')


data_results = get_stats_others(folder_in='har_files/{}/{}/'.format(c, ad), web_number=web_number, group_number=10)
# data cleaning
data_results.dropna(how='all', inplace=True)
data_results.to_csv('data/{}/{}_others.txt'.format(c, ad), sep='\t')


# data merge
median_data = pd.DataFrame.from_csv('data/{}/{}_main.txt'.format(c, ad), sep='\t')
red_data = pd.DataFrame.from_csv('data/{}/{}_others.txt'.format(c, ad), sep='\t')
result = pd.merge(median_data, red_data, left_index=True, right_index=True, how='outer')
result.to_csv('data/{}/{}_total.txt'.format(c, ad), sep='\t')