from datetime import date


print("Age Calculator")
print("Enter your Name: ")
name = input()
print("What is your birthmonth " + name + "?")
print("")
print("[1] January")
print("[2] February")
print("[3] March")
print("[4] April")
print("[5] May")
print("[6] June")
print("[7] July")
print("[8] August")
print("[9] September")
print("[10] October")
print("[11] November")
print("[12] December")
bmonth = int(input())

if bmonth == 1:
    print("")
    print("Your Birthmonth is January! How about your Birthday?")
    day = int(input())
    print("")
    print("Your Birthyear?")
    birthyear = int(input())
    
    today = date.today()
    
    yeardays = 365
    totaldaysinmonth = 30
    month = today.month
    year = today.year
    
    age = year - birthyear
    
    agemonth = (year - birthyear) * month - bmonth
    
    agedays = (year - birthyear) * yeardays + (month - bmonth) * totaldaysinmonth
    + (month - day)
    
    print(f"Your age is {age} and you've been here for {agemonth} months and {agedays} days")


    