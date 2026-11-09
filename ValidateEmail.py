import re

def validate_email(email):
    if len(email) < 5:
        return (False, "Email должен состоять из 5 и более символов")
    if len(email) > 50:
        return (False, "Email должен состоять менее чем 50 символов")
    if re.search(r'[<>"\';]', email):
        return (False, "Email не должен содержать запрещенные символы")
    if len(re.findall(r"@", email)) > 1:
        return (False, "Email должен содержать только один @")
    if email.count("@") != 1:
        return (False, "Email должен иметь один символ @")
    razdel_email = email.split("@")
    if len(razdel_email[0]) < 1:
        return (False, "Недопустимая длина")
    if len(razdel_email[1]) < 3:
        return (False, "Домен некоректной длины")
    if len(re.findall(r"\.", razdel_email[1])) < 1:
        return (False, "Домен должен содержать хотя бы одну .")
    if True:
        return (True, "OK")