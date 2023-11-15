cities = ["Beirut", "Jbeil", "Tripoli", "Zahle"]
drivers = [["Alex","Beirut","Zahle"], ["Omar","Beirut", "Jbeil"], ["Ahmad","Jbeil", "Tripoli"]]

def add_city():
    new_city = input("Enter the name of the city: ")
    for existing_city in cities:
        if existing_city.lower() == new_city.lower():
            print(f"A city with the name '{new_city}' is already in the list.")
            return
    if len(new_city) > 2:
        cities.append(new_city)
    else:
        print("The city name is invalid.")
    print(cities)

def add_driver():
    driver_name = input("Enter the name of the driver: ")
    for driver in drivers:
        if driver[0].lower() == driver_name.lower():
            print(f"A driver with the name '{driver_name}' is already in the list.")
            return
    driver_city = input("Enter the cities that the driver will visit (comma-separated): ")
    driver_city = [city.strip() for city in driver_city.split(',') if city.strip()]
    driver_info = [driver_name] + driver_city
    drivers.append(driver_info)
    print(drivers)

def add_city_driver():
    driver_name = input("Enter the name of the driver: ")

    driver_index = None
    for i in range(len(drivers)):
        if drivers[i][0].lower() == driver_name.lower():
            driver_index = i
            break

    if driver_index is None:
        print(f"Driver {driver_name} not found.")
        return

    driver_route = drivers[driver_index]
    print(f"The route for {driver_name} is: {driver_route[1:]}")

    while True:
        print("0. Add at the beginning of the route")
        print("-1. Add at the end of the route")
        print("Any other number to add the city to the given index")
        option = input("Enter your choice: ")

        driver_city = input("Enter the name of the city to be added to the driver's route: ")

        if option == '0':
            driver_route.insert(1, driver_city)
        elif option == '-1':
            driver_route.append(driver_city)
        else:
            try:
                index = int(option)
                driver_route.insert(index + 1, driver_city)
            except ValueError:
                print("Invalid index. Please enter a valid index.")
                continue

        print(f"{driver_city} added to {driver_name}'s route: {driver_route[1:]}")
        print(drivers)
        break

def remove_city_driver():
    driver_name = input("Enter the name of the driver: ")
    driver_city = input("Enter the name of the city to be removed from the driver's route: ")

    driver_name_lower = driver_name.lower()
    driver_city_lower = driver_city.lower()

    for i in range (len(drivers)):
        driver_route = drivers[i]
        if driver_route[0].lower() == driver_name_lower:
            if driver_city_lower in map(str.lower, driver_route[1:]):
                updated_route = [driver_route[0]] + [city for city in driver_route[1:] if city.lower() != driver_city_lower]
                drivers[i] = updated_route
                print(f"{driver_city} removed from {driver_name}'s route: {driver_route[1:]}")
                print(drivers)
                break
            else:
                print(f"City {driver_city} not found in {driver_name}'s route.")
                break
    else:
        print(f"Driver {driver_name} not found.")

def check_deliverability():
    driver_city = input("Enter the name of the city to check the deliverability of it: ")

    driver_city_lower = driver_city.lower()
    deliverable_drivers = []

    for driver_info in drivers:
        driver_name = driver_info[0]
        if driver_city_lower in map(str.lower, driver_info[1:]):
            deliverable_drivers.append(driver_name)
        else:
            print("There are no drivers that deliver to ", driver_city)
    driver_name_list = ', ' .join(deliverable_drivers)
    print("The city of '", driver_city, "' is deliverable by ", driver_name_list)

while True:
    print("1. Add a city")
    print("2. Add a driver")
    print("3. Add a city to the driver's route")
    print("4. Remove a city from the driver's route")
    print("5. Check the deliverability of a package")
    print("6. Close the program")
    print(f"The cities available: ", cities)
    print(f"The drivers available with their routes", drivers)
    choice = input("Enter your choice: ")

    if choice == '1':
        add_city()

    if choice == '2':
        add_driver()

    if choice == '3':
        add_city_driver()

    if choice == '4':
        remove_city_driver()

    if choice == '5':
        check_deliverability()

    elif choice == '6':
        print("Bye Bye")
        break