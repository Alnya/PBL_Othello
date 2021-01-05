"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""

import OthelloLogic as Ol
import copy
import time


def getAction(board, moves):
    start_time = time.time()
    turn = 61
    for i in board:
        turn -= i.count(0)
    # 先手turn:1 後手turn:2

    print("--------------------------------------------------")
    print(f"turn: {turn}")

    if 45 < turn:
        move, rate = complete(board, moves, turn, 1)
        print(f"turn: {turn}\nrate: {rate * 100:.2f} %")
        print(f"time: {time.time() - start_time:.2f} sec.")
        print(f"move: {move}")
        return move
    else:
        move, rate = open_rate(board, moves)
        print(f"turn: {turn}\nopen_rate: {rate} points")
        print(f"time: {time.time() - start_time:.2f} sec.")
        print(f"move: {move}")
        return move


def complete(board, moves, turn, player):
    tmp_board = copy.deepcopy(board)
    if len(moves) == 0:
        player *= -1
        moves = Ol.getMoves(board, player, 8)
    if len(moves) == 0:
        return None, win_rate(board)

    ans_move = moves[0]

    if turn == 60:
        next_board = Ol.execute(tmp_board, ans_move, player, 8)
        return ans_move, win_rate(next_board)

    w_rate = 0
    l_rate = 1
    sum_rate = 0
    for move in moves:
        next_board = Ol.execute(tmp_board, move, player, 8)
        next_moves = Ol.getMoves(next_board, player * -1, 8)
        next_move, next_rate = complete(next_board, next_moves, turn + 1, player * -1)
        if w_rate < next_rate:
            w_rate = next_rate
            ans_move = move
        if l_rate > next_rate:
            l_rate = next_rate
        sum_rate += next_rate
    ave_rate = float(sum_rate / len(moves))

    if player == 1:
        return ans_move, w_rate
    else:
        return None, ave_rate


def win_rate(board):
    my_stone = 0
    enemy_stone = 0
    for i in board:
        my_stone += i.count(1)
        enemy_stone += i.count(-1)
    if my_stone > enemy_stone:
        return 1
    else:
        return 0


def before_complete(board, moves, turn, player, end_turn):
    tmp_board = copy.deepcopy(board)
    if len(moves) == 0:
        player *= -1
        moves = Ol.getMoves(board, player, size=8)
    if len(moves) == 0:
        return None, weight_check(board)

    ans_move = moves[0]

    if turn == 60 or turn == end_turn:
        next_board = Ol.execute(tmp_board, ans_move, player, size=8)
        return ans_move, weight_check(next_board)

    ans_weight = -1000
    sum_weight = 0

    for move in moves:
        next_board = Ol.execute(tmp_board, move, player, size=8)
        next_moves = Ol.getMoves(next_board, player * -1, size=8)
        next_move, next_weight = before_complete(next_board, next_moves, turn + 1, player * -1, end_turn)
        if ans_weight < next_weight:
            ans_weight = next_weight
            ans_move = move
        sum_weight += next_weight
    ave_weight = float(sum_weight / len(moves))

    if player == 1:
        return ans_move, ans_weight
    else:
        return ans_move, ave_weight


def weight_check(board):
    weight_board = [
        [50, -22, 10, -1, -1, 10, -22, 50],
        [-22, -500, -3, -3, -3, -3, -500, -22],
        [10, -3, 5, -1, -1, 5, -3, 10],
        [-1, -3, -1, -1, -1, -1, -3, -1],
        [-1, -3, -1, -1, -1, -1, -3, -1],
        [10, -3, 5, -1, -1, 5, -3, 10],
        [-22, -500, -3, -3, -3, -3, -500, -22],
        [50, -22, 10, -1, -1, 10, -22, 50],
    ]
    ans = 0
    for h in range(8):
        for w in range(8):
            ans += board[h][w] * weight_board[h][w]
    return ans


def open_rate(board, moves):
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

    vectors = [
        [-1, -1],
        [0, -1],
        [1, -1],
        [-1, 0],
        [1, 0],
        [-1, 1],
        [0, 1],
        [1, 1]
    ]

    ans_move = moves[0]
    ans_rate = 100

    for move in moves:
        if move in danger:
            continue
        elif move in list_first:
            return move, "great!"
        rate = 0
        zero_board = [[0 for _ in range(8)] for _ in range(8)]
        tmp_board = copy.deepcopy(board)
        next_board = Ol.execute(tmp_board, move, player=1, size=8)
        for h in range(8):
            for w in range(8):
                if board[h][w] == -1 and next_board[h][w] == 1:
                    for vec in vectors:
                        moved_index = [int(h + vec[0]), int(w + vec[1])]
                        if 0 <= moved_index[0] <= 7 and 0 <= moved_index[1] <= 7:
                            zero_board[moved_index[0]][moved_index[1]] = 1
        for h in range(8):
            for w in range(8):
                if board[h][w] == 0 and zero_board[h][w] == 1:
                    rate += 1
        if rate < ans_rate:
            ans_rate = rate
            ans_move = move

    if ans_rate == 100:
        return open_rate_exception(board, moves)
    else:
        return ans_move, ans_rate


def open_rate_exception(board, moves):
    message = "open_rate_exception: success!"

    danger = [
        [1, 1],
        [1, 6],
        [6, 1],
        [6, 6]
    ]

    list_first = [
        [0, 0],
        [7, 0],
        [7, 7],
        [0, 7]
    ]

    ans_move = moves[0]
    success_frag = 0
    for move in moves:
        if move in danger:
            continue
        tmp_board = copy.deepcopy(board)
        next_board = Ol.execute(tmp_board, move, player=1, size=8)
        next_moves = Ol.getMoves(next_board, player=-1, size=8)
        for next_move in next_moves:
            if next_move in list_first:
                continue
        ans_move = move
        success_frag = 1
    if success_frag == 0:
        message = "open_rate_exception: failure..."
    return ans_move, message
