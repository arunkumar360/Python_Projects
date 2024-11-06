unit = input("Enter unit Celsius or Farenheit (C/F):").upper()
temp = float(input("Enter your temperature:"))

if unit == 'C':
    temp = (9 * temp) / 5 + 32
    print(f"Temperature in Farenheit is : {round(temp,1)} F")

elif unit == 'F':
    temp = (temp - 32) * 5 / 9 
    print(f"Temperature in Celsius is : {round(temp,1)} C")

else:
    print(f"{unit} is not a valid measurement!")