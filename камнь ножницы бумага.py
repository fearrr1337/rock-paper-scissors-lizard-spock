import random

print("добро пожаловать в игру камень ножницы бумага ящерица спок!")
stop = int(input('Введите количество игр, которые хотите сыграть: '))
playerScore = 0
botScore = 0
for i in range(stop):
    answer = input('Что выберешь?\n ').lower()
    if answer == 'камень':
        answer = 'к'
    elif answer == 'ножницы':
        answer = 'н'
    elif answer == 'бумаг':
        answer = 'б'
    elif answer == 'спок':
        answer = 'с'
    elif answer == 'ящерица':
        answer = 'я'
    botAnswer = random.choice(['камень', 'ножницы', 'бумага', 'ящерица', 'спок'])
    print(f'A я выберу {botAnswer}')
    botAnswer = botAnswer[0]
    if answer == botAnswer:
        print('Ничья!')
        playerScore += 1
        botScore += 1
    elif (answer == 'к' and botAnswer == 'н') or \
         (answer == 'к' and botAnswer == 'я') or \
         (answer == 'н' and botAnswer == 'б') or \
         (answer == 'н' and botAnswer == 'я') or \
         (answer == 'б' and botAnswer == 'с') or \
         (answer == 'б' and botAnswer == 'к') or \
         (answer == 'с' and botAnswer == 'к') or \
         (answer == 'с' and botAnswer == 'н') or \
         (answer == 'я' and botAnswer == 'с') or \
         (answer == 'я' and botAnswer == 'б'):
        playerScore += 1
        print('Ты победил!')
    else:
        botScore += 1
        print('Победил я!')
if playerScore == botScore:
    print(f'По итогам {stop} ранудов, победила ничья!')
elif playerScore > botScore:
    print(f'По итогам {stop} раундов, ты победил!')
else:
    print(f'По итогам {stop} ранудов, победил я!')

