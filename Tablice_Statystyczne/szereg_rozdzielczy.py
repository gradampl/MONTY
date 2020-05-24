import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("szkoly.xlsx")
# print(data.head())

type = data["Typ"]
freq = type.value_counts()
# print(freq)

relfreq= freq/len(type)
# print(relfreq)

# Wykres słupkowy
# x=np.arange(0,len(freq))
# plt.bar(x,freq)
# plt.xticks(x,freq.index, rotation=90)
# plt.title("Liczebność typów szkół w Olsztynie w r.szk. 2016/2017")
# plt.show()

# Wykres kołowy
plt.pie(freq, labels=freq.index)
plt.title("Liczebność typów szkół w Olsztynie w r.szk. 2016/2017")
plt.show()