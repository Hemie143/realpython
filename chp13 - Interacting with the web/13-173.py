from urllib.request import urlopen, Request
import re

my_address = 'http://realpython.com/practice/dionysus.html'
req = Request(my_address)
req.add_header('User-Agent', 'curl/7.55.1')
html_page = urlopen(req)

html_text = html_page.read().decode('utf-8')
match_results = re.search("<title.*?>.*</title.*?>", html_text, re.IGNORECASE)

title = match_results.group()
title = re.sub("<.*?>", "", title)
print(title)
