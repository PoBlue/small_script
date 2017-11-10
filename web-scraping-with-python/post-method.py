import requests

"""
quiz 1 in page 121: POST method 

url: http://pythonscraping.com/pages/files/form.html
"""
def quiz_1():
    url = "http://pythonscraping.com/pages/files/processing.php"
    params = {'firstname': 'witcher', 'lastname': 'Mo'}

    r = requests.post(url, data=params)
    print(r.text)

"""
quiz 2 in page 125: Cookie

url: http://pythonscraping.com/pages/cookies/login.html
"""
def quiz_2():
    params = {'username':'witcher', 'password': 'password'}
    url = "http://pythonscraping.com/pages/cookies/welcome.php"
 
    r = requests.post(url, data=params)

    print("Cookie below")
    print(r.cookies.get_dict())
    print("-"*8)

    welcome_page = "http://pythonscraping.com/pages/cookies/profile.php"
    w_r = requests.get(welcome_page, cookies=r.cookies)
    print(w_r.text)


"""
quiz 3 in page 126: Handle Cookie with session
"""
def quiz3():
    session = requests.Session()
    params = {'username':'witcher', 'password': 'password'}

    url = "http://pythonscraping.com/pages/cookies/welcome.php"
    s = session.post(url, params)

    print("Cookie Below")
    print(s.cookies.get_dict())
    print("-" * 8)

    welcome_page = "http://pythonscraping.com/pages/cookies/profile.php"
    s = session.get(welcome_page)
    print(s.text)

quiz3()