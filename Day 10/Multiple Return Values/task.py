# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# print(format_name("AnGEla", "YU"))


def is_leap_year(year):
    # Write your code here.
    # Don't change the function name.
    if year % 4 and year % 400:
        return True
    else:
        return False
print(is_leap_year(2000))