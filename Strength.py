# Password Strength Checker

import re


def check_strength(password):
    """Score a password from 0 to 5 and list what it is missing."""
    score = 0
    tips = []

    if len(password) >= 8:
        score += 1
    else:
        tips.append("Use at least 8 characters")

    if re.search(r"[a-z]", password):
        score += 1
    else:
        tips.append("Add lowercase letters (a-z)")

    if re.search(r"[A-Z]", password):
        score += 1
    else:
        tips.append("Add uppercase letters (A-Z)")

    if re.search(r"\d", password):
        score += 1
    else:
        tips.append("Add numbers (0-9)")

    if re.search(r"[^A-Za-z0-9]", password):
        score += 1
    else:
        tips.append("Add symbols (e.g. ! @ # $)")

    levels = ["Very weak", "Weak", "Fair", "Good", "Strong", "Very strong"]
    return score, levels[score], tips


def main():
    print("=" * 40)
    print("      PASSWORD STRENGTH CHECKER")
    print("=" * 40)

    while True:
        password = input("\nEnter a password to test (or 'q' to quit): ")

        if password.lower() == "q":
            print("Goodbye!")
            break

        if password == "":
            print("Please type something.")
            continue

        score, level, tips = check_strength(password)
        print(f"Score:    {score}/5")
        print(f"Strength: {level}")

        if tips:
            print("How to improve it:")
            for tip in tips:
                print(f"  - {tip}")
        else:
            print("Great password - it meets all the checks!")

    input("\nPress Enter to close...")


if __name__ == "__main__":
    main()