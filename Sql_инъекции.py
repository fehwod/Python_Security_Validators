import re

def detect_sqli(user_input):
    user_input = user_input.lower()
    
    if re.search(r"['\"]\s*(and|or)\b", user_input):
        return (False, "Обнаружен паттерн SQL-инъекции")
        
    if re.search(r"--", user_input):
        return (False, "Обнаружен паттерн SQL-инъекции")
        
    if re.search(r";\s*(drop|delete)", user_input):
        return (False, "Обнаружен паттерн SQL-инъекции")
        
    return (True, "Безопасно")