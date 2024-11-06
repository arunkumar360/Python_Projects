principle = 0
rate = 0
year = 0

while True:
    principle = float(input("Enter princible amount:"))
    if principle < 0:
        print("princible can't be less than zero!")
    else:
        break

while True:
    rate = float(input("Enter interest rate :"))
    if principle < 0:
        print("Interest rate can't be less than zero!")
    else:
        break

while True:
    year = int(input("Enter year:"))
    if principle < 0:
        print("year can't be less than zero!")
    else:
        break



total = principle * pow((1+rate/100),year)
print(f"Balance after {year} year is : ${total:.2f}")