#!/usr/bin/env python
# Test script for the Seaborn tips dataset visualization
import seaborn as sns
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

tips = sns.load_dataset('tips')
sns.regplot(x='total_bill',y='tip',data=tips)

model = smf.ols('tip ~ total_bill',data=tips)
results = model.fit()
print(results.summary())
