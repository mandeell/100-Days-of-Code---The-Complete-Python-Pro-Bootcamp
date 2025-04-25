number_to_check = int(input('What is the number you want to check? '))

number_checked = number_to_check % 2
if number_checked == 0:
    print('Even Number')
else:
    print('Odd Number')
