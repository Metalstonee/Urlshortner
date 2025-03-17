from validation import valid
from QR_CODE import genqr
import pyshorteners
url = str(input("enter the url  "))
valid(url)
s = pyshorteners.Shortener()
short = s.tinyurl.short(url)
genqr(url , "Shortendqr.png")
print(short)
f = open("Link.txt", "w")
f.write(f"Heres the Link !  =>  {short}")
f.close()
