unit = input("Enter the unit you want to convert from (e.g., 'meters', 'kilometers', 'miles'): ").strip().lower()
new_unit = input("Enter the unit you want to convert to (e.g., 'meters', 'kilometers', 'miles'): ").strip().lower()

value = float(input("Enter the value to convert: "))

match (unit, new_unit):
    case ("meters", "kilometers"):
        converted_value = value / 1000
    case ("kilometers", "meters"):
        converted_value = value * 1000
    case ("miles", "kilometers"):
        converted_value = value * 1.60934
    case ("kilometers", "miles"):
        converted_value = value / 1.60934
    case ("miles", "meters"):
        converted_value = value * 1609.34
    case ("meters", "miles"):
        converted_value = value / 1609.34
    case _:
        print("Conversion from {} to {} is not supported.".format(unit, new_unit))
        exit()
print("{} {} is equal to {:.4f} {}".format(value, unit, converted_value, new_unit))