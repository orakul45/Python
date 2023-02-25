import os
import shutil
import sys
from bank import bank
from victory import victory

allSum=0
historyBuy=()
while True:
    print('1. создать папку')
    print('2. удалить (файл/папку)')
    print('3. копировать (файл/папку)')
    print('4. просмотр содержимого рабочей директории')
    print('5. посмотреть только папки')
    print('6. посмотреть только файлы')
    print('7. просмотр информации об операционной системе')
    print('8. создатель программы')
    print('9. играть в викторину')
    print('10. мой банковский счет')
    print('11. смена рабочей директории (*необязательный пункт)')
    print('12. выход')


    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_folder=input('Введите название папки: ')
        if not os.path.exists(name_folder):
            os.mkdir(name_folder)
            print('Новая папка успешно создана!')
        else:
            print("Такая папка уже есть!")
    elif choice == '2':
        name_folder = input('Введите название папки/файла, которую надо удалить: ')
        os.rmdir(name_folder)
        print('Операция по удалению папки/файла успешно завершена!')
    elif choice == '3':
        name_folder = input("Введите название папки/файла, которую надо скопировать: ")
        name_new_folder = input("Введите новое название скопированной папки/файла: ")
        if os.path.exists(name_folder):
            shutil.copytree(name_folder, name_new_folder)
            print('Папка (файл) успешно скопирована!')
    elif choice == '4':
        print(os.listdir())

    elif choice == '5':
        for dirname, dirnames, filenames in os.walk('.'):
            # print path to all subdirectories first.
            for subdirname in dirnames:
                print(os.path.join(dirname, subdirname))
    elif choice == '6':
        for dirname, dirnames, filenames in os.walk('.'):
            for filename in filenames:
                print(os.path.join(dirname, filename))
    elif choice == '7':
        print(sys.platform)
    elif choice == '8':
        print('Поздняков Сергей')
    elif choice == '9':
        victory()
    elif choice == '10':
        bank()
    elif choice == '11':
        if not os.path.isdir("folder"):
            os.mkdir("folder")
        os.chdir("folder")
        print("Текущая директория изменилась на folder:", os.getcwd())
    elif choice == '12':
        break
    else:
        print('Неверный пункт меню')