import secrets
import string


def generate_password():
    print("----- PASSWORD GENERATOR -----")

    try:
        length = int(input("Enter password length: "))

        if length < 4:
            print("Password length must be at least 4 characters.")
            return

        print("\nChoose character types:")
        print("1. Letters only")
        print("2. Letters and digits")
        print("3. Letters, digits, and symbols")

        choice = input("Enter your choice (1/2/3): ")

        if choice == "1":
            characters = string.ascii_letters
        elif choice == "2":
            characters = string.ascii_letters + string.digits
        elif choice == "3":
            characters = string.ascii_letters + string.digits + string.punctuation
        else:
            print("Invalid choice!")
            return

        # Generate secure password
        password = "".join(secrets.choice(characters) for _ in range(length))

        print("\nGenerated Password:", password)

    except ValueError:
        print("Invalid input! Please enter a valid number.")


# Program entry point
if __name__ == "__main__":
    generate_password()
