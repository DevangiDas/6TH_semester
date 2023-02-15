#What is the count of pokemon per generation? (Visualize using Seaborn)

# Importing the needed libraries.
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("C:/Users/DDas/Downloads/pokemon.csv", index_col = 0)
df.head()
sns.lineplot(data = df["Generation"])
plt.title("Line plot for different generation")
plt.xlabel("Count")
