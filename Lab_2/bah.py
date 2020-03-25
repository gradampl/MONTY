months = ['kwiecień', 'marzec', 'styczeń', 'wrzesień', 'luty', 'maj', 'sierpień', 'listopad', 'lipiec', 'czerwiec', 'grudzień', 'październik']

print(months)

# Result:
# ['kwiecień', 'marzec', 'styczeń', 'wrzesień', 'luty', 'maj', 'sierpień', 'listopad', 'lipiec', 'czerwiec', 'grudzień', 'październik']


months_dictionary = {}

for i in range(12):
    if len(months[i]) == 4:
        months_dictionary[months[i]] = 2
    elif len(months[i]) == 3:
        months_dictionary[months[i]] = 5
    elif len(months[i]) == 7:
        months_dictionary[months[i]] = 1
    elif len(months[i]) == 11:
        months_dictionary[months[i]] = 10
    elif 'gr' in months[i]:
        months_dictionary[months[i]] = 12
    elif 'lis' in months[i]:
        months_dictionary[months[i]] = 11
    elif 'lip' in months[i]:
        months_dictionary[months[i]] = 7
    elif 'czer' in months[i]:
        months_dictionary[months[i]] = 6
    elif 'sier' in months[i]:
        months_dictionary[months[i]] = 8
    elif 'wr' in months[i]:
        months_dictionary[months[i]] = 9
    elif 'kw' in months[i]:
        months_dictionary[months[i]] = 4
    elif 'mar' in months[i]:
        months_dictionary[months[i]] = 3


# https://www.geeksforgeeks.org/python-sort-python-dictionaries-by-key-or-value/
# print(sorted(key_value.items(), key =
#              lambda kv:(kv[1], kv[0])))

print(list(sorted(months_dictionary.items(), key =
             lambda kv:(kv[1], kv[0]))))

# Result: 
# [('styczeń', 1), ('luty', 2), ('marzec', 3), ('kwiecień', 4), ('maj', 5), ('czerwiec', 6), ('lipiec', 7), ('sierpień', 8), ('wrzesień', 9), ('październik', 10), ('listopad', 11), ('grudzień', 12)]
