weight = int(input("Weight: "))
unit = input("(L)bs or (K)g: ")

if unit.upper() == "L":
    weight = weight * 0.4536
    print(f"You weight {weight} kg")
elif unit.upper() == "K":
    weight= weight/0.4536
    print(f"You weight {weight} lbs")