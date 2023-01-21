def input_money(text):
    return (input(text))


def p_hist(hist):
    for j in hist:
        print(j[0], '  ', j[1])
    pass


def bank():
    money = 0.00
    hist = []
    while True:
        print('1. пополнение счета')
        print('2. покупка')
        print('3. история покупок')
        print('4. выход')

        ch = input('Выберите пункт меню: ')
        if ch == '1':
            money += float(input_money('Введите сумму пополнения: '))
            pass
        elif ch == '2':
            deb = float(input_money('Введите сумму покупки: '))
            if deb > money:
                print('Сумма покупки больше доступного остатка')
            else:
                s = input_money('Введите название покупки: ')
                money = money - deb
                hist.append([s, deb])
            pass
        elif ch == '3':
            p_hist(hist)
            pass
        elif ch == '4':
            ch = '0'
            return
        else:
            print('Неверный пункт меню')
