digits = {'0':'zero', '1': 'jeden', '2': 'dwa', '3': 'trzy', '4': 'cztery', '5': 'pięć',\
          '6': 'sześć', '7': 'siedem', '8': 'osiem', '9': 'dziewięć'}

user_input = input("Wpisz cyfry, a ja zamienię je na słowa: \n")

for i in range(len(user_input)):
    if user_input[i] not in '0123456789':
        continue
    else:
        print(digits[user_input[i]],end=' ')
