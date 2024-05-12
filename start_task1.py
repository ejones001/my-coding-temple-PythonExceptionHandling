def get_temperature():
    while True:
        temperature_str = input("Please enter the temperature in Fahrenheit: ")
        try:
            temperature = float(temperature_str)
            return temperature
        except ValueError:
            print("Error: Please enter a valid numerical temperature.")


temperature = get_temperature()
print("Temperature entered:", temperature)
