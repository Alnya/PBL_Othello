"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""

import OthelloLogic as Ol
import copy
import time

"""
壁際を優先的にとりたい
theory_rateが0%の時でも、諦めないで良い手を探す
"""


def getAction(board, moves):
    start_time = time.time()
    turn = 61
    for i in board:
        turn -= i.count(0)
    # 先手turn:1 後手turn:2

    print("--------------------------------------------------")
    print(f"turn: {turn}")

    if turn == 2:
        turn_2 = turn2(moves)
        if turn_2 is not None:
            print(f"縦取り成功!\\(^_^)/")
            return turn_2
    if turn == 3:
        turn_3 = turn3(moves)
        if turn_3 is not None:
            print(f"兎定石だ!\\('o')/")
            return turn_3
    if turn < 15:
        move, rate = open_rate(board, moves)
        if type(rate) == str:
            print(f"turn: {turn}\n{rate}")
        else:
            print(f"turn: {turn}\nopen_rate: {rate} points")
        print(f"time: {time.time() - start_time:.2f} sec.")
        print(f"move: {move}")
        return move
    elif turn < 51:
        move, message = middle_check(board, moves)
        if message == "middle_check!":
            print(f"turn: {turn}\nmiddle_check: {message}")
        elif type(message) == str:
            print(f"turn: {turn}\n{message}")
        else:
            print(f"turn: {turn}\nopen_rate: {message} points")
        print(f"time: {time.time() - start_time:.2f} sec.")
        print(f"move: {move}")
        return move
    else:
        move, rate, ave_rate = complete(board, moves, turn, 1)
        print(f"turn: {turn}\ntheory_rate: {rate * 100:.2f} %\nave_rate: {ave_rate * 100:.2f} %")
        print(f"time: {time.time() - start_time:.2f} sec.")
        print(f"move: {move}")
        return move


def complete(board, moves, turn, player):
    tmp_board = copy.deepcopy(board)
    if len(moves) == 0:
        player *= -1
        moves = Ol.getMoves(board, player, 8)
    if len(moves) == 0:
        rate = win_rate(board)
        return None, rate, rate

    ans_move = moves[0]

    if turn == 60:
        next_board = Ol.execute(tmp_board, ans_move, player, 8)
        rate = win_rate(next_board)
        return ans_move, rate, rate

    w_rate = 0
    l_rate = 1
    sum_rate = 0
    ave_move = moves[0]
    ave_rate_max = 0
    for move in moves:
        # tmp_board = copy.deepcopy(board)
        # copy.deepcopyよりforで回した方が早い?
        for h in range(8):
            for w in range(8):
                tmp_board[h][w] = board[h][w]
        next_board = Ol.execute(tmp_board, move, player, 8)
        next_moves = Ol.getMoves(next_board, player * -1, 8)
        next_move, next_rate, next_ave_rate = complete(next_board, next_moves, turn + 1, player * -1)
        if w_rate < next_rate:
            w_rate = next_rate
            ans_move = move
        if l_rate > next_rate:
            l_rate = next_rate
        if ave_rate_max < next_ave_rate:
            ave_move = move
            ave_rate_max = next_ave_rate
        sum_rate += next_ave_rate
    ave_rate = float(sum_rate / len(moves))

    if player == 1:
        if w_rate == 0:
            return ave_move, w_rate, ave_rate
        else:
            return ans_move, w_rate, ave_rate
    else:
        return None, l_rate, ave_rate


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


def middle_check(board, moves):
    left_ls = [
        [0, 0],
        [0, 1],
        [0, 2],
        [0, 3],
        [0, 4],
        [0, 5],
        [0, 6],
        [0, 7],
    ]

    right_ls = [
        [7, 0],
        [7, 1],
        [7, 2],
        [7, 3],
        [7, 4],
        [7, 5],
        [7, 6],
        [7, 7],
    ]

    up_ls = [
        [0, 0],
        [1, 0],
        [2, 0],
        [3, 0],
        [4, 0],
        [5, 0],
        [6, 0],
        [7, 0],
    ]

    down_ls = [
        [0, 7],
        [1, 7],
        [2, 7],
        [3, 7],
        [4, 7],
        [5, 7],
        [6, 7],
        [7, 7],
    ]

    ls_manager = [up_ls, down_ls, left_ls, right_ls]

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

    for move in moves:
        if move in danger:
            continue
        elif move in list_first:
            return move, "middle_check!"
        for ls in ls_manager:
            if move in ls:
                tmp_board = copy.deepcopy(board)
                before_execute = for_middle_check(board, ls)
                next_board = Ol.execute(tmp_board, move, player=1, size=8)
                after_execute = for_middle_check(next_board, ls)
                next_moves = Ol.getMoves(next_board, player=-1, size=8)
                if before_execute + 1 < after_execute:
                    frag = 0
                    for next_move in next_moves:
                        if next_move in ls:
                            frag = 1
                    if frag == 1:
                        continue
                    else:
                        return move, "middle_check!"
                elif before_execute + 1 == after_execute:
                    enemy_stone = 0
                    for i in ls:
                        if board[i[1]][i[0]] == -1:
                            enemy_stone += 1
                    if enemy_stone == 0:
                        return move, "middle_check!"

    return open_rate(board, moves)


def for_middle_check(board, ls):
    ans = 0
    for i in ls:
        ans += board[i[1]][i[0]]
    return ans


def turn2(moves):
    turn_2_ls = [
        [3, 5],
        [4, 5],
        [3, 2],
        [4, 2]
    ]
    for move in moves:
        if move in turn_2_ls:
            return move
    return None


def turn3(moves):
    turn_3_ls = [
        [2, 4],
        [2, 3],
        [5, 4],
        [5, 3]
    ]
    for move in moves:
        if move in turn_3_ls:
            return move
    return None
