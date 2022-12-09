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


while 'ooo' or 'xxx' not in pobeda:
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
    print(f'Ход {count}')
    
print(f'Игрок {playing} победил!!!')
