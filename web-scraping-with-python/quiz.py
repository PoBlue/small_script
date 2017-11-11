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
def quiz_3():
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
def quiz_4():
    url = "http://pythonscraping.com/pages/javascript/ajaxDemo.html"
    path_to_this_project = "/Users/moweiquan/Desktop/mo_document/program/"
    path_to_phantomJS = "small_script/web-scraping-with-python/phantomjs-2.1.1-macosx/bin/phantomjs"
    driver = webdriver.PhantomJS(executable_path= path_to_this_project + path_to_phantomJS)
    driver.get(url)

    time.sleep(3)
    print(driver.find_element_by_id('content').text)
    driver.close()
    

"""
check header url: https://www.whatismybrowser.com
quiz 5 in page 155: customize header

Host
Connection: keep-alive
Accept: text/html and so on......    | describe type you want to receive
User-Agent: Chrome/39.0 and so on....| describe what your browser is
Referrer: https://www.google.com/    | describe where you jump from 
Accept-Encoding: gzip, deflate, sdch | describe what type of encoding to respone can be 
Accept-Language: en-US;              | describe which language of content should be responed
"""
from bs4 import BeautifulSoup
def quiz_5():
    session = requests.Session()

    headers = {
        'User-Agent': "Mozilla/ 5. 0 (Macintosh; Intel Mac OS X 10_ 9_ 5) AppleWebKit 537. 36 (KHTML, like Gecko) Chrome",
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8'
    }
    url = "https:// www. whatismybrowser.com/developers/what-http-headers-is-my-browser-sending"

    req = session.get(url, headers=headers)
    bsObj = BeautifulSoup(req.text)
    print(bsObj.find("table", {"class":"table-striped"}).get_text)


"""
quiz 6 in page 156: Handle cookie with PhantomJS: save and load

url: http://pythonscraping.com
"""
def quiz_6():
    path_to_this_project = "/Users/moweiquan/Desktop/mo_document/program/"
    path_to_phantomJS = "small_script/web-scraping-with-python/phantomjs-2.1.1-macosx/bin/phantomjs"
    driver = webdriver.PhantomJS(executable_path=path_to_this_project + path_to_phantomJS)
    
    url = "http://pythonscraping.com"
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())


"""
quiz 7 in page 158: save cookie for later use with PhantomJS

issue: set cookie, solve by: https://stackoverflow.com/a/37578697
or with execute_script: https://stackoverflow.com/a/37105419
or this issues to modify the source code: https://github.com/ariya/phantomjs/issues/13115
"""
def quiz_7():
    path_to_this_project = "/Users/moweiquan/Desktop/mo_document/program/"
    path_to_phantomJS = "small_script/web-scraping-with-python/phantomjs-2.1.1-macosx/bin/phantomjs"
    driver = webdriver.PhantomJS(executable_path=path_to_this_project + path_to_phantomJS)
    
    url = "http://pythonscraping.com"
    driver.get(url)
    driver.implicitly_wait(1)
    print(driver.get_cookies())

    savedCookies = driver.get_cookies()
    driver2 = webdriver.PhantomJS(executable_path=path_to_this_project+path_to_phantomJS)
    driver2.get(url)
    driver2.delete_all_cookies()

    ##First way: it is not work properly, Error: can not set
    # for cookie in savedCookies:
    #     # driver2.add_cookie(cookie)
    #     driver2.add_cookie({k: cookie[k] for k in ('name', 'value',  'path', 'expiry') if k in cookie})
    
    # second way to set cookies, just for value and name
    for cookie in savedCookies:
        print(cookie)
        driver2.add_cookie({
            'domain': '.pythonscraping.com',  # note the dot at the beginning
            'name': cookie['name'],
            'value': cookie['value'],
            'path': '/',
            'expires': None
        })

    driver2.get(url)
    driver.implicitly_wait(1)
    print(driver2.get_cookies())

quiz_7()
