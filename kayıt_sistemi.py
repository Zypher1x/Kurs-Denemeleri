kayıt_durumu = False
kayıt_tekrar = False
giriş_durumu = False
giriş_tekrar = False
x = False

while x == False:
    print('Kayıt-Giriş-Çıkış')
    işlem = input().lower()


    if işlem == 'kayıt':
        if işlem == 'kayıt' and kayıt_durumu == True:
            print('Zaten Kayıtlısınız. Lütfen Giriş Yapınız.')

        while kayıt_tekrar == False:
            if kayıt_durumu == False:
                kayıt_kullanıcı_adı = input('Kullanıcı Adınızı Giriniz:')
                kayıt_şifre = input('Şifrenizi Giriniz:')
                kayıt_şifre_tekrar = input('Şifrenizi Tekrar Girniz:')

                if kayıt_şifre == kayıt_şifre_tekrar:
                    print('Başarılı Bir Şekilde Kayıt Oldunuz.')
                    print('Artık Giriş Yapabilirsiniz')
                    print('Kullanıcı Adınız:', kayıt_kullanıcı_adı, 'Şifreniz:', kayıt_şifre)
                    kayıt_durumu = True
                    kayıt_tekrar = True
                else:
                    print('Şifreleriniz Eşleşmiyor. Birdaha Deneyiniz.')

    elif işlem == 'giriş' and kayıt_durumu == False:
            print('Lütfen İlk Başta Kayıt Olunuz.')


    elif işlem == 'giriş':
        while giriş_tekrar == False:
            if kayıt_durumu == True:
                giriş_kullanıcı_adı = input('Kullanıcı Adınızı Giriniz:')
                giriş_şifre = input('Şifrenizi Giriniz:')
                if giriş_kullanıcı_adı == kayıt_kullanıcı_adı and giriş_şifre == kayıt_şifre:
                    print('Başarılı Bir Şekilde Giriş Yaptınız.')
                    giriş_durumu = True
                    giriş_tekrar = True
                    x = True
                else:
                    print('Kullanıcı Adınız yada Şifreniz Yanlış. Tekrar Deneyiniz')


    elif işlem == 'çıkış':
        print('Sistemden Çıkış Yapılıyor...')
        break

    else:
        print('Geçerli Bir İşlem Giriniz.')
                

    if kayıt_durumu == True and kayıt_tekrar == True and giriş_durumu == True and giriş_tekrar == True and x == True:
        break
