FAHRENHEIT_TO_CELSIUS_FACTOR = 5 / 9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9 / 5


def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR


def convert_to_fahrenheit(celsius):
    return (celsius * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32


def main():
    temp_input = input("Enter the temperature to convert: ")

    # Validate numeric temperature input
    try:
        temp = float(temp_input)
    except ValueError:
        raise ValueError("Invalid temperature. Please enter a numeric value.")

    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    if unit == "C":
        result = convert_to_fahrenheit(temp)
        print(f"{temp}°C is {result}°F")

    elif unit == "F":
        result = convert_to_celsius(temp)
        print(f"{temp}°F is {result}°C")

    else:
        print("Invalid unit. Please enter 'C' or 'F'.")


if __name__ == "__main__":
    main()
