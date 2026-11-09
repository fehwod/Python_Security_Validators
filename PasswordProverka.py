# Подключите модуль для работы с регулярными выражениями.
import re
# Создайте функцию password_recommendations(password).
def password_recommendations(password):
# Создайте пустой список для хранения рекомендаций.
    recommendations = []
# Проверьте длину пароля.
    if len(password) < 8:
        recommendations.append("Пароль должен быть длиньше 8 символов")
# Проверьте наличие заглавных букв.
    if not (re.findall(r'[A-Z]', password)):
        recommendations.append("Пароль должен иметь заглавную букву")
# Проверьте наличие строчных букв.
    if not (re.findall(r'[a-z]', password)):
        recommendations.append("Пароль должен содержать строчные буквы")
# Проверьте наличие цифр.
    if not (re.findall(r'[0-9]', password)):
        recommendations.append("Пароль должен содержать цифры")
# Проверьте наличие специальных символов.
    if not(re.findall(r'[^\w\s]', password)):
        recommendations.append("Пароль должен содержать специальные символы")
# Для каждого невыполненного требования
# добавьте соответствующую рекомендацию в список.
    if len(recommendations) == 0:
        recommendations.append("Пароль проходит по всем параметрам")
# Если список рекомендаций остался пустым,
# добавьте сообщение о соответствии пароля всем требованиям.
    return recommendations
# Верните список рекомендаций.
print(password_recommendations(""))