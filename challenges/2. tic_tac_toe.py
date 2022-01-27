"""
Create a Tic Tac Toe game.
Here are the requirements:

- 2 players should be able to play the game (both sitting at the same computer)
- The board should be printed out every time a player makes a move
- You should be able to accept input of the player position and then place a symbol on the board
"""
from time import sleep


def print_board(p1, p2, bp):
    board = f"""
    {bp[1]} | {bp[2]} | {bp[3]}
    -----------
    {bp[4]} | {bp[5]} | {bp[6]} 
    -----------
    {bp[7]} | {bp[8]} | {bp[9]}"""
    print('\n' * 100)
    print(f'Markers of Player1:{p1}, Player2:{p2}')
    print(board)


def win_check(bp, position):
    win_probs = [(1, 2, 3),
                 (4, 5, 6),
                 (7, 8, 9),
                 (1, 4, 7),
                 (2, 5, 8),
                 (3, 6, 9),
                 (1, 5, 9),
                 (3, 5, 7)]
    for probs in win_probs:
        if position in probs:
            if bp[probs[0]] == bp[probs[1]] == bp[probs[2]]:
                return True
    return False


@property
def replay():
    return input('Play Again!!!, Enter Y|y|Yes').lower() in ['y', 'yes']


def get_player_markers():
    player1 = input("Please pick a marker 'X' or 'O'\n:")
    if player1.upper() == 'X':
        player2 = 'O'
    elif player1.upper() == 'O':
        player2 = 'X'
    else:
        print('Invalid Entry, so assigned default markers,')
        player1, player2 = 'X', 'O'
    return player1, player2


def tic_tac_toe():
    print('\n' * 100)
    print('Welcome To Tic Tac Toe Game!')
    new_game = True
    while new_game:
        player1, player2 = get_player_markers()
        bp = {1:' ', 2:' ', 3:' ', 4:' ', 5:' ', 6:' ', 7:' ', 8:' ', 9:' '}

        count = 1
        game_on = True
        while count < 10 and game_on:
            print_board(player1, player2, bp)
            position = int(input('Enter Marker position: '))
            if bp[position] != ' ':
                continue
            if count%2 != 0:
                bp[position] = player1
            else:
                bp[position] = player2
            if win_check(bp, position):
                print(f'{bp[position]} Won the match!!!')
                sleep(10)
                game_on = False
            count += 1
        else:
            print_board(player1, player2, bp)

        if replay:
            print('\n' * 100)
        else:
            new_game = False


if __name__ == "__main__":
    tic_tac_toe()
