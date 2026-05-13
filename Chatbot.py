def greet():
    print("🏨 Hello! Welcome to Sunshine Hotel Bot.")
    print("I am your virtual assistant (Created in 2026).")


def get_name():
    print("Please enter your name:")
    name = input()
    print(f"Welcome {name}! How can I assist you today?")
    return name


def hotel_info():
    print("\n🏨 Hotel Information:")
    print("We offer Single, Double, and Deluxe rooms.")
    print("Located in the city center near main market.")


def facilities():
    print("\n✨ Facilities:")
    print("- Free WiFi")
    print("- Swimming Pool")
    print("- Gym")
    print("- Restaurant")
    print("- Parking")


def room_price():
    print("\n💰 Room Prices:")
    print("Single Room: ₹1500")
    print("Double Room: ₹2500")
    print("Deluxe Room: ₹4000")


def quiz():

    score = 0

    print("What is the check-in time?")
    print("1. 10 AM")
    print("2. 12 PM")
    print("3. 3 PM")

    answer = int(input("Enter answer: "))

    if answer == 2:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")


    print("\nWhich facility is available in hotel?")
    print("1. WiFi")
    print("2. Gym")
    print("3. Pool")
    print("4. All")

    answer = int(input("Enter answer: "))

    if answer == 4:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")


    print("\nWhich room type is premium?")
    print("1. Single")
    print("2. Double")
    print("3. Deluxe")

    answer = int(input("Enter answer: "))

    if answer == 3:
        print("Correct ✅")
        score += 1
    else:
        print("Wrong ❌")


    print(f"\nFinal Score = {score}/3")



def end():
    print("\n🤖 Thank you for visiting Sunshine Hotel!")
    print("Have a great day 😊")


def main():
    greet()
    get_name()

    while True:
        print("\nChoose an option:")
        print("1. Hotel Info")
        print("2. Facilities")
        print("3. Room Prices")
        print("4. Take Quiz")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            hotel_info()
        elif choice == "2":
            facilities()
        elif choice == "3":
            room_price()
        elif choice == "4":
            quiz()
        elif choice == "5":
            break
        else:
            print("Invalid choice! Please try again.")

    end()


if __name__ == "__main__":
    main()