weight = float(input("Enter your weight:"))
unit = input("Enter unit Kilogram or Pounds (K or L):").upper()

if unit == 'K' :
    weight = weight * 2.205
    unit = 'Lps.'
    print(f"Your weight in Pound is:{round(weight,2)} {unit}")
elif unit == 'L' :
    weight = weight / 2.205
    unit = 'Kgs.'
    print(f"Your weight in Kilogram is:{round(weight,2)} {unit}")

else:
    print(f"{unit} is not valid unit!")