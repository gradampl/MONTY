import inline as inline
import matplotlib
import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("muzea.xlsx")
print(data.head())

# SZEREG ROZDZIELCZY

type = data["Region"]

freq = type.value_counts()
print(freq)

# Wykres słupkowy
x = np.arange(0, len(freq))
plt.bar(x, freq)
plt.xticks(x, freq.index, rotation=90)
plt.title("Liczba województw w danym regionie")
plt.show()

# Wykres kołowy
plt.pie(freq, labels=freq.index)
plt.title("Liczba województw w danym regionie")
plt.show()

# Przygotowanie danych do analizy ststystycznej

lzm = data["Liczba_zwiedzajacych"]
rzw = data["rozwody"]
sep = data["separacje"]
ukr = data["uklad_krazenia"]
ntw = data["nowotwory"]
uod = data["uklad_oddech"]
sbj = data["samoboj_na_10tys"]
lm = data["ile_mieszkancow"]

# Średnia i odch. standrdowe 2 zmiennych:

print('Liczba ludności w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(lm), np.std(lm)))
print('Liczba zwiedzających muzea w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(lzm), np.std(lzm)))

# KORELACJA (r-Pearsona)

# Czy liczba zwiedzających muzea w poszczególnych województwach
# jest skorelowana z liczbą mieszkańców?

from scipy.stats import pearsonr

corr, _ = pearsonr(lzm, lm)
print(corr)

# Wykres ilustrujący ten związek

plt.scatter(lzm, lm)
plt.title("Związek między liczbą mieszkańców województwa"
          " a liczbą zwiedzających muzea")
plt.show()

# Czy liczba samobójstw w poszczególnych województwach
# jest skorelowana z liczbą rozwodów?

print('Liczba samobójstw na 10000 mieszkańców'
      ' w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(sbj), np.std(sbj)))

print('Liczba rozwodów w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(rzw), np.std(rzw)))

corr, _ = pearsonr(sbj, rzw)
print(corr)

# Wykres ilustrujący ten związek

plt.scatter(sbj, rzw)
plt.title("Związek między liczbą rozwodów"
          " a liczbą samobójstw")
plt.show()

# Czy liczba rozwodów w poszczególnych województwach
# jest skorelowana z liczbą separacji?

print('Liczba separacji w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(sep), np.std(sep)))
print('Liczba rozwodów w poszcz. wojewodztwach: średnia = %.2f,'
      ' odch. standardowe = %.2f' % (np.mean(rzw), np.std(rzw)))

corr, _ = pearsonr(sep, rzw)
print(corr)

# Wykres ilustrujący ten związek

plt.scatter(sep, rzw)
plt.title("Związek między liczbą rozwodów"
          " a liczbą separacji")
plt.show()

# REGRESJA LINIOWA

# W jakim stopniu takie czynniki, jak liczba zgonów
# (z powodu róznych rodzajów chorób oraz na skutek
# samobójstwa) oraz separacje i rozwody wpływają
# na liczbę mieszkańców.

import seaborn as seabornInstance
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn import metrics

# %matplotlib inline

# Podział danych na (potencjalne) wyznaczniki (X) oraz zmienną przewidywaną (y)

X = data[['uklad_krazenia', 'nowotwory', 'uklad_oddech',
          'samoboj_na_10tys', 'rozwody', 'separacje']].values
y = data['ile_mieszkancow'].values

# Jaki rozkład ma zmienna y:

plt.figure(figsize=(15, 10))
plt.tight_layout()
plt.title('Rozkład zmiennej "Liczba mieszkańców"')
seabornInstance.distplot(lm)

# Dane rozdzielamy na zestaw treningowy (80%) i testowy (20%)

X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.2, random_state=0)

# Model poddajemy treningowi:

regressor = LinearRegression()
regressor.fit(X_train, y_train)

# Współczynniki regresji ustalone przez model:

# coeff_df = pd.DataFrame(regressor.coef_, X.columns, X=['Coefficient'])
# coeff_df

# Ten kod niestety nie działa, jeszcze nie wiem, dlaczego.


# Model dokonuje predykcji:

y_pred = regressor.predict(X_test)

# Porównujemy wartości faktyczne i przewidywane przez model

df = pd.DataFrame({'Faktyczny': y_test, 'Przewidywany': y_pred})
df1 = df.head(6)
df1.plot(kind='bar', figsize=(12, 10))
plt.grid(which='major', linestyle='-', linewidth='0.5', color='green')
plt.grid(which='minor', linestyle=':', linewidth='0.5', color='black')
plt.xticks(x, rotation=0)
plt.title("Liczba mieszkańców: faktyczna i przewidywana na podstawie wybranych zmiennych")
plt.show()
