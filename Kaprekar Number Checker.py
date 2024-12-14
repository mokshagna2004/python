def is_kaperka_number(num):
    square = num**2
    str_num = str(square)
    for i in range(1,len(str_num)):
        right_part = int(str_num[:i])
        left_part = int(str_num[i:])
        if right_part+left_part == num:
            return True
    return False
number = int(input('enter a number'))
if(is_kaperka_number(number)):
    print('its kap')
else:
    print('not kap')
