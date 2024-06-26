def convert_temp(temp, original_unit):
    if original_unit.upper() == 'C':
        return f"{temp} degrees Celsius is equal to {(temp * 9/5) + 32} degrees Fahrenheit and {temp + 273.15} Kelvin."
    elif original_unit.upper() == 'F':
        return f"{temp} degrees Fahrenheit is equal to {(temp - 32) * 5/9} degrees Celsius and {(temp - 32) * 5/9 + 273.15} Kelvin."
    elif original_unit.upper() == 'K':
        return f"{temp} Kelvin is equal to {temp - 273.15} degrees Celsius and {(temp - 273.15) * 9/5 + 32} degrees Fahrenheit."
    else:
        return "Invalid unit. Please enter C for Celsius, F for Fahrenheit, or K for Kelvin."


def main():
    print("Temperature Conversion Program")
    print("-------------------------------")

    n = int(input("Enter the number of times you want to convert temperatures: "))

    for _ in range(n):
        original_unit = input("Enter the original unit (C for Celsius, F for Fahrenheit, K for Kelvin): ")
        temperature = float(input("Enter the temperature value: "))
        print(convert_temp(temperature, original_unit))
        print()


if __name__ == "__main__":
    main()