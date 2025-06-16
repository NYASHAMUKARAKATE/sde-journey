# This code is a unit converter application that allows users to convert between different units of length, temperature, weight, and volume.    
# It provides a user-friendly interface to select the type of conversion and input the values and units.
# The conversion functions handle the logic for converting between specified units using predefined conversion factors. 
# The application continues to prompt the user for conversions until they choose to exit.
# The code is structured to be modular, with separate functions for each type of conversion and a main function to run the application. 
# The unit converter supports various units for each type of measurement, ensuring flexibility and usability.



def convert_length(value, from_unit, to_unit):
    """Convert length between different units."""
    # Define conversion factors
    conversion_factors = {
        'meters': 1,
        'kilometers': 0.001,
        'centimeters': 100,
        'millimeters': 1000,
        'miles': 0.000621371,
        'yards': 1.09361,
        'feet': 3.28084
    }

    # Convert the length to meters
    if from_unit in conversion_factors:
        value_in_meters = value / conversion_factors[from_unit]
    else:
        return "Invalid from_unit"

    # Convert from meters to a specified unit
    if to_unit in conversion_factors:
        return value_in_meters * conversion_factors[to_unit]
    else:
        return "Invalid to_unit"
    
def convert_temperature(value, from_unit, to_unit):
    """Convert temperature between different units."""
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        else:
            return "Invalid to_unit"
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        else:
            return "Invalid to_unit"
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        else:
            return "Invalid to_unit"
    else:
        return "Invalid from_unit"

def convert_weight(value, from_unit, to_unit):
    """Convert weight between different units."""
    # Define conversion factors
    conversion_factors = {
        'grams': 1,
        'kilograms': 0.001,
        'milligrams': 1000,
        'pounds': 0.00220462,
        'ounces': 0.035274
    }

    # Convert the weight to grams
    if from_unit in conversion_factors:
        value_in_grams = value / conversion_factors[from_unit]
    else:
        return "Invalid from_unit"

    # Convert from grams to a specified unit
    if to_unit in conversion_factors:
        return value_in_grams * conversion_factors[to_unit]
    else:
        return "Invalid to_unit"
def convert_volume(value, from_unit, to_unit):
    """Convert volume between different units."""
    # Define conversion factors
    conversion_factors = {
        'liters': 1,
        'milliliters': 1000,
        'cubic_meters': 0.001,
        'gallons': 0.264172,
        'quarts': 1.05669,
        'pints': 2.11338,
        'cups': 4.22675
    }

    # Convert the volume to liters
    if from_unit in conversion_factors:
        value_in_liters = value / conversion_factors[from_unit]
    else:
        return "Invalid from_unit"

    # Convert from liters to a specified unit
    if to_unit in conversion_factors:
        return value_in_liters * conversion_factors[to_unit]
    else:
        return "Invalid to_unit"
    
def unit_converter():
    print("---------------Welcome to the Unit Converter App!--------\n")
    print("--------------------Select conversion type------------------\n")
    print("1. Length")
    print("2. Temperature")
    print("3. Weight")
    print("4. Volume")
    print("------------------------------------------------------\n")

    while True:
        choice = input("Enter choice (1 / 2 / 3 / 4): ")

        if choice in ['1', '2', '3', '4']:
            value = float(input("Enter value to convert: "))
            from_unit = input("Enter from unit: ")
            to_unit = input("Enter to unit: ")

            if choice == '1':
                result = convert_length(value, from_unit, to_unit)
            elif choice == '2':
                result = convert_temperature(value, from_unit, to_unit)
            elif choice == '3':
                result = convert_weight(value, from_unit, to_unit)
            elif choice == '4':
                result = convert_volume(value, from_unit, to_unit)

            print(f"Converted value: {result}")
        else:
            print("Invalid choice. Please try again.")
        
        another_conversion = input("Do you want to perform another conversion? (yes/no): ")
        if another_conversion.lower() != 'yes':
            break
    print("Thank you for using the Unit Converter App!")
if __name__ == "__main__":
    unit_converter()
