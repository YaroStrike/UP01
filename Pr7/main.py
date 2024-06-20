def is_leap_year(Y):
    return Y % 4 == 0 and not (Y % 100 == 0 and Y % 400)

def month_days(M, Y):
    month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
    if M == 2 and is_leap_year(Y):
        return month[M - 1] + 1
    return month[M - 1]

if __name__ == "__main__":
    yr = int(input("Введите номер года -> "))
    mo = int(input("Введите номер месяца -> "))
   
    if is_leap_year(yr) == True:
        print(f"В этом месяце {month_days(mo, yr)} дней. Год - високосный!")
    else:
        print(f"В этом месяце {month_days(mo, yr)} дней. Год - невисокосный!")
    