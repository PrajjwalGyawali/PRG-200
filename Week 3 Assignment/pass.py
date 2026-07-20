passwords = ["hello", "Hello123", "H3ll0@World", "12345678", "MyP@ss!"]
special_chars = "!@#$%^&*"

for pwd in passwords:
    print(f"Checking: {pwd}")

    missing = []

    if len(pwd) < 8:
        missing.append("At least 8 characters long")

    has_upper = False
    has_lower = False
    has_digit = False
    has_special = False

    for ch in pwd:
        if ch.isupper():
            has_upper = True
        if ch.islower():
            has_lower = True
        if ch.isdigit():
            has_digit = True
        if ch in special_chars:
            has_special = True

    if not has_upper:
        missing.append("At least one uppercase letter")
    if not has_lower:
        missing.append("At least one lowercase letter")
    if not has_digit:
        missing.append("At least one digit")
    if not has_special:
        missing.append("At least one special character (!@#$%^&*)")

    if len(missing) == 0:
        print("-> Status: Strong Password")
    else:
        print("-> Status: Weak Password")
        print("   Missing criteria:")
        for reason in missing:
            print(f"   - {reason}")

    print("-" * 40)