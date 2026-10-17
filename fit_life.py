# Проект FitLife - MVP версия 1.1
# import sys
# import io

# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

WATER_NORM_PER_KG = 30
MIL_TO_LITR = 1000

# 1. Знакомство
while True:
    user_name = input('Как вас зовут? ')
    if user_name.strip():
        break
    print('Ошибка: Имя не может быть пустым. Попробуйте ввести ещё раз.')
# TODO: Спроси у пользователя имя и сохрани в переменную user_name
# print(user_name) # закомменть/удали потом строку

while True:
    try:
        user_age = int(input('Введите Ваш возраст: '))
        if user_age <= 0:
            print('Ошибка: Ваш возраст явно больше нуля. Попробуйте ещё раз')
            continue
        break
    except ValueError:
        print('Ошибка: пожалуйста, введите целое число лет, цифрами.')
# print(user_age) # закомменть/удали потом строку

# 2. Сбор данных
# TODO: Запроси вес (в кг) и сохрани в user_weight (тип float)
while True:
    try:
        user_weight = float(input('Пожалуйста, введите ваш вес, в "кг": '))
        if user_weight <= 0:
            print('Ошибка: Ваш вес явно больше нуля. Попробуйте ещё раз')
            continue
        break
    except ValueError:
        print('Ошибка: пожалуйста, введите целое число килограммах, цифрами.')
# print(user_weight) # закомменть/удали потом строку

while True:
    try:
        user_height = float(input('Пожалуйста, введите ваш рост в метрах: '))
        if user_height <= 0:
            print('Ошибка: Ваш рост явно выше уровня земли. Попробуйте ещё')
            continue
        break
    except ValueError:
        print('Ошибка: пожалуйста, введите ваш реальный рост в метрах.')
# print(user_height) # закомменть/удали потом строку

# 3. Логика расчетов (Функции как "черный ящик": используем арифметику)
bmi = user_weight / (user_height ** 2)
# Формула ИМТ: вес разделить на (рост в квадрате)
# TODO: Рассчитай bmi (Индекс массы тела)
# print ('Ваш идекс массы тела равен: ', round(bmi, 1))

# Подсчет воды: вес * 30 мл
water_needed = (user_weight * WATER_NORM_PER_KG) / MIL_TO_LITR
# TODO: Рассчитай water_needed
# print ('Ваша норма воды в литрах равна: ', water_needed)

# 4. Вывод красивого результата
print(f'Привет, {user_name}!')
# TODO: Выведи возраст, ИМТ (округленный до 1 знака) и норму воды.
print(f'Ваш индекс массы тела {round(bmi, 1)}, норма воды {water_needed} л.')
print('Расчет окончен. Будьте здоровы!')
