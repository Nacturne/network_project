import matplotlib.pyplot as plt
import pandas as pd


data = pd.DataFrame.from_csv('data/total.txt', sep='\t')
data = data[data['load_time'] < 40]
data = data[data['red_count_total'] <200]

plt.plot(data['load_time'], data['count_302'], marker='.', linestyle='')
plt.plot(range(10), range(10), linestyle='-')
plt.show()

print(data[['load_time', 'count_302']].corr())