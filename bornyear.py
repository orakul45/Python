# 6. (МОДУЛЬ 2) В проекте создать новый модуль bornyear.py
# 7. Написать программу используя условные операторы:
# - Спросить у пользователя год рождения А.С Пушкина
# - Если пользователь ввел верный год вывести 'Верно'
# - Если пользователь ошибся вывести 'Неверно'


birthday_Pushkin = '06.06.1799'
question = input('Когда родился А.С.Пушкин? (дд.мм.гггг): ')
print("Проверка: ", question)
if question == birthday_Pushkin:
     print("Правильно!")
else:
     print("Не правильно!")
     
     
# result
# Когда родился Пушкин? (дд.мм.гггг): 06.05.2000
# Проверка:  06.05.2000
# Не правильно!