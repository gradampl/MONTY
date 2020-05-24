import xlrd
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = pd.read_excel("szkoly.xlsx")
print(data.head())

# Result:
#
# ys.path.extend(['E:\\Adam\\Studia\\MAGISTERSKIE\\Semestr_1\\PYTHON\\MONTY\\Tablice_Statystyczne', 'E:/Adam/Studia/MAGISTERSKIE/Semestr_1/PYTHON/MONTY/Tablice_Statystyczne'])
# PyDev console: starting.
# Python 3.7.6 (tags/v3.7.6:43364a7ae0, Dec 19 2019, 00:42:30) [MSC v.1916 64 bit (AMD64)] on win32
# runfile('E:/Adam/Studia/MAGISTERSKIE/Semestr_1/PYTHON/MONTY/Tablice_Statystyczne/szereg_szczegolowy.py', wdir='E:/Adam/Studia/MAGISTERSKIE/Semestr_1/PYTHON/MONTY/Tablice_Statystyczne')
#                        Nazwa  Liczba uczniów          Typ
# 0  Przedszkole Miejskie nr 1             125  przedszkole
# 1  Przedszkole Miejskie nr 2              75  przedszkole
# 2  Przedszkole Miejskie nr 3              66  przedszkole
# 3  Przedszkole Miejskie nr 4             100  przedszkole
# 4  Przedszkole Miejskie nr 5             174  przedszkole

