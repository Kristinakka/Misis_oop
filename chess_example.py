class Figuire:
    def __init__(self, name, color, position):
        self.name = name
        self.color = color
        self.position = position

    def get_info(self):
        return f"{self.color} {self.name} находится на клетке {self.position}"

    def move(self, new_position):
        raise NotImplementedError("Метод move() должен быть переопределён.")
    


class Knight(Figuire):
    def __init__(self, color, position):
        super().__init__("Knight", color, position)
        self.symbol = "N"

    def move(self, new_position):
        old_col = self.position[0]
        old_row = int(self.position[1])

        new_col = new_position[0]
        new_row = int(new_position[1])

        col_diff = abs(ord(new_col) - ord(old_col))
        row_diff = abs(new_row - old_row)

        if (col_diff, row_diff) in [(1, 2), (2, 1)]:
            self.position = new_position
            return True, f"Конь переместился на {self.position}"

        return False, f"Недопустимый ход коня: {self.position} -> {new_position}"
        

#
class Rook(Figuire):
    def __init__(self, color, position):
        super().__init__("Rook", color, position)
        self.symbol = "R"

    def move(self, new_position):
        old_col = self.position[0]
        old_row = self.position[1]

        new_col = new_position[0]
        new_row = new_position[1]

        if old_col == new_col or old_row == new_row:
            self.position = new_position
            return True, f"Ладья переместилась на {self.position}"

        return False, f"Недопустимый ход ладьи: {self.position} -> {new_position}"
        

#
class Bishop(Figuire):
    def __init__(self, color, position):
        super().__init__("Bishop", color, position)
        self.symbol = "B"

    def move(self, new_position):
        old_col = ord(self.position[0])
        old_row = int(self.position[1])

        new_col = ord(new_position[0])
        new_row = int(new_position[1])

        if abs(new_col - old_col) == abs(new_row - old_row):
            self.position = new_position
            return True, f"Слон переместился на {self.position}"

        return False, f"Недопустимый ход слона: {self.position} -> {new_position}"
        

#


# class ChessGame:
#     def move_piece(self, piece, new_position):
#         if isinstance(piece, Knight):
#             print("Ход коня")
#         elif isinstance(piece, Rook):
#             print("Ход ладьи")
#         elif isinstance(piece, Bishop):
#             print("Ход слона")


class ChessGame:
    def __init__(self):
        self.pieces = {}

    def add_piece(self, piece):
        self.pieces[piece.position] = piece

    def show_board_state(self):
        print("Текущее состояние доски:")
        for position, piece in self.pieces.items():
            print(f"{position}: {piece.get_info()}")

    def move_piece(self, from_position, to_position):
        piece = self.pieces.get(from_position)

        if piece is None:
            print(f"На клетке {from_position} нет фигуры.")
            return

        success, message = piece.move(to_position)
        print(message)

        if success:
            del self.pieces[from_position]
            self.pieces[to_position] = piece

#
print()
print()
game = ChessGame()
game.add_piece(Knight("White", "g1"))
game.add_piece(Rook("Black", "a8"))
game.add_piece(Bishop("White", "c1"))

game.show_board_state()
print()

game.move_piece("g1", "f3")
game.move_piece("a8", "a5")
game.move_piece("c1", "h6")
print()

game.show_board_state()
print()

