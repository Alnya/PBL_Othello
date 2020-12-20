"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""

# strong


import OthelloLogic as ol


def getAction(board, moves):
    ans = moves[0]
    tmp = 0
    for move in moves:
        next_board = ol.execute(board, move, 1, 8)
        next_moves = ol.getMoves(next_board, -1, 8)
        if tmp < len(next_moves):
            ans = move
    return ans
