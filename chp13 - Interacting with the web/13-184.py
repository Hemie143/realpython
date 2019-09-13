import mechanicalsoup
from bs4 import BeautifulSoup

my_browser = mechanicalsoup.Browser()
login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "ThunderDude"

profiles_page = my_browser.submit(form, login_page.url)
print(f'Title: {profiles_page.soup.title.string}')

login_page = my_browser.get("https://realpython.com/practice/login.php")
login_html = login_page.soup
print(f'Title: {login_html.title.string}')

form = login_html.select("form")[0]
form.select("input")[0]["value"] = "zeus"
form.select("input")[1]["value"] = "password"

return_page = my_browser.submit(form, login_page.url)
if 'Wrong username or password' in return_page.soup.text:
    print('Login failed')
else:
    print('Login succeeded')
