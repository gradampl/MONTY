str = "To jest dosyć pospolity, ale za to bardzo długi string."

# wydruk znakow o parzystych indeksach
i = 1
while i < len(str):
    if i%2==0:
        print(str[i],end='')
    i += 1
print()


# wydruk 3 ostatnich znakow
print(str[len(str)-3:])

# wydruk znaku o indeksie 12
print(str[12])

# operacje arytmetyczne
print(str * 2)
# print(str / 2)
# print(str // 2)
# print(str ** 2)
# print(str + 2)
print(str + " 2")