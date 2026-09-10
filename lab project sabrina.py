import datetime
from decimal import Decimal
from anonymate.anonymizer import Anonymizer


# Create the AnonyMate anonymizer
anonymizer = Anonymizer()


# Patient/Profile data
profiles = [
    {
        'job': 'Agricultural engineer',
        'company': 'Phillips-Johnson',
        'ssn': '055-51-3629',
        'residence': '1107 Brian Coves\nSouth Jessica, UT 66862',
        'current_location': (
            Decimal('-81.6575675'),
            Decimal('111.794874')
        ),
        'blood_group': 'B+',
        'username': 'nnelson',
        'name': 'Oscar Newman',
        'sex': 'M',
        'address': '2574 Scott Manors\nPort Aprilfort, MI 13337',
        'mail': 'wgraham@hotmail.com',
        'birthdate': datetime.date(1927, 1, 19)
    },

    {
        'job': 'Engineer, civil (consulting)',
        'company': 'Guzman Inc',
        'ssn': '457-09-3674',
        'residence': '8014 Lambert Ways Apt. 285\nSouth Briannaside, KS 13217',
        'current_location': (
            Decimal('61.686331'),
            Decimal('-42.036583')
        ),
        'blood_group': 'A-',
        'username': 'lking',
        'name': 'Jeremy Wilson',
        'sex': 'M',
        'address': '9375 Thomas Alley Suite 536\nNorth Darren, AZ 22956',
        'mail': 'hdeleon@hotmail.com',
        'birthdate': datetime.date(1996, 10, 12)
    },

    {
        'job': 'Information officer',
        'company': 'Green Inc',
        'ssn': '230-42-2169',
        'residence': 'Unit 6625 Box 0858\nDPO AE 52466',
        'current_location': (
            Decimal('-78.802646'),
            Decimal('-47.996111')
        ),
        'blood_group': 'A-',
        'username': 'timothycastro',
        'name': 'Kenneth Rhodes',
        'sex': 'M',
        'address': '7994 Pearson Square\nHannahmouth, FM 16699',
        'mail': 'sonya72@hotmail.com',
        'birthdate': datetime.date(2003, 6, 15)
    },

    {
        'job': 'Contracting civil engineer',
        'company': 'Smith-Williamson',
        'ssn': '796-76-1297',
        'residence': '0041 Brittany Mountains\nNorth Harryshire, MN 69202',
        'current_location': (
            Decimal('66.422320'),
            Decimal('107.124001')
        ),
        'blood_group': 'AB+',
        'username': 'debraphillips',
        'name': 'Nicole Richardson',
        'sex': 'F',
        'address': '303 Wong Trafficway Suite 883\nLake Kiara, MN 78039',
        'mail': 'andrew33@gmail.com',
        'birthdate': datetime.date(2003, 9, 7)
    },

    {
        'job': 'Engineer, technical sales',
        'company': 'Moody-Meza',
        'ssn': '574-63-6422',
        'residence': '74438 Moore Fall\nSouth Andrew, GA 64257',
        'current_location': (
            Decimal('38.089195'),
            Decimal('35.459581')
        ),
        'blood_group': 'A+',
        'username': 'xlewis',
        'name': 'Gary Gamble',
        'sex': 'M',
        'address': '9929 Henderson Branch Suite 961\nLake Mary, AL 36478',
        'mail': 'ambercordova@yahoo.com',
        'birthdate': datetime.date(1968, 8, 19)
    }
]


def display_profiles():
    """Display the available profiles."""
    print("\nAvailable Profiles:")
    for number, profile in enumerate(profiles, start=1):
        print(f"{number}. {profile['name']}")


def query_profile(profile, choice):
    """Return the requested profile information."""

    if choice == "1":
        return "Name", profile["name"]

    elif choice == "2":
        return "DoB", profile["birthdate"]

    elif choice == "3":
        return "Sex", profile["sex"]

    elif choice == "4":
        return "Blood Type", profile["blood_group"]

    else:
        return None, None


def main():

    while True:

        display_profiles()

        try:
            profile_number = int(
                input("\nChoose a profile number (1-5): ")
            )

            if profile_number < 1 or profile_number > 5:
                print("Please choose a number from 1 to 5.")
                continue

        except ValueError:
            print("Please enter a valid number.")
            continue

        selected_profile = profiles[profile_number - 1]

        print("\nWhat information would you like to query?")
        print("1. Name")
        print("2. DoB")
        print("3. Sex")
        print("4. Blood Type")

        choice = input("\nEnter your choice (1-4): ")

        field_name, value = query_profile(
            selected_profile,
            choice
        )

        if field_name is None:
            print("Invalid selection.")
            continue

        print(f"\n{field_name}: {value}")

        encrypt_choice = input(
            "\nWould you like to encrypt this data? (yes/no): "
        ).lower()

        if encrypt_choice == "yes":

            encrypted_data = anonymizer.encrypt_text(
                str(value)
            )

            print("\nEncrypted Data:")
            print(encrypted_data)

        else:
            print("\nData was not encrypted.")

        again = input(
            "\nWould you like to make another query? (yes/no): "
        ).lower()

        if again != "yes":
            print("\nProgram ended.")
            break

if __name__ == "__main__":
    main()