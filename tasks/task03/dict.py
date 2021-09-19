import re
string_list = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

words_list = [{'word':'word', 'count':'count', 'first_line':'first line'}]
check_list = []

for sting_number in range(0, len(string_list)):
    string = string_list[sting_number].split()
    print(string)
    for unit_number in range(0, len(string)):
        string[unit_number] = ''.join(x for x in string[unit_number] if x.isalpha())
        string[unit_number] = string[unit_number].lower()
        print (string[unit_number])
        if string[unit_number] in check_list:
            for word_number in range (0, len(words_list)-1):
                if string[unit_number] == words_list[word_number]['word']:
                    words_list[word_number]['count'] +=1
        else:
            check_list.append(string[unit_number])
            words_list.append({'word':string[unit_number], 'count':1, 'first_line':sting_number})

for item in range(0, len(words_list)):
    print (list(words_list[item].values()))
