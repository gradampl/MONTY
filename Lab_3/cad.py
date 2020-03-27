def greeting():
    should_continue = True
    while should_continue:
        choice = input("Jeśli chcesz, żebym zamienił liczbę rzymską na arabską, wciśnij 't'."\
                       "\nJeśli chcesz zakończyć program, wciśnij 'n'.\n")
        if choice.lower() !='t' and choice.lower() !='n':
            print('Nie wiem, co mam zrobić.')
        elif choice.lower() == 'n':
            should_continue = False
        else:
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

    reversed_list = []

    while input_chars != []:
        reversed_list.append(int(input_chars.pop()))

    arabic = 0
    previous = 0

    for i in range(len(reversed_list)):
        current = reversed_list[i]
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
    print(calculate(switched))

# I II III IV V VI VII VIII IX X XI XII XIII XIV XV XVI XVII XVIII XIX XX XXI XXII XXIII XIV XXV

greeting()