def is_leap_year(Y):
    return Y % 4 == 0 and not (Y % 100 == 0 and Y % 400)

def month_days(M, Y):
    if M == 2:
        if is_leap_year(Y):
            return 29
        return 28
    if 1 <= M <= 7:
        return 31 if M % 2 else 30
    return 30 if M % 2 else 31

def month_days2(M, Y):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if M == 2 and is_leap_year(Y):
        return month[M - 1] + 1
    return month[M - 1]

if __name__ == "__main__":
    print(31, month_days(1, 2012), month_days2(1, 2012))
    print(29, month_days(2, 2012), month_days2(2, 2012))
    print(30, month_days(9, 2012), month_days2(9, 2012))
    
    print(31, month_days(1, 2003), month_days2(1, 2003))
    print(28, month_days(2, 2003), month_days2(2, 2003))
    print(30, month_days(9, 2003), month_days2(9, 2003))
    
    print(31, month_days(1, 2000), month_days2(1, 2000))
    print(29, month_days(2, 2000), month_days2(2, 2000))
    print(30, month_days(9, 2000), month_days2(9, 2000))
    
    print(31, month_days(1, 1900), month_days2(1, 1900))
    print(28, month_days(2, 1900), month_days2(2, 1900))
    print(30, month_days(9, 1900), month_days2(9, 1900))
