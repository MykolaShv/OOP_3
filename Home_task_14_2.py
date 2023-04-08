class ChessPiece():
    colour: str = 'white'
    place_figure = x_initial, y_initial = 5, 5

    def change_colour(self) -> str:
        if self.colour == 'white':
            self.colour = 'black'
        else:
            self.colour = 'white'
        return self.colour

    def valid_place(self, x, y) -> bool:
        return 0 < x < 9 and 0 < y < 9

    def check_potential_move(self, x, y) -> None:
        raise NotImplementedError

    def move_piece(self) -> str:
        return 'This piece has been moved'



class King(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        if abs(x - self.x_initial) <= 1 and abs(y - self.y_initial) <= 1:
            if self.valid_place(x, y):
                 print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Queen(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        if abs(x - y) == abs(self.x_initial - self.y_initial) \
                   or x == self.x_initial or y == self.y_initial:
            if self.valid_place(x, y):
                 print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Rook(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        if x == self.x_initial or y == self.y_initial:
            if self.valid_place(x, y):
                print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Rook(ChessPiece):
    def check_potential_move(self, x, b) -> bool:
        if self.valid_place(x, y) and x == self.x_initial or y == self.y_initial:
            if self.valid_place(x, y):
                print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Bishop(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        if abs(x - y) == abs(self.x_initial - self.y_initial):
            if self.valid_place(x, y):
                print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Knight(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        delta_x, delta_y = abs(x - self.x_initial), abs(y - self.y_initial)
        if (delta_x, delta_y) in [(2, 1), (1, 2)]:
            if self.valid_place(x, y):
                print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


class Pawn(ChessPiece):
    def check_potential_move(self, x, y) -> bool:
        if self.colour == 'white' and x == self.x_initial and y - self.y_initial == 1 \
                or self.colour == 'black' and x == self.x_initial and y - self.y_initial == -1:
            if self.valid_place(x, y):
                print(self.move_piece())
            return self.valid_place(x, y)
        else:
            return False


king = King()
queen = Queen()
rook = Rook()
bishop = Bishop()
knight = Knight()
pawn1 = Pawn()
pawn2 = Pawn()
pawn2.change_colour()

list_of_pieces = (king, queen, rook, bishop, knight, pawn1, pawn2)

def out_result(list_of_pieces, x, y) -> list:
    return [piece for piece in list_of_pieces if piece.check_potential_move(x, y)]


x, y = 6, 6
out_result(list_of_pieces, x, y)
x, y = 5, 6
out_result(list_of_pieces, x, y)
x, y = 5, 10
out_result(list_of_pieces, x, y)
x, y = -5, 6
out_result(list_of_pieces, x, y)
x, y = 5, 16
out_result(list_of_pieces, x, y)
x, y = 5, 4
out_result(list_of_pieces, x, y)
x, y = 5, 1
out_result(list_of_pieces, x, y)

