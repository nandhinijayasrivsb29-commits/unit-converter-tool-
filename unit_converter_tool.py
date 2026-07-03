# ============================================
# UNIT CONVERTER TOOL
# Converts between common units: length, weight,
# temperature
# ============================================

def length_converter():
    """Handles length conversions (meters, km, miles, feet, etc.)"""
    
    # Conversion factors — everything relative to 1 meter
    units = {
        "meter": 1,
        "kilometer": 1000,
        "centimeter": 0.01,
        "mile": 1609.34,
        "foot": 0.3048,
        "inch": 0.0254
    }
    
    print("\nAvailable units:", ", ".join(units.keys()))
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    
    if from_unit not in units or to_unit not in units:
        print("❌ Invalid unit entered!")
        return
    
    value = float(input(f"Enter value in {from_unit}: "))
    
    # Convert to meters first, then to target unit
    value_in_meters = value * units[from_unit]
    result = value_in_meters / units[to_unit]
    
    print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")


def weight_converter():
    """Handles weight conversions (kg, grams, pounds, etc.)"""
    
    # Everything relative to 1 kilogram
    units = {
        "kilogram": 1,
        "gram": 0.001,
        "pound": 0.453592,
        "ounce": 0.0283495
    }
    
    print("\nAvailable units:", ", ".join(units.keys()))
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    
    if from_unit not in units or to_unit not in units:
        print("❌ Invalid unit entered!")
        return
    
    value = float(input(f"Enter value in {from_unit}: "))
    
    value_in_kg = value * units[from_unit]
    result = value_in_kg / units[to_unit]
    
    print(f"✅ {value} {from_unit} = {result:.4f} {to_unit}")


def temperature_converter():
    """Handles temperature conversions (Celsius, Fahrenheit, Kelvin)"""
    
    print("\nAvailable units: celsius, fahrenheit, kelvin")
    from_unit = input("Convert from: ").lower()
    to_unit = input("Convert to: ").lower()
    
    value = float(input(f"Enter value in {from_unit}: "))
    
    # Step 1: Convert input to Celsius first
    if from_unit == "celsius":
        celsius = value
    elif from_unit == "fahrenheit":
        celsius = (value - 32) * 5/9
    elif from_unit == "kelvin":
        celsius = value - 273.15
    else:
        print("❌ Invalid unit entered!")
        return
    
    # Step 2: Convert Celsius to the target unit
    if to_unit == "celsius":
        result = celsius
    elif to_unit == "fahrenheit":
        result = (celsius * 9/5) + 32
    elif to_unit == "kelvin":
        result = celsius + 273.15
    else:
        print("❌ Invalid unit entered!")
        return
    
    print(f"✅ {value} {from_unit} = {result:.2f} {to_unit}")


# ============================================
# MAIN MENU
# ============================================

def main():
    """Displays menu and routes user to the correct converter"""
    
    while True:
        print("\n===== UNIT CONVERTER =====")
        print("1. Length")
        print("2. Weight")
        print("3. Temperature")
        print("4. Exit")
        
        choice = input("Choose an option (1-4): ")
        
        if choice == "1":
            length_converter()
        elif choice == "2":
            weight_converter()
        elif choice == "3":
            temperature_converter()
        elif choice == "4":
            print("Goodbye! 👋")
            break
        else:
            print("❌ Invalid choice, try again.")


# Run the program
if __name__ == "__main__":
    main()