def wrong_format():
    print("Niewłaściwy format wprowadzonych danych.\n")


def formally_wrong():
    print("To nie jest formalnie poprawny nr PESEL.")


def get_input():
    user_input = None
    is_len_correct = False
    is_numeric = False
    while is_len_correct != True or is_numeric != True:
        user_input = input("Podaj numer PESEL: \n")
        if len(user_input) == 11:
            is_len_correct = True
        else:
            wrong_format()
            continue
        for i in range(len(user_input)):
            if user_input[i] not in '0123456789':
                wrong_format()
                break
            else:
                is_numeric = True
    calculate_sum(user_input)


def calculate_sum(user_input):
    sum = 0
    weight = [9, 7, 3, 1]
    for i in range(0, 10):
        sum = sum + weight[i % 4] * int(user_input[i])
    check_sum(sum, user_input)


def check_sum(sum, user_input):
    if sum % 10 != int(user_input[-1]):
        formally_wrong()
        get_input()
    else:
        correct_date(user_input)


def correct_date(user_input):
    months = {'01': 31, '02': 28, '03': 31, '04': 30,
              '05': 31, '06': 30, '07': 31, '08': 31,
              '09': 30, '10': 31, '11': 30, '12': 31}

    m = str(set_month(user_input))
    d = int(set_day(user_input))
    y = int(set_year(user_input))

    is_leap = None

    if m == '02' and d == 29:
        if y % 4 == 0:
            is_leap = True
        if y % 100 == 0:
            is_leap = False
        if y % 400 == 0:
            is_leap = True
        if is_leap != True:
            formally_wrong()
            get_input()
        else:
            print_info(user_input)
    else:
        if m in months and d in range(1, (int(months[str(m)]) + 1)):
            print_info(user_input)
        else:
            formally_wrong()
            get_input()


def set_month(user_input):
    month = None
    if int(user_input[2]) % 2 == 0:
        month = '0' + str(user_input[3])
    else:
        month = '1' + str(user_input[3])
    return month


def set_year(user_input):
    year = None
    if int(user_input[2]) == 8 or int(user_input[2]) == 9:
        year = '18' + str(user_input[0]) + str(user_input[1])
    else:
        i = 0
        k = 0
        while i <= 6:
            if int(user_input[2]) == i or int(user_input[2]) == i + 1:
                year = str(int(19 + (i - k))) + str(user_input[0]) + str(user_input[1])
                break
            k += 1
            i += 2
    return year


def set_day(user_input):
    day = str(user_input[4]) + str(user_input[5])
    return day


def set_gender(user_input):
    gender = None
    if int(user_input[9]) % 2 == 0:
        gender = 'kobieta'
    else:
        gender = 'mężczyzna'
    return gender


def print_info(user_input):
    gender = set_gender(user_input)
    day = set_day(user_input)
    month = set_month(user_input)
    year = set_year(user_input)
    print("{0}, data urodzenia: {1}.{2}.{3}".format(gender, day, month, year))


# PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL #

get_input()
