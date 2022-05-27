# Tip Calculator

# variables
bill = float(input("What is the Total Bill: "))
tip_percent = float(input("How much are you going to tip: "))
num_of_people = int(input("How many people: "))
final_bill = (bill * (tip_percent/100) + bill)/num_of_people

print(f"your total bill is {round(final_bill,2)}")

