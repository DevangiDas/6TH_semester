#Which pokemon in the 4th generation can defeat Legendary Pokemon of higher generation.

import pandas as pd


df = pd.read_csv("C:/Users/DDas/Downloads/pokemon.csv")
df.head()

for index, row in df.iterrows():
    for ind, r in df.iterrows():
        if row['Generation'] == 4 and r['Legendary'] == True and row['Total'] > r['Total']:
            if row['Generation'] < r['Generation']:
                print(index," ",row['Name'],"-",row['Total'],"     ",r['Name'],"-",r['Total'])