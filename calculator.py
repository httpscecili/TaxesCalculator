income = float(input("Write the income: "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = income * 0.32 - 14839.02

tax = round(tax, 0)

print("The tax is:", tax, "thalers")


