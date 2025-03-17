
import re
def valid(url):
    while True:
        pattern = re.compile(
            r"^https?://([a-zA-Z0-9-\.]+\.[a-zA-Z]{2,})(:[a-zA-Z0-9]+)?(/.*)?$"
        )
        if pattern.match(url):
            return url
        else:
            print("Invalid URL. Please try again.")
            url = str(input("enter the url  "))
