def num_days(month):
    if month == 'feb':
        days = 28
    elif month in {'apr', 'jun', 'sep', 'nov'}:
        days = 30
    elif month in {'jan', 'mar', 'may', 'jul', 'aug', 'oct', 'dec'}:
        days = 31
    else:
        print("The program ended because you didn't enter a correct month.")
        raise SystemExit(1)
    print("number of days in", month, "is", days)

num_days('jan')
num_days('feb')
num_days('apr')
num_days('oct')
num_days('November')
# optimize/shorten the code in the function
# try to reduce the number of conditionals
