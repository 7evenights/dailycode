
first_date = input().split()
sec_date = input().split()

day = (int(first_date[0]) - int(sec_date[0]))
fine_day = 15*day

month = (int(first_date[1]) - int(sec_date[1]))
fine_month = (500 * month)

year = (int(first_date[2]) - int(sec_date[2]))
fine_year = 10000


if year > 0:
    print(fine_year)
elif year < 0:
    print(0)
elif year == 0:
    if month < 0:
        print(0)
    elif month > 0:
        print(fine_month)
    elif month == 0:
        if fine_day <= 0:
            print(0)
        if fine_day > 0:
            print(fine_day)
