from datetime import datetime, date, time
def bank ():
    name = "НЕТ"
    histoty = []
    dt = datetime.now()
    dt_new = dt.strftime('%H:%M:%S - %m.%d.%Y')
    print(f'Сегодня {dt_new}')
    with open('balans.txt', 'r') as f:
        # 1. Прочитать сразу данные счета
        chet = f.read()
        if chet == 0:
            chet == float(0)
        else:
            chet = float(chet)
    print(f'Сейчас на счету {chet} руб')


    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')


        choice = input('Выберите пункт меню: ')
        if choice == '1':
            try:
                # Тот код который может вызвать исключение
                plus = float(input("Введите сумму на сколько пополнить счет: "))
                chet = chet + plus
                with open('balans.txt', 'w') as f:
                    f.write(str(chet))
                print(f'Сейчас на счету {chet} руб')
            except:
                # Этот блок срабатывает если было исключение
                print('Вы ввели не число')
                print('Введите верное число')
        elif choice == '2':
            try:
                 buy = float(input("Введите сумму покупки: "))
                 if buy>chet:
                    print("Денег не хватает")
                 else:
                    chet -= buy
                    name = (input("Введите название покупки: "))
                    histoty.append((name , buy))
                    with open('balans.txt', 'w') as f:
                        f.write(str(chet))
                    with open('buy.txt', 'a') as f:
                        dt = datetime.now()
                        dt_byu = dt.strftime('%H:%M:%S - %m.%d.%Y')
                        f.write("\n")
                        f.write(f'{dt_byu} ')
                        f.write(f' {name , buy}')
            except:
                # Этот блок срабатывает если было исключение
                print('Вы ввели не число')
                print('Введите верное число')

        elif choice == '3':
            print(f'Последние покупки:', histoty)
            with open('buy.txt', 'r') as f:
                # 1. Прочитать сразу все данные
                result = f.read()
                print(f'Все покупки:',result)
        elif choice == '4':
            break
        else:
            print('Неверный пункт меню')