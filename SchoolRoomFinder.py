
print("|    Room Finder v1.0     |")

print()
while True:
    code = input("Enter the room code: ").title()

    if len(code)<=4:
        letter = code[0]
        print("This room is located in the "+ letter+"block.")

        number = int(code[1:])
        if number < 100:
            print("It is on the ground floor.")
        elif number >=100 and number < 200:
            print("It is on the first floor.")
        elif number >=200:
            print("It is on the second floor")

    else:
        rooms = {"Main Reception": "at the main entrance of the A block",
                 "Staff Room": "on the top floor of the B block",
                 "Sport Hall": "on the side of the B block",
                 "Dance Studio": "on the ground floor in the A block",
                 "Activity Studio": "on the ground floor in the A block"
                 }
        if code in rooms:
            print("This room is located "+ rooms[code])
        else:
            print("We cannont locate this room! Are you sure this is a valid room?")
