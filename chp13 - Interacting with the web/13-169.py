from urllib.request import urlopen, Request

my_address = 'http://realpython.com/practice/aphrodite.html'
req = Request(my_address)
req.add_header('User-Agent', 'curl/7.55.1')
html_page = urlopen(req)

html_text = html_page.read().decode('utf-8')
print(html_text)
