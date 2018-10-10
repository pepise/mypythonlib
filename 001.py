# -*- coding: utf-8 -*-
"""
Created on Wed Oct 10 11:43:05 2018

@author: Alperen Can
"""

from hashlib import md5
from getpass import getpass
import sys

print("Hello! Welcome to FaceSnap!") 

attempts = 0
check_username = "0891c983837e60440be7b5e57afae60f"
check_password = "c20ad4d76fe97759aa27a0c99bff6710"


while True: 
    username = input("Username: ")
    password = getpass("Password: ")

    print()

    if attempts == 3:
        sys.exit("Too many failed attempts.")

    if mdpass.hexdigest() == password:
        if mdpass.hexdigest() == username:
                   print("YOu have logged in!")



#BROKEN ONE