from bs4 import BeautifulSoup
from urllib.request import urlopen, Request

my_address = 'http://realpython.com/practice/dionysus.html'
req = Request(my_address)
req.add_header('User-Agent', 'curl/7.55.1')
html_page = urlopen(req)
html_text = html_page.read().decode('utf-8')

my_soup = BeautifulSoup(html_text, features="html.parser")
print(my_soup.get_text())
print(my_soup.find_all('img'))