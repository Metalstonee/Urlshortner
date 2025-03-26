from validation import valid
from QR_CODE import genqr
import pyshorteners
from colorama import Fore, Back, Style
from os import system
from saving_methods import clipboard
print(Style.DIM  + ''' 

  _    _        _    _____  _                   _                      
 | |  | |      | |  / ____|| |                 | |                     
 | |  | | _ __ | | | (___  | |__    ___   _ __ | |_  _ __    ___  _ __ 
 | |  | || '__|| |  \___ \ | '_ \  / _ \ | '__|| __|| '_ \  / _ \| '__|
 | |__| || |   | |  ____) || | | || (_) || |   | |_ | | | ||  __/| |   
  \____/ |_|   |_| |_____/ |_| |_| \___/ |_|    \__||_| |_| \___||_|   


              

  / __ 
 ( (__) |___ ___
  \________,'   """""----....____
   _______<  () dd       ____----'
  / __   __`.___-----""""
 ( (__) |
  \____/

                                                                       


''')
url = str(input("enter the url  "))
system("cls")
valid(url)
s = pyshorteners.Shortener()
short = s.tinyurl.short(url)
genqr(url , "Shortendqr.png")
print(short)
clipboard(short)
f = open("Link.txt", "w")
f.write(f"Heres the Link !  =>  {short}")
f.close()
