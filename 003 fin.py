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
check_username = "63a9f0ea7bb98050796b649e85481845"
check_password = "63a9f0ea7bb98050796b649e85481845"


while True: 
    username = input("Kullanıcı Adı: ")
    password = getpass("Şifre: ")

    print()

    if attempts == 3:
        sys.exit("Çok fazla yanlış girildi.")

    if md5(username.encode()).hexdigest() == check_username:
        if md5(password.encode()).hexdigest() == check_password: 
            #ANA KODU BURAYA KOY
            print("You have logged in.")
            command = input("Bir komut girin :")
        if command == "Oyunu oyna":
            #OYUN BAŞLANGICI
                print("oyun oynandı")
            #OYUN BİTİŞİ

            #ANA KODUN BİTŞİ
        else:
            print("Yanlış şifre.")
            attempts += 1
    else:
        print("Yanlış kullanıcı adı.")
        attempts += 1