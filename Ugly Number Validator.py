def is_ugly_number(num):
    if  num <= 0:
        return False
    for i in [2,3,5]:
        while num%i == 0:
            num//=i
    return num == 1
number = int(input('enter a number'))
if is_ugly_number(number):
    print('its ugly number')
else:
    print('not ugly number')




