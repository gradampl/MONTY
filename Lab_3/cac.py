phone_numbers = {'Iwona': 2134098, 'Paweł': 4138769, 'Adam': 5352211, 'Gaweł': 4123455, 'Waldemar': 9909090}
print(phone_numbers['Adam'])
phone_numbers['Franz'] = 89523646
phone_numbers['Iwona'] = 10
print(phone_numbers)
print(sorted(phone_numbers))
print(list(sorted(phone_numbers)))
print('Iwona' in phone_numbers)
print('Iwona' not in phone_numbers)
del phone_numbers['Franz']
print(list(sorted(phone_numbers)))
del phone_numbers
# print(phone_numbers)
# NameError: name 'phone_numbers' is not defined
