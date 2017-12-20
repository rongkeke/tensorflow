# _*_ coding: utf-8 _*_
# !/usr/bin/env python
import os
from sklearn.decomposition import PCA
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
pac = PCA(n_components='mle',copy=False)
data = [[ 1.  ,  1.  ],
       [ 0.9 ,  0.95],
       [ 1.01,  1.03],
       [ 2.  ,  2.  ],
       [ 2.03,  2.06],
       [ 1.98,  1.89],
       [ 3.  ,  3.  ],
       [ 3.03,  3.05],
       [ 2.89,  3.1 ],
       [ 4.  ,  4.  ],
       [ 4.06,  4.02],
       [ 3.97,  4.01]]
newdata = pac.fit_transform(data)
print newdata
print pac.n_components
print pac.explained_variance_ratio_
print pac.explained_variance_
print pac.get_params()