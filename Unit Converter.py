def convert():
    print("1. km to miles\n2. kg to pounds\n3. Celsius to Fahrenheit")
    choice = input("Choose conversion: ")
    val = float(input("Enter value: "))

    if choice == '1':
        print("Miles:", round(val * 0.621371, 2))
    elif choice == '2':
        print("Pounds:", round(val * 2.20462, 2))
    elif choice == '3':
        print("Fahrenheit:", round((val * 9/5) + 32, 2))
    else:
        print("Invalid choice")

convert()
