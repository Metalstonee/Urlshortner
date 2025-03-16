from pythonping import ping
import re
url = str(input("enter the url  "))
def valid(url):
    while True:
        url = input("Please enter a URL: ")
        pattern = re.compile(
            r"^https?://([a-zA-Z0-9-\.]+\.[a-zA-Z]{2,})(:[a-zA-Z0-9]+)?(/.*)?$"
        )
        if pattern.match(url):
            return url
        else:
            print("Invalid URL. Please try again.")



    
def connection(url):
    a = ping( url , verbose=True)
    print(a)

valid(url)
