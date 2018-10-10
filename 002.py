# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 12:32:00 2018

@author: Alperen Can
"""

from hashlib import md5
from getpass import getpass
import sys

print("Merhaba oyuna hoşgeldiniz!") 

attempts = 0
check_username = "0891c983837e60440be7b5e57afae60f"
check_password = "c4ca4238a0b923820dcc509a6f75849b"


while True: 
    username = input("Username: ")
    password = getpass(prompt='Password: ', stream=None)
    print()

    if attempts == 3:
        sys.exit("Too many failed attempts.")

    if md5('username'.encode("utf8")).hexdigest() == check_username:

        if md5('password'.encode("utf8")).hexdigest() == check_password:
            print("Username and password entered correctly.")
        else:
            print("Password entered incorrectly.")
            attempts += 1
    else:
        print("Username entered incorrectly.")
        attempts += 1