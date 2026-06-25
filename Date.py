
import datetime

def validation_e_date(date):
    try:
        datetime.datetime.strptime(date, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def date_check():
    flag = False
    while not flag:
        datee = input("Enter date of wicket in format YYYY-MM-DD")
        if not validation_e_date(datee):
            print("wrong format man try again")
        else:
            flag = True
    return datee