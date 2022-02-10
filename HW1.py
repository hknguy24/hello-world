#Huy Kevin Nguyen
#PSID: 1346435

print("Birthday Calculator")

print("Current day")

current_month = int(input("Month: "))

current_day = int(input("Day: "))

current_year = int(input("Year: "))


print("Birthday")

birth_month = int(input("Month: "))

birth_day = int(input("Day: "))

birth_year = int(input("Year: "))

difference_years = current_year - birth_year

if current_month > birth_month:
    age = difference_years
elif current_month == birth_month:
    if current_day >= birth_day:
        age = difference_years
    else:
        age = difference_years - 1
elif current_month < birth_month:
    age = difference_years - 1

print("You are", age, "years old.")
