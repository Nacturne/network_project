import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

c = 'US'
data_block = pd.DataFrame.from_csv('../../data/{}/with_ad_block_total.txt'.format(c), sep='\t')
data = pd.DataFrame.from_csv('../../data/{}/without_ad_block_total.txt'.format(c), sep='\t')


index_1 = data.index.tolist()
index_2 = data_block.index.tolist()
print(index_1)
print(index_2)

if len(index_1) > index_2:
    index_list = index_2
else:
    index_list = index_1

data = data.loc[index_list]
data_block = data_block.loc[index_list]



total_number = data['total_number'] + data['others_app_number'] + data['others_text_number']
total_number_block = data_block['total_number'] + data_block['others_app_number'] + data_block['others_text_number']

plt.figure()
diff_number = total_number - total_number_block
plt.plot(diff_number, marker='.', linestyle='')


total_size = data['total_size'] + data['others_app_size'] + data['others_text_size']
total_size_block = data_block['total_size'] + data_block['others_app_size'] + data_block['others_text_size']
plt.figure()
diff_size = total_size - total_size_block
plt.plot(diff_size, marker='.', linestyle='')

plt.show()

print(len(diff_size))
print(len(data['load_time']))


print(np.corrcoef(diff_number, data['load_time'] - data_block['load_time']))
print(np.corrcoef(diff_size, data['load_time'] - data_block['load_time']))