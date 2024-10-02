income = float(input("Entre com os rendimentos "))

if income < 85528:
    tax = income * 0.18 - 556.02
else:
    tax = income * 0.32 - 14839.02

tax = round(tax, 0)

print(
 "A taxa é:", tax, "thalers")


