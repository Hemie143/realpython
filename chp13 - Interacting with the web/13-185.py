import mechanicalsoup

my_browser = mechanicalsoup.Browser()
page = my_browser.get('http://finance.yahoo.com.com/q?s=yhoo')
html_text = page.soup
print(html_text)

my_tags = html_text.select("#yfs_l84_yhoo")
my_price = my_tags[0].text
print(f'The curent price of YHOO is {my_price}')