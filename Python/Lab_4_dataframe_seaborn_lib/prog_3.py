#Show the variability in HP in different types of pokemons using BoxPlot.
#(Visualize using Seaborn)

# Importing the needed libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


df = pd.read_csv("C:/Users/DDas/Downloads/pokemon.csv", index_col = 0)
df.head()

sns.boxplot(x = "HP", data = df)
plt.xticks(fontsize = 4)
plt.title("HP of the Pokemons")