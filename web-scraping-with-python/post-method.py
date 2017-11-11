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


"""
url of quiz is: http://pythonscraping.com/pages/javascript/ajaxDemo.html
quiz 4 in page 132: Handle JS and AJAX

install selenium: https://pypi.python.org/pypi/selenium
install PhantomJS: https://github.com/ariya/phantomjs
PhantomJS in mac: https://ariya.io/2012/02/phantomjs-and-mac-os-x
PhantomJS in Linux: https://stackoverflow.com/questions/8778513/how-can-i-setup-run-phantomjs-on-ubuntu
"""
from selenium import webdriver
import time
def quiz4():
    url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
    path_to_this_project = "/Users/moweiquan/Desktop/mo_document/program/"
    path_to_phantomJS = "small_script/web-scraping-with-python/phantomjs-2.1.1-macosx/bin/phantomjs"
    driver = webdriver.PhantomJS(executable_path= path_to_this_project + path_to_phantomJS)
    driver.get(url)

    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    driver.close()
    
quiz4()
