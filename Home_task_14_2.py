class ChessFigure():
    colour: str = 'white'
    place_figure = x, y = 5, 5

    def change_colour(self) -> str:
        if self.colour == 'white':
            self.colour = 'black'
        else:
            self.colour = 'white'
        return self.colour

    def valid_place(self, a, b) -> bool:
        return 0 < a < 9 and 0 < b < 9

    def check_potential_move(self, a, b) -> None:
        raise NotImplementedError


class King(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            return abs(a - self.x) <= 1 and abs(b - self.y) <= 1


class Queen(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            return abs(a - b) == abs(self.x - self.y) or a == self.x or b == self.y


class Rook(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            return abs(a - b) == abs(self.x - self.y)


class Bishop(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            return a == self.x or b == self.y


class Knight(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            delta_x, delta_y = abs(a - self.x), abs(b - self.y)
            return delta_x == 1 and delta_y == 2 or delta_x == 2 and delta_y == 1


class Pawn(ChessFigure):
    def check_potential_move(self, a, b) -> bool:
        if self.valid_place(a, b):
            return self.colour == 'white' and a == self.x and b - self.y == 1 \
                   or self.colour == 'black' and a == self.x and b - self.y == -1


king = King()
queen = Queen()
rook = Rook()
bishop = Bishop()
knight = Knight()
pawn1 = Pawn()
pawn2 = Pawn()
pawn2.change_colour()

list_of_figures = (king, queen, rook, bishop, knight, pawn1, pawn2)
list_for_print = ('king', 'queen', 'rook', 'bishop', 'knight', 'pawn1', 'pawn2')


def out_result(list_of_figures, a, b) -> list:
    list_answer = ([_.check_potential_move(a, b) for _ in list_of_figures])
    zip_answer = zip(list_for_print, list_answer)
    answer_figures = []
    for key, value in zip_answer:
        if value:
            answer_figures.append(key)
    print(answer_figures)


a, b = 6, 6
out_result(list_of_figures, a, b)
a, b = 5, 6
out_result(list_of_figures, a, b)
a, b = 5, 10
out_result(list_of_figures, a, b)
a, b = -5, 6
out_result(list_of_figures, a, b)
a, b = 5, 16
out_result(list_of_figures, a, b)
a, b = 5, 4
out_result(list_of_figures, a, b)
a, b = 5, 1
out_result(list_of_figures, a, b)

