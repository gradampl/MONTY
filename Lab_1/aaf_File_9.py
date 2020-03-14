print('Jestem konwerterem temperatury. Jeśli podasz mi temperaturę, np. w stopniach Celsjusza,')
print('policzę, ile to jest w st. Fahrenheita i Kelvina.\n')

degrees = None
fahrenheit = None
kelvin = None
celsius = None

################################## Functions #######################################

def cannot_calculate():
    print('Nie ma tak niskich temperatur.')

def give_degrees():
    degs = input('Podaj liczbę stopni: \n')
    try:
        float(degs)
        return degs
    except ValueError:
            degs = input('Podaj liczbę stopni: \n')
    return float(degs)


def scale_unknown():
    print('Nie znam takiej skali.')

def message(choice):
    if(choice == 'c'):
        print('Temperatura ', degrees, ' stopni Celsjusza')
        print('to ', kelvin, ' stopni w skali Kelvina')
        print('i ', fahrenheit, 'stopni w skali Farenheita.')
    elif(choice == 'f'):
        print('Temperatura ', degrees, ' stopni Farenheita')
        print('to ', kelvin, ' stopni w skali Kelvina')
        print('i ', celsius, 'stopni w skali Celsjusza.')
    else:
        print('Temperatura ', degrees, ' stopni Kelvina')
        print('to ', fahrenheit, ' stopni w skali Farenheita')
        print('i ', celsius, 'stopni w skali Celsjusza.')

###########################################################################

degrees = give_degrees()
scale = input('Podaj skalę (C = Celsjusza, F = Fahrenheita, K = Kelvina) : \n').lower()

while not (scale == 'c' or scale == 'f' or scale == 'k'):
    scale_unknown()
    scale = input('Podaj skalę (C = Celsjusza, F = Fahrenheita, K = Kelvina): \n').lower()

if scale == 'c':
    while degrees < -273.15:
        cannot_calculate()
        degrees = give_degrees()
    fahrenheit = 9 / 5 * degrees + 32
    kelvin = degrees + 273.15
    message('c')

elif scale == 'f':
    while degrees < -459.67:
        cannot_calculate()
        degrees = give_degrees()
    kelvin = 5 / 9 * (degrees - 32) + 273.15
    celsius = 5 / 9 * (degrees - 32)
    message('f')

elif scale == 'k':
    while degrees < 0:
        cannot_calculate()
        degrees = give_degrees()
    fahrenheit = 9 / 5 * (degrees - 273.15) + 32
    celsius = degrees - 273.15
    message('k')