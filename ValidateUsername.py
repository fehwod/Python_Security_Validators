import re

def validate_username(username):
    if len(username) < 3:
        return (False, "Username должен содержать более 3 символов")
    if len(username) > 20:
        return (False, "Username должен содержать менее 20 символов")
    if not re.match(r"[A-Za-z]", username):
        return (False, "Username должен начинаться с буквы")
    if not re.fullmatch(r"[A-Za-z0-9_]+", username):
        return (False, "Username должен содержать только латинские буквы, цифры и подчеркивание")
    return (True, "OK")