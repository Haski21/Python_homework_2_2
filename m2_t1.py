'''
Задача №2
В заданной строке найти количество вхождений символа 'a'
Используем индексы для получения значения каждого элемента строки
'''

string = input('enter string:')
counter = len(string)
COUNTER_A = 0

while counter:
#      string[counter - 1] == 'a' or string[counter - 1] == 'A':
    if string[counter - 1] == 'a':
#      counter_a ++; а есть что-то похожее на СИ++?)
        COUNTER_A += 1
        counter -= 1
    else:
        counter -= 1
print('find symbol "a":',COUNTER_A)