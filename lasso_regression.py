import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import scale
from sklearn import cross_validation
from sklearn.linear_model import Ridge, RidgeCV, Lasso, LassoCV
from sklearn.metrics import mean_squared_error


c = 'total'
df = pd.DataFrame.from_csv('redirections/type_data/{}/with_ad_block_total.txt'.format(c), sep='\t')
#df = df[df['load_time_std']<1000]




vars=['html_number', 'html_size',
      'image_number', 'image_size',
      'javascript_number',
      'red_number_frac_x',
      'server_number']

y = df['load_time']
X = df[vars]

alphas = 10**np.linspace(-5, 5, 100)


lasso = Lasso(max_iter=10000, normalize=True)
coefs = []
for a in alphas:
    lasso.set_params(alpha=a)
    lasso.fit(scale(X), y)
    coefs.append(lasso.coef_)

    print('Alpha: {0:.5f}   R^2: {1:.3f}'.format(a, lasso.score(scale(X), y)))

coefs = np.asarray(coefs)
row, col = coefs.shape



markers = ['.', ',', 'o', 'v', '^', '1', '2', '3', '4', 's', 'p', 'P', '*', 'h', 'x', '1', 'D']

for i, marker, label in zip(range(col), markers, vars):
    plt.plot(alphas, coefs[:,i], marker=marker[:col], label=label)
    plt.axis('tight')
    plt.xlabel('alpha')
    plt.ylabel('weights')
    plt.xscale('log')
    plt.legend()

plt.title('LASSO results for Page Loading Time\n{} (with_ad_block)'.format(c))
plt.show()




