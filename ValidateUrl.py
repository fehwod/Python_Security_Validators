import re

def validate_url(url):
    if len(url) > 200:
        return (False, "URL должен содержать менее 200 символов")
    if len(url) < 10:
        return (False, "URL должен содержать более 10 символов")
    if re.search(r"[\'\"<>;]", url):
        return (False, "URL не должен содержать запрещенные символы")
    if not(re.match(r"https?://", url)):
        return (False, "URL должен начинаться с http:// или https://")
    razdel = url.split("://", 1)
    only_domain = razdel[1].split("/")
    if len(only_domain[0]) < 3:
        return (False, "Длина домена должна быть длинее 3 символов")
    return (True, "OK")