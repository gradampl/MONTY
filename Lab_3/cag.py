def wrong_format():
    print("Niewłaściwy format wprowadzonych danych.\n")


def get_input():

    user_input = None
    is_len_correct = False
    is_numeric = False

    while is_len_correct !=True or is_numeric !=True:
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

    return user_input


def calculate_sum(user_input):
    sum = 0
    j = 0
    while j<4:
        if j <= 1:
            for i in range((0+j),(9+j),4):
                sum += (9-(2*j))*int(user_input[i])
        else:
            for i in range((0 + j), (5 + j), 4):
                sum += (3-((j-1)*(j-2)))*int(user_input[i])
        j += 1

    return sum



def check_sum(sum,user_input):
    if sum%10 != int(user_input[-1]):
        return False
    else:
        return True

# PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL PESEL #

user_input = get_input()
sum = calculate_sum(user_input)
print(check_sum(sum,user_input))




