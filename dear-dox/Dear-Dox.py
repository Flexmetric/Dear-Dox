import time
from colorama import init, Style

import social as sd
import ip as ipd, phone as phn

init()

resetstyle = Style.RESET_ALL
red = "\033[31m"
yellow = "\033[33m"
blue = "\033[34m"
reset = "\033[0m"

def logo():
    logo_text = """{}
  ____  _____    _    ______     _____    _________   __________
 |  _ \| ____|  / \   |   \_\   |  _  \  /  _    \ \  \ \  / / /
 | | | |  _|   / _ \  |___/_/   | | |  | | | |    | |  \ \/ / /
 | |_| | |___ / ___ \ |\  \ \   | |_|  | | |_|    | |  / /\ \ \ 
 |____/|_____/_/   \_\| \__\_\  |_____/  \_______/_/  /_/__\_\_\                
    {}""".format(red, reset)

    for line in logo_text.split('\n'):
        print(line)
        time.sleep(0.1)

    print(Style.BRIGHT + 'Загрузка...' + resetstyle)
    time.sleep(2)


def menu():
    while True:
        print('''{}
              Made by MEPTB1Y                                               
 _____    ___  ________  ___________    ________N  
 ||__/\__|  |  |   |__|  |  \ \ |  |   |  | | | 
 ||_/__\/|  |  |   |__|  |   \ \|  |   |  |_| | 
 ||//\__/|__|  |___|__|  |____\ \__|   |______| 
{}'''.format(red, reset))
        print('{}{}Главное меню{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
        print('{}{}1) Проверка NickName на соц.сети{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
        print('{}{}2) Проверка IP-адреса{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
        print('{}{}3) Проверка по номеру телефона{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
        print(' {}{}0) ! ВЫХОД !'.format(Style.BRIGHT, red, reset, resetstyle))
        home_page = int(input('\n {}[+] Cделайте выбор: {}'.format(red, reset)))

        if home_page == 0:
            print('\n {}{}До свидания!{}{}'.format(Style.BRIGHT, red, reset, resetstyle))
            break
        elif home_page == 1:
            sd.SocialDeanon()
        elif home_page == 2:
            ipd.Ipcheck()
        elif home_page == 3:
            phn.PhoneNumber()
        else:
            print(' {}Введите существующий пункт меню!{}'.format(red, reset))
            continue


if __name__ == '__main__':
    logo()
    menu()
