# Life In Weeks

age = int(input("What is your age: "))
days_in_year = 364.25
age_in_weeks = age * 52
weeks_till_90 = (90 * 52) - age_in_weeks
age_in_days = age * days_in_year
days_till_90 = (90*days_in_year) - age_in_days

print(f" There are this many weeks till your 90 : {weeks_till_90} \n There are this many days till your 90: {days_till_90}")


