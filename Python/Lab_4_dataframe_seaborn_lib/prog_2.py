#List the pokemons from lower generation that can defeat higher generation pokemon? Print both the pokemons with generation.


# Importing the needed libraries.
import pandas as pd


data=pd.read_csv('C:/Users/DDas/Downloads/pokemon.csv')
count=data['Generation'].value_counts()
print(count)

