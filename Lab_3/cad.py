def greeting():
    should_continue = True
    j = 1
    while should_continue:
        choice = input("Uruchomić program po raz {} ?"\
                       "\nTak - wciśnij 't'.\
                        \nNie - wciśnij 'n'.\n".format(j))
        if choice.lower() !='t' and choice.lower() !='n':
            print('\nNie wiem, co mam zrobić.\n')
        elif choice.lower() == 'n':
            should_continue = False
        else:
            j += 1
            start()

def get_number():
    number = input("Podaj liczbę rzymską, a ja zamienię ją na arabską: \n")
    return number


def check_input(number):
    import re
    p = re.compile('(?<=^)M{0,4}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})(?=$)')
    m = p.match(number)
    if m:
        return True
    else:
        return False


def switch_to_arabic(number):

    input_chars = []

    for i in range(len(number)):
        if number[i] == 'i':
            input_chars.append(int(1))
        elif number[i] == 'v':
            input_chars.append(int(5))
        elif number[i] == 'x':
            input_chars.append(int(10))
        elif number[i] == 'l':
            input_chars.append(int(50))
        elif number[i] == 'c':
            input_chars.append(int(100))
        elif number[i] == 'd':
            input_chars.append(int(500))
        elif number[i] == 'm':
            input_chars.append(int(1000))

    return input_chars



def calculate(input_chars):

    arabic = 0
    previous = 0
    j = len(input_chars)-1

    for i in range(len(input_chars)):
        current = input_chars[j-i]
        if current >= previous:
            arabic += current
        else:
            arabic -= current
        previous = current

    return arabic



def start():

    number = None
    inputOK = False

    while (inputOK != True):
        number = get_number()
        inputOK = check_input(number.upper())

    switched = switch_to_arabic(number.lower())
    print("{} = ".format(number.upper()) + str(calculate(switched)) + "\n")

# I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XIV XXV

greeting()