"""
name: Derek D'Arcy
Description: This program manages the seating for an airline
"""


def main():
    seating_chart = ['A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A', 'A']
    menu(seating_chart)


def menu(seating_chart: list[str]):
    """Menu continuously loops to get what user wishes to do"""
    while True:
        first_class_status = "Full" if seating_chart[:5].count('X') == 5 else ""
        economy_status = "Full" if seating_chart[5:].count('X') == 5 else ""
        print(f"1. First Class \t (Rows: 1 to 5) \t {first_class_status}")
        print(f"2. Economy \t (Rows: 6 to 10 \t {economy_status}")
        print("3. Exit")
        print(f"Seating Chart: \t {seating_chart}")
        user_choice = int(input("Please choose option '1', '2', or '3'. Choice: "))
        if user_choice == 1:
            if first_class_status == "Full":
                print("First class is full. Please choose a different option")
            else:
                reserve_first_class(seating_chart)
        elif user_choice == 2:
            if economy_status == "Full":
                print("Economy is full. Please choose a different option")
            else:
                reserve_economy(seating_chart)
        elif user_choice == 3:
            print("Thank you for flying with us")
            break
        else:
            print("That was not a valid choice.")


def reserve_first_class(seating_chart: list[str]):
    """Reserves a first class seat based on seating chart"""
    seat_choice = int(input("Please select a seat number (1 - 5): "))
    while seating_chart[seat_choice-1] == 'X' or seat_choice not in range(1, 6):
        seat_choice = int(input("Invalid choice. Please select a different seat number (1 - 5): "))
    seating_chart[seat_choice-1] = 'X'


def reserve_economy(seating_chart: list[str]):
    """Reserves a economy seat based on seating chart"""
    seat_choice = int(input("Please select a seat number (6 - 10): "))
    while seat_choice not in range(6, 11) or seating_chart[seat_choice-1] == 'X':
        seat_choice = int(input("Invalid choice. Please select a seat number (6 - 10): "))
    seating_chart[seat_choice-1] = 'X'


if __name__ == "__main__":
    main()
