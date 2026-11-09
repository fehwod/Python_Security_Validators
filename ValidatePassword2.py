import re
def validate_password(password):
    recomendations = []
    if len(password) < 8:
        recomendations.append("Пароль должен быть более 8 символов")
    if not re.search(r'[A-ZА-Я]', password):
        recomendations.append("Пароль должен содержать хотя бы одну заглавную букву") 
    if not re.search(r'[0-9]', password):
        recomendations.append("Пароль должен содержать хотя бы одну цифру")
    if not re.search(r'[!@#$%^&*]', password):
            recomendations.append("Пароль должен содержать хотя бы один специальный символ")
    return recomendations