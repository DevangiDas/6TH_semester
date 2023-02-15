import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from unicodedata import normalize

table_MN = pd.read_html('https://en.wikipedia.org/wiki/Minnesota')
print(table_MN)

from numpy import random

x = random.randint(100, size=(3, 5))
y = random.randint(100, size=(3, 5))

print(x)
print(y)

Arr1 = x.transpose()
Arr2 = y.transpose()

print("First Array after transpose")
print(Arr1)

print("Second Array after Transpose")
print(Arr2)

print("Final Array after multiplication")
final_array = (Arr1*Arr2)
print(final_array)