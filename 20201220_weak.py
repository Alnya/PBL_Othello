"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""


# weak


def getAction(board, moves):
    dirs = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1]
    ]
    danger = [
        [0, 0],
        [0, 7],
        [7, 0],
        [7, 7]
    ]
    max_index = moves[0]
    max_available = 0
    for move in moves:
        if move in danger:
            continue
        available = 0
        for dir in dirs:
            moved_index = [move[0] + dir[0], move[1] + dir[1]]
            tmp = 0
            frag = 0
            while 0 <= moved_index[0] <= 7 and 0 <= moved_index[1] <= 7:
                if board[moved_index[0]][moved_index[1]] == -1:
                    tmp += 1
                elif board[moved_index[0]][moved_index[1]] == 1:
                    frag = 1
                    break
                else:
                    tmp = 0
                moved_index[0] += dir[0]
                moved_index[1] += dir[1]
            if frag == 1:
                available += tmp
        if max_available < available:
            max_available = available
            max_index = move
    return max_index
