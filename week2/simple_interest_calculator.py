principle = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the time in number of years: "))

try:
    if principle < 0 or rate < 0 or time < 0:
        raise ValueError("Principal, rate, and time must be non-negative.")

    simple_interest = (principle * rate * time) / 100
    amount = simple_interest + principle
    print("The simple interest is: ${:.2f}".format(simple_interest))
    print("The total amount is: ${:.2f}".format(amount))
except ValueError as e:
    print("Error:", e)