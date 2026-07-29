#compoundinterestcalculator.py
principal = 0
time = 0
rate = 0

while principal <= 0:
    principal = float(input("Enter the principal: "))
    if principal <= 0:
        print("Zero is not possible")

while time <= 0:
        time = int(input("Enter the time: "))

        if time <= 0:
               print("Time cannot be zero.")

while rate <= 0:
    rate = float(input("Enter the rate: "))
    if rate <= 0:
            print("rate cannot be zero.")
total = principal * (1 + rate / 100) ** time

print(f"Your balance after {time} year/s is ${total:.2f}")