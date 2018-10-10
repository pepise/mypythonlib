# @author alperencanesen
#this is one of my first attempts of username section of game





username = input("Kullanıcı adınızı girin : ")
password = input("Şifrenizi girin : ")
if (username == 'alperen') & (password == "123456"):
    print ("Merhaba " , username, " Oyuna hoşgeldin")
    command = input("Komut :")
    if command == "çıkış":
            print ("Çıkış yaptın ",username)
            
else:
    print ("Şifre veya kullanıcı adı yanlış! yeniden girin")

username = input("Kullanıcı adınızı girin : ")
password = input("Şifrenizi girin : ")
