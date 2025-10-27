# Pay and Go Evening Parking Program
# Constants
MAX_CAPACITY = 50
PARKING_FEE = 4.00
ADMIN_PASSWORD = "password"

# Global lists to store vehicle data
plates = []
cc_numbers = []


def print_menu():
    """Display the application menu"""
    print("*" * 60)
    print("*** Welcome to Park and Go Parking Application! ***")
    print("Park from 6 PM - Midnight for a flat fee of $4.00")
    print("*" * 60)
    print("Select from the following options")
    print("1- Register a vehicle")
    print("2- Verify vehicle registration")
    print("3- Display registered vehicles and save them to a file")
    print("4- Display daily charges and save them to a file")
    print("5- Remove a vehicle")
    print("6- Clear vehicles")
    print("0- Exit")


def check_password():
    """Ask user to enter password and validate it"""
    password = input("Enter password: ")
    if password == ADMIN_PASSWORD:
        return True
    else:
        return False


def register_vehicle():
    """Register a vehicle in the parking lot"""
    if len(plates) >= MAX_CAPACITY:
        print("The parking lot is full")
        return
    
    plate = input("Enter license plate number: ")
    
    if plate in plates:
        print(f"License plate {plate} is already registered")
    else:
        cc_number = input("Enter credit card number: ")
        plates.append(plate)
        cc_numbers.append(cc_number)
        print(f"Vehicle {plate} registered successfully")


def verify_vehicle(plate):
    """Verify if a vehicle is registered in the parking lot"""
    if plate in plates:
        return plate
    else:
        return None


def display_vehicles():
    """Display all registered vehicles and save to vehicles.txt"""
    if len(plates) == 0:
        print("No vehicles in the lot")
    else:
        print("\nLicense Plates in Lot:")
        for plate in plates:
            print(plate)
        
        # Save to file
        with open("vehicles.txt", "w") as file:
            file.write("License Plates in Lot:\n")
            for plate in plates:
                file.write(plate + "\n")


def display_charges():
    """Display all charges and save to charges.txt"""
    if len(plates) == 0:
        print("No vehicles in the lot")
    else:
        print("\nDaily Charges:")
        print(f"{'License Plate':<20}{'Credit Card':<20}{'Charge'}")
        print("-" * 50)
        for i in range(len(plates)):
            print(f"{plates[i]:<20}{cc_numbers[i]:<20}${PARKING_FEE:.2f}")
        
        # Save to file
        with open("charges.txt", "w") as file:
            file.write("Daily Charges:\n")
            file.write(f"{'License Plate':<20}{'Credit Card':<20}{'Charge'}\n")
            file.write("-" * 50 + "\n")
            for i in range(len(plates)):
                file.write(f"{plates[i]:<20}{cc_numbers[i]:<20}${PARKING_FEE:.2f}\n")


def remove_vehicle(plate):
    """Remove a vehicle from the parking lot"""
    result = verify_vehicle(plate)
    if result is None:
        print(f"It is not registered")
    else:
        index = plates.index(plate)
        plates.pop(index)
        cc_numbers.pop(index)
        print(f"License plate {plate} removed successfully")


def clear_vehicles():
    """Clear all vehicles from the parking lot"""
    plates.clear()
    cc_numbers.clear()
    print("All license plates removed")


def main():
    """Main function to run the parking program"""
    
    while True:
        print_menu()
        choice = input("Enter your choice: ")
        
        if choice == "1":
            register_vehicle()
            input("Press Enter to continue...")
        elif choice == "2":
            if check_password():
                plate = input("Enter license plate number: ")
                result = verify_vehicle(plate)
                if result is None:
                    print(f"License plate {plate} not found")
                else:
                    print(f"License plate {plate} found in lot")
            else:
                print("Password is incorrect")
            input("Press Enter to continue...")
        elif choice == "3":
            if check_password():
                display_vehicles()
            else:
                print("Password is incorrect")
            input("Press Enter to continue...")
        elif choice == "4":
            if check_password():
                display_charges()
            else:
                print("Password is incorrect")
            input("Press Enter to continue...")
        elif choice == "5":
            if check_password():
                plate = input("Enter license plate number: ")
                remove_vehicle(plate)
            else:
                print("Password is incorrect")
            input("Press Enter to continue...")
        elif choice == "6":
            if check_password():
                clear_vehicles()
            else:
                print("Password is incorrect")
            input("Press Enter to continue...")
        elif choice == "0":
            print("Exiting the parking system. Goodbye!")
            break
        elif choice == "":
            continue
        else:
            print("Invalid choice. Please try again")
            input("Press Enter to continue...")


# Run the program
if __name__ == "__main__":
    main()