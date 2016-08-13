#! /usr/bin/env python

import numpy as np
from scipy import stats

prop = [.08]
prop_hat = .12
n = 125

#z_score_prop = stats.zscore(prop)
#print(z_score_prop)

t_score_prop = stats.ttest_1samp(prop, prop_hat)
print(t_score_prop)

