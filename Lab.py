## **Cinema Booking Program** ##
booked_seats = [
    (1, 5, "Gold 🟡"),
    (1, 6, "Gold 🟡"),
    (2, 10, "Standard 🟤"),
    (3, 7, "Bronze ⚪"),
    (4, 15, "Standard 🟤")
]

# booked show    
def booked_seat():
    if not booked_seats:
        print("No seats booked yet. Please book your seat.")
    else:
        for row, seat, cat in booked_seats:
            print(f"Row {row}, Seat {seat}, Category: {cat}")

# check if seat is booked    
def check_booked():
    row = int(input("Enter row number: "))
    seat = int(input("Enter seat number: "))
    found = False
    for r, s, c in booked_seats:
        if r == row and s == seat:
            print(f"❌ That seat is already booked. Category: {c}")
            found = True
            break
    if not found:
        print("✅ That seat is available.")

# add new booking
def add_booked():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    for r, s, c in booked_seats:
        if r == row and s == seat:
            print("❌ Seat already booked.")
            return
    category = input("Enter ticket category (Gold / Standard / Bronze): ").capitalize()
    if category not in ["Gold", "Standard", "Bronze"]:
        print("❗ Invalid category. Try again.")
        return
    booked_seats.append((row, seat, category))
    print("✅ Seat booked successfully.")

# cancel booking
def cancel_booked():
    row = int(input("Enter row number (1-10): "))
    seat = int(input("Enter seat number (1-20): "))
    for seat_info in booked_seats:
        if seat_info[0] == row and seat_info[1] == seat:
            booked_seats.remove(seat_info)
            print("✅ Seat cancelled successfully.")
            return
    print("❌ That seat is not booked.")

# show sorted booked seats
def sorted_booked():
    sorted_seats = sorted(booked_seats)
    for row, seat, cat in sorted_seats:
        print(f"Row {row}, Seat {seat}, Category: {cat}")

# Calculate and display stats
def calculate():
    print(f"Total seats booked: {len(booked_seats)}")
    seat_row = [0] * 10
    category_count = {"Gold": 0, "Standard": 0, "Bronze": 0}
    for row, seat, cat in booked_seats:
        seat_row[row - 1] += 1
        if cat in category_count:
            category_count[cat] += 1
    print("Booked seats by row:")
    for i in range(10):
        print(f"Row {i + 1}: {seat_row[i]}")
    print("Booked seats by category:")
    for cat, count in category_count.items():
        print(f"{cat}: {count}")


while True:
    print("\nWelcome to the cinema booking program!") 
    print("1. Show all booked seats")
    print("2. Check seat availability")
    print("3. Book a seat")
    print("4. Cancel a booking")
    print("5. Show sorted bookings")
    print("6. Show booked seats statistics")
    print("7. Exit")   

    again = input("Enter your choice: ").strip().lower()
    
# main menu
    if again == "1":
        booked_seat()
    elif again == "2":
        check_booked()
    elif again == "3":
        add_booked()
    elif again == "4":
        cancel_booked()
    elif again == "5":
        sorted_booked()
    elif again == "6":
        calculate()
    elif again == "7":
        print("🎉 Thank you for using the cinema booking program!")
        break
    else:
        print("❗ Please enter a valid option.")
