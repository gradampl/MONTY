print('Jestem konwerterem temperatury. Jeśli podasz mi temperaturę, np. w stopniach Celsjusza,')
print('policzę, ile to jest w st. Fahrenheita i Kelvina.\n')

degrees = None
fahrenheit = None
kelvin = None
celsius = None

################################## Functions #######################################

def cannot_calculate():
    print('Nie ma tak niskich temperatur.')


def get_degrees():
    ok = False
    while ok == False:
        degs = input('Podaj liczbę stopni: \n')
        try:
            ok = float(degs)
        except ValueError:
            print('Nie znam takiej liczby.\n')
    return float(degs)


def convert_to_celsius(x):
    if x == 'f':
        celsius = 5 / 9 * (degrees - 32)
    else:
        celsius = degrees - 273.15
    return celsius


def convert_to_fahrenheit(x):
    if x == 'c':
        fahrenheit = 9 / 5 * degrees + 32
    else:
        fahrenheit = 9 / 5 * (degrees - 273.15) + 32
    return fahrenheit


def convert_to_kelvin(x):
    if x == 'c':
        kelvin = degrees + 273.15
    else:
        kelvin = 5 / 9 * (degrees - 32) + 273.15
    return kelvin


def get_scale():
    scale = input('Podaj skalę (C = Celsjusza, F = Fahrenheita, K = Kelvina) : \n').lower()
    return scale


def scale_unknown():
    print('Nie znam takiej skali.')


def message(choice):
    if(choice == 'c'):
        first = 'Celsjusza'
        second = kelvin
        third = 'Kelvina'
        fourth = fahrenheit
        fifth = 'Fahrenheita'
        message_content(first, second, third, fourth, fifth)
    elif (choice == 'f'):
        first = 'Fahrenheita'
        second = celsius
        third = 'Celsjusza'
        fourth = kelvin
        fifth = 'Kelvina'
        message_content(first, second, third, fourth, fifth)
    else:
        first = 'Kelvina'
        second = celsius
        third = 'Celsjusza'
        fourth = fahrenheit
        fifth = 'Fahrenheita'
        message_content(first, second, third, fourth, fifth)


def message_content(first, second, third, fourth, fifth):
    print('Temperatura', "%.2f"%degrees, 'stopni ' + str(first)+',')
    print('to', "%.2f"%second, 'stopni w skali ' + str(third))
    print('i', "%.2f"%fourth, 'stopni w skali ' + str(fifth) + '.')

###########################################################################

degrees = get_degrees()
scale = get_scale()

while not (scale == 'c' or scale == 'f' or scale == 'k'):
    scale_unknown()
    scale = get_scale()

if scale == 'c':
    while degrees < -273.15:
        cannot_calculate()
        degrees = get_degrees()
    fahrenheit = convert_to_fahrenheit('c')
    kelvin = convert_to_kelvin('c')
    message('c')

elif scale == 'f':
    while degrees < -459.67:
        cannot_calculate()
        degrees = get_degrees()
    celsius = convert_to_celsius('f')
    kelvin = convert_to_kelvin('f')
    message('f')

elif scale == 'k':
    while degrees < 0:
        cannot_calculate()
        degrees = get_degrees()
    celsius = convert_to_celsius('k')
    fahrenheit = convert_to_fahrenheit('k')
    message('k')