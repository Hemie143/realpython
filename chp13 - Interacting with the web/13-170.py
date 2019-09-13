from urllib.request import urlopen, Request

my_address = 'http://realpython.com/practice/aphrodite.html'
req = Request(my_address)
req.add_header('User-Agent', 'curl/7.55.1')
html_page = urlopen(req)

html_text = html_page.read().decode('utf-8')
start_tag = "<title>"
end_tag = "</title>"

start_index = html_text.find(start_tag) + len(start_tag)
end_index = html_text.find(end_tag)

print(html_text[start_index:end_index])
