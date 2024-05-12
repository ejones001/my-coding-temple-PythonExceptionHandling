def fahrenheit_to_celsius(fahrenheit):
    try:
        celsius = (fahrenheit - 32) * 5 / 9
        return celsius
    except ZeroDivisionError:
        print("Error: Division by zero occurred during temperature conversion.")
    except OverflowError:
        print("Error: Overflow occurred during temperature conversion.")

# Example usage:
try:
    fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
    celsius = fahrenheit_to_celsius(fahrenheit)
    print(f"{fahrenheit} Fahrenheit is equal to {celsius:.2f} Celsius.")
except ValueError:
    print("Error: Please enter a valid numerical temperature.")
