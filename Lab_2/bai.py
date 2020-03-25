# https://stackoverflow.com/questions/7001144/range-over-character-in-python
def char_range(c1, c2):
    """Generates the characters from `c1` to `c2`, inclusive."""
    for c in range(ord(c1), ord(c2)+1):
        yield chr(c)


names = []
for i in range(5):
    names.append(input("Podaj nazwisko {0}: \n".format(i+1)))

print()
print('Nazwiska zaczynające się na litery, które w alfabecie występują po literze "P":')
print()
for i in names:
    if i[0].lower() in char_range('q','ż'):
        print(i)

print()
print('Nazwiska, które mają więcej niż 6 liter:')
print()
for i in names:
    if len(i)>6:
        print(i)