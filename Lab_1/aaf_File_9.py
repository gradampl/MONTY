################################## Functions #######################################
def greeting():
    print('Jestem konwerterem temperatury. Jeśli podasz mi temperaturę, np. w stopniach Celsjusza,')
    print('policzę, ile to jest w st. Fahrenheita i Kelvina.\n')
    get_scale()



def cannot_calculate():
    print('Nie ma tak niskich temperatur.')



def give_scale():
    print('Podaj skalę (C = Celsjusza, F = Fahrenheita, K = Kelvina) : \n')



def get_degrees():
    ok = False
    while ok == False:
        degs = input('Podaj liczbę stopni: \n')
        try:
            ok = float(degs)
        except ValueError:
            print('Nie znam takiej liczby.\n')
    return float(degs)




def get_scale():
    give_scale()
    scale = input().lower()
    while not (scale == 'c' or scale == 'f' or scale == 'k'):
        scale_unknown()
        scale = input().lower()
    prepare_to_convert(scale)



def prepare_to_convert(scale):
    degrees = get_degrees()
    if scale == 'c':
        while degrees < -273.15:
            cannot_calculate()
            degrees = get_degrees()
        fahrenheit = convert_to_fahrenheit('c', degrees)
        kelvin = convert_to_kelvin('c', degrees)
        message('c', degrees, fahrenheit, kelvin)

    elif scale == 'f':
        while degrees < -459.67:
            cannot_calculate()
            degrees = get_degrees()
        celsius = convert_to_celsius('f', degrees)
        kelvin = convert_to_kelvin('f', degrees)
        message('f', degrees, celsius, kelvin)

    elif scale == 'k':
        while degrees < 0:
            cannot_calculate()
            degrees = get_degrees()
        celsius = convert_to_celsius('k', degrees)
        fahrenheit = convert_to_fahrenheit('k', degrees)
        message('k', degrees, celsius, fahrenheit)




def convert_to_celsius(x, degs):
    degrees = degs
    if x == 'f':
        celsius = 5 / 9 * (degrees - 32)
    else:
        celsius = degrees - 273.15
    return celsius




def convert_to_fahrenheit(x, degs):
    degrees = degs
    if x == 'c':
        fahrenheit = 9 / 5 * degrees + 32
    else:
        fahrenheit = 9 / 5 * (degrees - 273.15) + 32
    return fahrenheit




def convert_to_kelvin(x, degs):
    degrees = degs
    if x == 'c':
        kelvin = degrees + 273.15
    else:
        kelvin = 5 / 9 * (degrees - 32) + 273.15
    return kelvin




def scale_unknown():
    print('Nie znam takiej skali.')




def message(choice, degrees, scale1, scale2):
    degs = degrees
    second = scale1
    fourth = scale2
    if(choice == 'c'):
        first = 'Celsjusza'
        third = 'Fahrenheita'
        fifth = 'Kelvina'
    elif (choice == 'f'):
        first = 'Fahrenheita'
        third = 'Celsjusza'
        fifth = 'Kelvina'
    else:
        first = 'Kelvina'
        third = 'Celsjusza'
        fifth = 'Fahrenheita'
    message_content(degs, first, second, third, fourth, fifth)


def message_content(degrees, first, second, third, fourth, fifth):
    print('Temperatura', "%.2f"% degrees, 'stopni ' + str(first)+',')
    print('to', "%.2f"%second, 'stopni w skali ' + str(third))
    print('i', "%.2f"%fourth, 'stopni w skali ' + str(fifth) + '.')

###########################################################################

greeting()
