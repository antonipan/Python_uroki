print ('hello world')
# Программа записывает в файл слова, читает их, 
# Ищет среди них слова "о" и "л" и записывает в новый файл
words = open('words.txt', 'w', encoding='utf-8')
for _ in range(6):
    words.writelines(input('Введите слово: '))
    words.writelines('\n')
words.close()

some_list = list(open('words.txt', 'r', encoding='utf-8'))
# print(some_list)
out_list = []
for i in range (0, len(some_list)):
    if 'о' and 'л' not in some_list[i]:
        replace = some_list[i]
        some_list[i] = replace[:-1]
        out_list.append(some_list[i])      
# print(out_list)

data = open('res_words.txt', 'w', encoding='utf-8')
for i in out_list:
    data.writelines(i)
    data.writelines('\n')
data.close()

# Игра в крестики-нолики на двух игроков, игровое поле - 3х3.


print('Перед вами игровое поле')
gameBoard = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
print(f'| {gameBoard[0]} || {gameBoard[1]} || {gameBoard[2]} |', 
    f'| {gameBoard[3]} || {gameBoard[4]} || {gameBoard[5]} |',
    f'| {gameBoard[6]} || {gameBoard[7]} || {gameBoard[8]} |', sep='\n')

def pole (playing, step_game, gameBoard):
        if playing == 1:
            gameBoard[int(step_game)-1] = 'x'
        else:
            gameBoard[int(step_game)-1] = 'o'
        print(f'| {gameBoard[0]} || {gameBoard[1]} || {gameBoard[2]} |', 
            f'| {gameBoard[3]} || {gameBoard[4]} || {gameBoard[5]} |',
            f'| {gameBoard[6]} || {gameBoard[7]} || {gameBoard[8]} |', sep='\n')
player_1 = 'x'
player_2 = 'o'
playing = 1
count = 1
pobeda = ['123', '456', '789', '147', '258', '369', '159', '357']


def hod (pobeda, player, game_step):
    step_pobeda = []
    for i in pobeda:
        marker = True
        for j in i:
            if j == game_step:
                output_i = i.replace(game_step, player)
                step_pobeda.append(output_i)
                marker = False
        if marker == True:
            step_pobeda.append(i)
    return step_pobeda


while 'ooo' not in pobeda and 'xxx' not in pobeda:
    print(f'Ход {count}')
    game_step = input(f'Игрок {playing} ходит: ')
    if playing == 1:
        pobeda = hod (pobeda, player_1, game_step)
        pole(playing, game_step, gameBoard)
        playing = 2
    elif playing == 2:
        pobeda = hod (pobeda, player_2, game_step)
        pole(playing, game_step, gameBoard)
        playing = 1
    count += 1
    print(pobeda)

if playing == 1: 
    playing = 2
    print(f'Игрок {playing} победил!!!')
elif playing == 2: 
    playing = 1
    print(f'Игрок {playing} победил!!!')