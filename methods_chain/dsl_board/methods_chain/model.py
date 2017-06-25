from dsl_board.semantic_model.board import Board
from dsl_board.semantic_model.cut import Cut


def board(name, cuts):
    return Board(name, cuts)


def cut(name):
    return Cut(name, swimlanes=[])
