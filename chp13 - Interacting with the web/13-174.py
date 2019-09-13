from urllib.request import urlopen, Request
import re

my_address = 'https://realpython.com/practice/dionysus.html'
req = Request(my_address)
req.add_header('User-Agent', 'curl/7.55.1')
html_page = urlopen(req)
html_text = html_page.read().decode('utf-8')

for prop in ['Name: ', 'Favorite Color: ']:
    start = html_text.find(prop) + len(prop)
    end = html_text[start:].find('<')
    print(html_text[start: start + end].strip(' \n'))

for prop in ['Name: ', 'Favorite Color: ']:
    pattern = f'{prop}(.*?)[<\n]'
    match_results = re.search(pattern, html_text, re.IGNORECASE)
    value = match_results.group(1)
    print(value.strip(' \n'))
