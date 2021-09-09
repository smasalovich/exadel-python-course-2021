number = 1000

while number > 0:
    copy_number = number
    symbol_count = 0
    while copy_number >0:
        symbol_count += 1
        copy_number = copy_number//10
    check_number = 0
    second_copy_number = number
    while second_copy_number >0:
        module = second_copy_number//10
        digit = second_copy_number - module*10
        second_copy_number = second_copy_number//10
        check_number = check_number + digit**symbol_count
    if check_number == number:
        print(number)
    number -= 1
