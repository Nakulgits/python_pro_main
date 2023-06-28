# year=int(input("what is the year : \n"))
# month=int(input("what is the month : \n"))
# def is_leap(yr):
#     if yr%100==0 and yr%400==0:
#         return True
#     elif yr%100!=0 and yr%4==0:
#         return True
#     else:
#         return False
# def days_in_month(yr,mth):
#     month_leap_days=[31,29,31,30,31,30,31,31,30,31,30,31]
#     month_non_leap_days=[31,28,31,30,31,30,31,31,30,31,30,31]
#     # first we will be checking whether the year is a leap year or not 
#     if mth >12 or mth <0:
#         return "give valid input for the month"
#     elif is_leap(yr):
#         return month_leap_days[mth-1]
#     else:
#         print("the year is not a leap year")
#         return month_non_leap_days[mth-1]
# days=days_in_month(year,month)
# print(f"so the no of days in that particular month are {days}")

# month_non_leap_days=[31,28,31,30,31,30,31,30,31,30,31,30]
# for i,x in enumerate(month_non_leap_days):
#     print(f"{i}{x}")


#------------ following is the same function above but done using the try and the except block

# def days_in_month(yr, mth):
#     month_leap_days = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
#     month_non_leap_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    
#     try:
#         if mth > 12 or mth < 1:
#             raise ValueError("Invalid input for the month")
        
#         if is_leap(yr):
#             return month_leap_days[mth - 1]
#         else:
#             print("The year is not a leap year")
#             return month_non_leap_days[mth - 1]
#     except ValueError as e:
#         return str(e)
#     finally:
#         print("End of program")

# -------------------------- end of the function --------------------------------

# ------------------- now comes the usage of the docstring -----------------------

