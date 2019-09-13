import mechanicalsoup

my_browser = mechanicalsoup.Browser()
page = my_browser.get("https://realpython.com/practice/aphrodite.html")
print(page.soup)