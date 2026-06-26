import string

def check_password_strength(password):
    score = 0

    # Check password length
    if len(password) >= 8:
        score += 1

    # Check uppercase letter
    if any(char.isupper() for char in password):
        score += 1

    # Check lowercase letter
    if any(char.islower() for char in password):
        score += 1

    # Check digit
    if any(char.isdigit() for char in password):
        score += 1

    # Check special character
    if any(char in string.punctuation for char in password):
        score += 1

    # Display strength
    if score == 8:
        return "🟢 Strong Password"
    elif score >= 5:
        return "🟡 Medium Password"
    else:
        return "🔴 Weak Password"


print("=" * 40)
print("      PASSWORD STRENGTH CHECKER")
print("=" * 40)

password = input("Enter Password: ")

result = check_password_strength(password)

print("\nPassword Strength:", result)