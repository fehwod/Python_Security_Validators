import re


def analyze_log(log_text):

    ip = re.findall(r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}', log_text)
    
    counter_ip = {}
    
    for i in ip:
        counter_ip[i] = counter_ip.get(i, 0) + 1
    
    ip2 = []
    for i  in counter_ip.items():

        if i[1] > 2:
            ip2.append(f'{i[0]} Встречается {i[1]} раз(а)') 

    return ip2

print(analyze_log("""
192.168.1.10 - - [10/Nov/2026] "POST /login HTTP/1.1" 200
10.0.0.5 - - [10/Nov/2026] "GET /index.html HTTP/1.1" 200
192.168.1.10 - - [10/Nov/2026] "POST /login HTTP/1.1" 401
10.0.0.5 - - [10/Nov/2026] "GET /admin HTTP/1.1" 403
192.168.1.10 - - [10/Nov/2026] "POST /login HTTP/1.1" 401
8.8.8.8 - - [10/Nov/2026] "GET / HTTP/1.1" 200
8.8.8.8 - - [10/Nov/2026] "GET / HTTP/1.3" 700
8.8.8.8 - - [10/Nov/2026] "GET / HTTP/1.1" 200
"""))
