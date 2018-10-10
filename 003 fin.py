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