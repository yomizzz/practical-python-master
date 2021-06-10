"""
井字棋游戏

Version: 0.1
Author: yomi
Date: 2021-04-21
"""

import os 

def print_board(board):
    # 通过输入以下位置对应代码，在对应位置输出'x'和'o'
    print(board['TL'] + '|' + board['TM'] + '|' + board['TR'])
    print('-+-+-')
    print(board['ML'] + '|' + board['MM'] + '|' + board['MR'])
    print('-+-+-')
    print(board['BL'] + '|' + board['BM'] + '|' + board['BR'])

def main():
    init_board = {
        'TL': ' ', 'TM': ' ', 'TR': ' ',
        'ML': ' ', 'MM': ' ', 'MR': ' ',
        'BL': ' ', 'BM': ' ', 'BR': ' '
    }
    begin = True
    while begin:
        curr_board = init_board.copy()
        begin = False
        turn = 'x'
        counter = 0
        os.system('cls') # 原代码给出的是os.system('clear')，可能是linux命令，在win上无法使用
        print_board(curr_board)
        while counter < 9:
            move = input('轮到%s走棋，请输入位置： ' % turn)
            if curr_board[move] == ' ':
                counter += 1
                curr_board[move] = turn
                # 如果上一个走棋的是'x',则下一个转换为'o'
                if turn == 'x':
                    turn = 'o'
                else:
                    turn = 'x'
            # 清空屏幕，输出走棋后的内容
            os.system('cls')
            print_board(curr_board)
        choice = input('再玩一局?(yes|no)')
        begin = choice == 'yes'

if __name__ == '__main__':
    main()