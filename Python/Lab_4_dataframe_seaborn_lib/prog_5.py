#How many types of
#pokemon are there in each generation? 
#(Visualize using Seaborn)

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

sns.catplot(
    x='Generation',
    data=pd.read_csv("C:/Users/DDas/Downloads/pokemon.csv"),
    col='Type 1',
    kind='count',
    col_wrap=3
).set_axis_labels('Generation', '# of Pokemon');
plt.show()