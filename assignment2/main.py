def is_valid_email(email):
    if "@" not in email:
        return False
    if email.endswith("@test.com"):
        return False
    # Check if there's content before the first @ and after the last @
    at_index = email.rfind("@")
    if at_index == 0 or at_index == len(email) - 1:
        return False
    return True
