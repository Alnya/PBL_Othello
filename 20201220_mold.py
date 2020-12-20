"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""

# mold


import OthelloLogic as ol


def getAction(board, moves, turn):
    if turn < 5:
        tatedori = sente_tatedori(board)
        if tatedori is not None and tatedori in moves:
            return tatedori
        tatedori = gote_tatedori(board)
        if tatedori is not None and tatedori in moves:
            return tatedori
        usi = sente_usi(board)
        if usi is not None and usi in moves:
            return usi
    return moves[0]


def sente_tatedori(board):
    tatedori1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, -1, 1, 0, 0, 0],
                 [0, 0, 0, -1, 1, 1, 0, 0],
                 [0, 0, 0, -1, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    tatedori2 = []
    for i in range(len(tatedori1)):
        tatedori2.append(tatedori1[len(tatedori1) - i - 1])
    tatedori3 = []
    for i in tatedori1:
        tmp = []
        for j in range(len(i)):
            tmp.append(i[len(i) - j - 1])
        tatedori3.append(tmp)
    tatedori4 = []
    for i in range(len(tatedori3)):
        tatedori4.append(tatedori3[len(tatedori3) - i - 1])

    if board == tatedori1:
        return [4, 2]
    elif board == tatedori2:
        return [3, 2]
    elif board == tatedori3:
        return [4, 5]
    elif board == tatedori4:
        return [3, 5]
    else:
        return None


def gote_tatedori(board):
    tatedori1 = [[0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 1, -1, 0, 0, 0],
                 [0, 0, 0, -1, -1, -1, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0]]
    tatedori2 = []
    for i in range(len(tatedori1)):
        tatedori2.append(tatedori1[len(tatedori1) - i - 1])
    tatedori3 = []
    for i in tatedori1:
        tmp = []
        for j in range(len(i)):
            tmp.append(i[len(i) - j - 1])
        tatedori3.append(tmp)
    tatedori4 = []
    for i in range(len(tatedori3)):
        tatedori4.append(tatedori3[len(tatedori3) - i - 1])

    if board == tatedori1:
        return [5, 3]
    elif board == tatedori2:
        return [2, 3]
    elif board == tatedori3:
        return [5, 4]
    elif board == tatedori4:
        return [2, 4]
    else:
        return None


def sente_usi(board):
    usi1 = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    usi2 = [[0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, -1, 1, 0, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0]]

    usi3 = []
    for i in range(len(usi1)):
        usi3.append(usi1[len(usi1) - i - 1])

    usi4 = []
    for j in range(len(usi2)):
        usi4.append(usi2[len(usi2) - j - 1])

    if board == usi1:
        return [4, 5]
    elif board == usi2:
        return [3, 2]
    elif board == usi3:
        return [2, 3]
    elif board == usi4:
        return [5, 4]
    else:
        return None
