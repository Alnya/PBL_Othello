"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""


# 序盤は少なく、終盤は多く。


def getAction(board, moves):
    turn = 61
    for i in board:
        turn -= i.count(0)
    # 先手turn:1 後手turn:2

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
        [1, 0],
        [1, 1],
        [0, 1],

        [6, 0],
        [7, 1],
        [6, 1],

        [7, 6],
        [6, 6],
        [6, 7],

        [1, 7],
        [0, 6],
        [1, 6]
    ]

    list_first = [
        [0, 0],
        [7, 0],
        [7, 7],
        [0, 7]
    ]

    list_second = [
        [2, 0],
        [5, 0],
        [7, 2],
        [7, 5],
        [5, 7],
        [2, 7],
        [0, 5],
        [0, 2]
    ]

    list_third = [
        [3, 0],
        [4, 0],
        [7, 3],
        [7, 4],
        [4, 7],
        [3, 7],
        [0, 4],
        [0, 3],
        [2, 2],
        [5, 2],
        [5, 5],
        [2, 5]
    ]

    if turn == 30 or turn == 31:
        for i in list_third:
            list_second.append(i)

    del_ls = []
    for i in range(4):
        if board[list_first[i][0]][list_first[i][1]] == 1:
            del_ls.append(i)
    for i in del_ls:
        for j in range(i * 3, (i * 3) + 3):
            list_first.append(danger[j])
    del_ls.sort(reverse=True)
    for i in del_ls:
        del danger[(i * 3):((i * 3) + 3)]

    if 35 < turn:
        max_index = moves[0]
        for move in moves:
            if move in danger:
                continue
            else:
                max_index = move
                break
        max_available = 0
        for move in moves:
            if move in list_first:
                return move
            if move in list_second:
                return move
            if move in danger:
                continue
            available = 0
            for dir in dirs:
                moved_index = [int(move[0] + dir[0]), int(move[1] + dir[1])]
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
    else:
        min_index = moves[0]
        for move in moves:
            if move in danger:
                continue
            else:
                min_index = move
                break
        min_available = 0
        for move in moves:
            if move in list_first:
                return move
            if move in list_second:
                return move
            if move in danger:
                continue
            available = 0
            for dir in dirs:
                moved_index = [int(move[0] + dir[0]), int(move[1] + dir[1])]
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
            if min_available > available:
                min_available = available
                min_index = move
        return min_index
