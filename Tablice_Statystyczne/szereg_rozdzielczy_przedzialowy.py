import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(123456)
data = np.random.rand(100)
bins = pd.cut(data, 4, precision=2)
freq = bins.value_counts()
relfreq = freq / len(data)

# Wykres słupkowy
# x = np.arange(0, len(freq))
# plt.bar(x, freq)
# plt.xticks(x, freq.index)
# plt.show()

# Wykres kołowy
plt.pie(freq, labels=freq.index)
plt.show()
