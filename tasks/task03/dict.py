import re
string_list = [
   "Hello, World!",
   "The world is mine",
   "Hello, how are you?"
]

words_list = [{'word':'word', 'count':'count', 'first_line':'first line'}]
check_list = []

for sting_number, value in enumerate(string_list):
    string = value.split()
    for unit_number, string_value in enumerate(string):
        string_value = re.sub('[^A-Za-z0-9]+', '', string_value)
        string_value = string_value.lower()
        if string_value in check_list:
            for word_number, word in enumerate(words_list):
                if string_value == word['word']:
                    word['count'] +=1
        else:
            check_list.append(string_value)
            words_list.append({'word':string_value, 'count':1, 'first_line':sting_number})

for  number, item in enumerate(words_list):
    print (list(item.values()))
