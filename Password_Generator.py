import random
import string

def generate_password(length, use_uppercase=True, use_lowercase=True, use_digits=True, use_special_chars=True):
    """Generate a random password based on user preferences."""
    # Build the character pool based on user preferences
    char_pool = ''
    
    if use_uppercase:
        char_pool += string.ascii_uppercase  # A-Z
    if use_lowercase:
        char_pool += string.ascii_lowercase  # a-z
    if use_digits:
        char_pool += string.digits  # 0-9
    if use_special_chars:
        char_pool += string.punctuation  # Special characters like @, #, $, etc.

    # Ensure the pool is not empty
    if not char_pool:
        raise ValueError("At least one character type must be selected.")

    # Generate a random password using the character pool
    password = ''.join(random.choice(char_pool) for _ in range(length))

    return password

def get_password_length():
    """Prompt the user for the password length and validate the input."""
    while True:
        try:
            length = int(input("Enter the desired password length: "))
            if length < 6:
                print("Password length should be at least 6 characters.")
            else:
                return length
        except ValueError:
            print("Invalid input! Please enter a number.")

def get_user_preferences():
    """Prompt the user for character type preferences."""
    print("\nSelect the types of characters to include in your password:")
    
    use_uppercase = input("Include uppercase letters? (y/n): ").lower() == 'y'
    use_lowercase = input("Include lowercase letters? (y/n): ").lower() == 'y'
    use_digits = input("Include numbers? (y/n): ").lower() == 'y'
    use_special_chars = input("Include special characters? (y/n): ").lower() == 'y'
    
    return use_uppercase, use_lowercase, use_digits, use_special_chars

def main():
    """Main function to run the password generator."""
    print("Random Password Generator")

    # Get user preferences for password generation
    use_uppercase, use_lowercase, use_digits, use_special_chars = get_user_preferences()

    # Get password length
    length = get_password_length()

    # Generate the password
    try:
        password = generate_password(length, use_uppercase, use_lowercase, use_digits, use_special_chars)
        # Display the generated password
        print(f"\nYour generated password is: {password}")
    except ValueError as e:
        print(f"\nError: {e}")

    # Ask the user if they want to generate another password
    again = input("\nDo you want to generate another password? (y/n): ").lower()
    if again == 'y':
        main()
    else:
        print("Exiting the program. Goodbye!")

if __name__ == "__main__":
    main()
