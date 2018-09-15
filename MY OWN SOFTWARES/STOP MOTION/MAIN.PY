import time
import sys
import random
import os

clear = lambda: os.system("cls")
clear()

printable = "THANK YOU FOR WATCHING"

print()
print()
print(" ",end = " ")
print(" ",end = " ")
print(" ",end = " ")
print(" ",end = " ")



for letter in printable:
    time.sleep(0.1)
    sys.stdout.write(letter)
    sys.stdout.flush()

input()