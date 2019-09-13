from time import sleep
import mechanicalsoup

my_browser = mechanicalsoup.Browser()
for i in range(0, 3):
    page = my_browser.get("http://finance.yahoo.com/q?s=yhoo")
    html_text = page.soup

    my_tags = html_text.select("#yfs_l84_yhoo")
    my_price = my_tags[0].text
    print(f'The current price of YHOO is: {my_price}')
    if i<2: # wait a minute if this isn't the last request
        sleep(60)