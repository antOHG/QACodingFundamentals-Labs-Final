class PasswordChecker:
    def __init__(self, password):
        """
        Constructor method that takes a password and initializes instance variables.
        """
        self.password = password

    def get_password_rating(self):
        """
        Method that returns a string indicating the rating of the password.
        """
        # Check for uppercase letters, lowercase letters, numbers, and special characters
        upper = False
        lower = False
        number = False
        special = False
        for char in self.password:
            if char.isupper():
                upper = True
            elif char.islower():
                lower = True
            elif char.isnumeric():
                number = True
            elif not char.isalnum():
                special = True
        
        # Check against common passwords
        common_passwords = ["password", "123456", "qwerty", "abc123", "letmein", "monkey", "password1", "12345678", "admin", "welcome"]
        if self.password.lower() in common_passwords:
            return "Very weak"

        # check strength
        if len(self.password) < 8:
            return "Weak"
        elif len(self.password) < 12 and (not upper or not lower or not number):
            return "Moderate"
        elif len(self.password) < 12 and upper and lower and number:
            return "Strong"
        elif len(self.password) < 16 and upper and lower and number and special:
            return "Strong"
        elif len(self.password) >= 16:
            return "Very strong"
        else:
            return "Moderate"


history = {}

while True:
    password = input("Enter a password: ")

    if password in history:
        print(f"Password rating: {history[password][-1]}")
    else:
        checker = PasswordChecker(password)
        rating = checker.get_password_rating()

        if password not in history:
            history[password] = []
        history[password].append(rating)

        print(f"Password rating: {rating}")
    
    print("History:")
    for password, ratings in history.items():
        print(f"Password: {password}")
        for rating in ratings:
            print(f" - Rating: {rating}")
    
    answer = input("Enter another password? (y/n): ")
    if answer.lower() != "y":
        break