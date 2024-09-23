import random

up_let = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
low_let = up_let.lower()
digits = "0123456789"
symbols = "@#$%^&*()_+-={()}[]|:;<>,.?/~ "

upper, lower, nums, syms = True, True, True, True 


password = ""
all = ""

if upper:
    all += up_let
if lower:
    all += low_let
if nums:
    all += digits
if symbols:
    all += symbols


length = 20
amount = 10 

for x in range(amount):
    password = "".join(random.sample(all, length))
    print(password)




