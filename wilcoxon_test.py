'''
from utils.HAR import HAR
from pprint import pprint

har = HAR('httpdata22/0.har')

type_set = set([])

for entry in har.entries:
    type_set.add(entry['response']['content']['mimeType'])

print(type_set)
'''

import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
import numpy as np

c ='total'

df = pd.DataFrame.from_csv('redirections/type_data/{}/without_ad_block_total.txt'.format(c), sep='\t')
df_block = pd.DataFrame.from_csv('data/{}/with_ad_block_total.txt'.format(c), sep='\t')





index_1 = df.index.tolist()
index_2 = df_block.index.tolist()
print(index_1)
print(index_2)

index_list = list(set(index_1).intersection(index_2))

df = df.loc[index_list]
df_block = df_block.loc[index_list]


total_number = df['total_number'] + df['others_app_number'] + df['others_text_number']
total_number_block = df_block['total_number'] + df_block['others_app_number'] + df_block['others_text_number']

total_size = df['total_size'] + df['others_app_size'] + df['others_text_size']
total_size_block = df_block['total_size'] + df_block['others_app_size'] + df_block['others_text_size']



'''
plt.figure('number')
plt.boxplot([total_number,total_number_block] )

plt.figure('size')
plt.boxplot([total_size, total_size_block])
plt.yscale('log')

plt.figure('line')
plt.plot(total_size, total_size_block)
plt.show()
'''


print(total_size[total_size_block < 1])

print(len(total_number.index))
print(len(total_number_block.index))
print('number: {:0.5f}'.format(stats.wilcoxon(total_number, total_number_block)[1]))
print('size:   {:0.5f}'.format(stats.wilcoxon(total_size, total_size_block)[1]))
print(stats.wilcoxon(df_block['load_time'], df['load_time']))

