#Which type has the easiest pokemon to catch?

import pandas as pd
import seaborn as sns
data = data[['speed','tottal','HP','Attack']]
corr = data.corr()
print(data.corr())
seaborn.heatmap(corr)
