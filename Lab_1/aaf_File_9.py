print('Jestem konwerterem temperatury. Jeśli podasz mi temperaturę, np. w stopniach Celsjusza,')
print('policzę, ile to jest w st. Fahrenheita i Kelvina.\n')
degrees = float(input('Podaj liczbę stopni: \n'))

fahrenheit = 0.0
kelvin = 0.0
celsjusz = 0.0

scale = input('Podaj skalę (C = Celsjusza, F = Fahrenheita, K = Kelvina: \n').lower()
if scale == 'c':
    fahrenheit = 9/5 * degrees + 32
    if degrees >= -273.15:
        kelvin = degrees + 273.15
    else:
        while degrees < -273.15:
            print('Nie mogę przeliczyć tak niskiej temperatury na stopnie Kelvina.')
            degrees = float(input('Podaj liczbę stopni: \n'))
    print('Temperatura ', degrees, ' stopni Celsjusza')
    print('to ', fahrenheit, ' stopni w skali Farenheita')
    print('i ',kelvin, 'stopni w skali Kelvina.')
elif scale == 'k' and degrees>=0:
    fahrenheit = 9/5 * (degrees - 273.15) + 32
    celsjusz = degrees - 273.15
    print('Temperatura ', degrees, ' stopni Kelvina')
    print('to ', fahrenheit, ' stopni w skali Farenheita')
    print('i ', celsjusz, 'stopni w skali Celsjusza.')
    if degrees < 0:
        while degrees < 0:
            print('Nie ma tak niskich temperatur.')
            degrees = float(input('Podaj liczbę stopni: \n'))
elif scale == 'f' and degrees >= -459.67:
    kelvin = 5/9 * (degrees-32) + 273.15
    celsjusz = 5/9 * (degrees-32)
    print('Temperatura ', degrees, ' stopni Farenheita')
    print('to ', kelvin, ' stopni w skali Kelvina')
    print('i ', celsjusz, 'stopni w skali Celsjusza.')
    if degrees < -459.67:
        while degrees < 0:
            print('Nie ma tak niskich temperatur.')
            degrees = float(input('Podaj liczbę stopni: \n'))



