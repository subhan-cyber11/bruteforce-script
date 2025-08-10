# Brute force example for password guessing (educational use only)

def brute_force_attack(password, wordlist):
    for guess in wordlist:
        guess = guess.strip()
        print(f"Trying password: {guess}")
        if guess == password:
            print(f"Password found: {guess}")
            return True
    print("Password not found in wordlist.")
    return False

# Example usage
if __name__ == "__main__":
    password_to_crack = "secret123"  # Target password (for demo)
    # Wordlist of possible passwords
    wordlist = ["123456", "password", "letmein", "secret123", "admin"]

    brute_force_attack(password_to_crack, wordlist)
Trying password: 123456
Trying password: password
Trying password: letmein
Trying password: secret123
Password found: secret123
