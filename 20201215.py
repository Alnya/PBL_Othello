"""
引数について

board:現在の盤面の状態
moves:現在の合法手の一覧

詳しい説明はサイトのHomeページをご覧ください。

"""


def getAction(board, moves):
    first_suggestion = FirstSuggestion(board, moves)
    return first_suggestion.main()


class FirstSuggestion:
    def __init__(self, board, moves):
        self.board = board
        self.moves = moves

    def main(self):
        return self.priority_first()

    def test(self):
        ls = [[0] * 8 for _ in range(8)]
        for i in self.list_first:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_second:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_third:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_fourth:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_fifth:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_sixth:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in self.list_seventh:
            a = i[0]
            b = i[1]
            ls[a][b] = 1
        for i in range(8):
            for j in range(8):
                print(ls[i][j], end="")
            print()

    list_first = [[0, 0],
                  [7, 0],
                  [7, 7],
                  [0, 7]]

    list_second = [[2, 0],
                   [5, 0],
                   [7, 2],
                   [7, 5],
                   [5, 7],
                   [2, 7],
                   [0, 5],
                   [0, 2]]

    list_third = [[3, 0],
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
                  [2, 5]]

    list_fourth = [[3, 2],
                   [4, 2],
                   [5, 3],
                   [5, 4],
                   [4, 5],
                   [3, 5],
                   [2, 4],
                   [2, 3]]

    list_fifth = [[2, 1],
                  [3, 1],
                  [4, 1],
                  [5, 1],
                  [6, 2],
                  [6, 3],
                  [6, 4],
                  [6, 5],
                  [5, 6],
                  [4, 6],
                  [3, 6],
                  [2, 6],
                  [1, 5],
                  [1, 4],
                  [1, 3],
                  [1, 2]]

    list_sixth = [[1, 0],
                  [6, 0],
                  [7, 1],
                  [7, 6],
                  [6, 7],
                  [1, 7],
                  [0, 6],
                  [0, 1]]

    list_seventh = [[1, 1],
                    [6, 1],
                    [6, 6],
                    [1, 6]]

    def priority_first(self):
        for i in self.moves:
            if i in self.list_first:
                return i
        return self.priority_second()

    def priority_second(self):
        for i in self.moves:
            if i in self.list_second:
                return i
        return self.priority_third()

    def priority_third(self):
        for i in self.moves:
            if i in self.list_third:
                return i
        return self.priority_fourth()

    def priority_fourth(self):
        for i in self.moves:
            if i in self.list_fourth:
                return i
        return self.priority_fifth()

    def priority_fifth(self):
        for i in self.moves:
            if i in self.list_fifth:
                return i
        return self.priority_sixth()

    def priority_sixth(self):
        for i in self.moves:
            if i in self.list_sixth:
                return i
        return self.priority_seventh()

    def priority_seventh(self):
        for i in self.moves:
            if i in self.list_seventh:
                return i
        return self.moves[0]


if __name__ == '__main__':
    test = FirstSuggestion([[0, 0]], [[0, 0]])
    test.test()
