string1 = "Hans"
string2 = "Kloss"
number1 = 0.9874
number2 = 12.307
number3 = 79870234

print('Jestem {}, {} {}.'.format(string2,string1,string2))
# Result: Jestem Kloss, Hans Kloss.

print('Jestem {1}, {0} {1}.'.format(string1,string2))
# Result: Jestem Kloss, Hans Kloss.
print()

print('{0:.5f}, {1:20f}, {2:20d}'.format(number1,number2,number3))
# Result: 0.98740,            12.307000,             79870234

print()

print('Ależ {0}, krzyknął agent {1:.2f}, {2:.2f} to człowiek Brunera!'.format(string1,number1,number2))
# Result: Ależ Hans, krzyknął agent 0.99, 12.31 to człowiek Brunera!

print()

suma = number1+number2+number3
for i in range(5):
    suma += 1
    print('{0:.{4}f} + {1:.{4}f} + {2:{4}d} + 1 = {3:.{4}f}'.format(number1,number2,number3,suma,i))

# Result:
# 1 + 12 + 79870234 + 1 = 79870248
# 1.0 + 12.3 + 79870234 + 1 = 79870249.3
# 0.99 + 12.31 + 79870234 + 1 = 79870250.29
# 0.987 + 12.307 + 79870234 + 1 = 79870251.294
# 0.9874 + 12.3070 + 79870234 + 1 = 79870252.2944
