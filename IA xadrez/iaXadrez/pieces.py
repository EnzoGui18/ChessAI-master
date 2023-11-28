import ai
from move import Move

class Piece():

    WHITE = "W"
    BLACK = "B"

    def __init__(self, x, y, color, piece_type, value):
        self.x = x
        self.y = y
        self.color = color
        self.piece_type = piece_type
        self.value = value



    # Retorna todos os movimentos diagonais desta peça. Isto deve, portanto, apenas
    # ser usado pelo Bispo e pela Rainha, pois são as únicas peças que podem
    # mover-se na diagonal.
    def get_possible_diagonal_moves(self, board):
        moves = []

        for i in range(1, 8):
            if (not board.in_bounds(self.x+i, self.y+i)):
                break

            piece = board.get_piece(self.x+i, self.y+i)
            moves.append(self.get_move(board, self.x+i, self.y+i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x+i, self.y-i)):
                break

            piece = board.get_piece(self.x+i, self.y-i)
            moves.append(self.get_move(board, self.x+i, self.y-i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y-i)):
                break

            piece = board.get_piece(self.x-i, self.y-i)
            moves.append(self.get_move(board, self.x-i, self.y-i))
            if (piece != 0):
                break

        for i in range(1, 8):
            if (not board.in_bounds(self.x-i, self.y+i)):
                break

            piece = board.get_piece(self.x-i, self.y+i)
            moves.append(self.get_move(board, self.x-i, self.y+i))
            if (piece != 0):
                break

        return self.remove_null_from_list(moves)

    # Retorna todos os movimentos horizontais desta peça. Isto deve, portanto, apenas
    # ser usadas pelas Torres e Dama, pois são as únicas peças que podem
    # mover horizontal
    def get_possible_horizontal_moves(self, board):
        moves = []

        # Move-se para a direita da peça.
        for i in range(1, 8 - self.x):
            piece = board.get_piece(self.x + i, self.y)
            moves.append(self.get_move(board, self.x+i, self.y))

            if (piece != 0):
                break

        # Move-se para a esquerda da peça.
        for i in range(1, self.x + 1):
            piece = board.get_piece(self.x - i, self.y)
            moves.append(self.get_move(board, self.x-i, self.y))
            if (piece != 0):
                break

        # Movimentos descendentes.
        for i in range(1, 8 - self.y):
            piece = board.get_piece(self.x, self.y + i)
            moves.append(self.get_move(board, self.x, self.y+i))
            if (piece != 0):
                break

        # Movimentos ascendentes.
        for i in range(1, self.y + 1):
            piece = board.get_piece(self.x, self.y - i)
            moves.append(self.get_move(board, self.x, self.y-i))
            if (piece != 0):
                break

        return self.remove_null_from_list(moves)

    # Retorna um objeto Move com (xfrom, yfrom) definido para a posição atual da peça.
    # (xto, yto) é definido para a posição especificada. Se a movimentação não for válida, 0 será retornado.
    # Um movimento não é válido se estiver fora de campo ou se uma peça da mesma cor for
    # sendo comido.
    def get_move(self, board, xto, yto):
        move = 0
        if (board.in_bounds(xto, yto)):
            piece = board.get_piece(xto, yto)
            if (piece != 0):
                if (piece.color != self.color):
                    move = Move(self.x, self.y, xto, yto)
            else:
                move = Move(self.x, self.y, xto, yto)
        return move

    # Retorna a lista de movimentos limpos de todos os 0's.
    def remove_null_from_list(self, l):
        return [move for move in l if move != 0]

    def to_string(self):
        return self.color + self.piece_type + " "

class Rook(Piece):

    PIECE_TYPE = "R"
    VALUE = 500

    def __init__(self, x, y, color):
        super(Rook, self).__init__(x, y, color, Rook.PIECE_TYPE, Rook.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_horizontal_moves(board)

    def clone(self):
        return Rook(self.x, self.y, self.color)


class Knight(Piece):

    PIECE_TYPE = "N"
    VALUE = 320

    def __init__(self, x, y, color):
        super(Knight, self).__init__(x, y, color, Knight.PIECE_TYPE, Knight.VALUE)

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x+2, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y+1))
        moves.append(self.get_move(board, self.x+1, self.y-2))
        moves.append(self.get_move(board, self.x+2, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y+2))
        moves.append(self.get_move(board, self.x-2, self.y-1))
        moves.append(self.get_move(board, self.x-1, self.y-2))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Knight(self.x, self.y, self.color)


class Bishop(Piece):

    PIECE_TYPE = "B"
    VALUE = 330

    def __init__(self, x, y, color):
        super(Bishop, self).__init__(x, y, color, Bishop.PIECE_TYPE, Bishop.VALUE)

    def get_possible_moves(self, board):
        return self.get_possible_diagonal_moves(board)

    def clone(self):
        return Bishop(self.x, self.y, self.color)


class Queen(Piece):

    PIECE_TYPE = "Q"
    VALUE = 900

    def __init__(self, x, y, color):
        super(Queen, self).__init__(x, y, color, Queen.PIECE_TYPE, Queen.VALUE)

    def get_possible_moves(self, board):
        diagonal = self.get_possible_diagonal_moves(board)
        horizontal = self.get_possible_horizontal_moves(board)
        return horizontal + diagonal

    def clone(self):
        return Queen(self.x, self.y, self.color)


class King(Piece):

    PIECE_TYPE = "K"
    VALUE = 20000

    def __init__(self, x, y, color):
        super(King, self).__init__(x, y, color, King.PIECE_TYPE, King.VALUE)

    def get_possible_moves(self, board):
        moves = []

        moves.append(self.get_move(board, self.x+1, self.y))
        moves.append(self.get_move(board, self.x+1, self.y+1))
        moves.append(self.get_move(board, self.x, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y+1))
        moves.append(self.get_move(board, self.x-1, self.y))
        moves.append(self.get_move(board, self.x-1, self.y-1))
        moves.append(self.get_move(board, self.x, self.y-1))
        moves.append(self.get_move(board, self.x+1, self.y-1))

        moves.append(self.get_castle_kingside_move(board))
        moves.append(self.get_castle_queenside_move(board))

        return self.remove_null_from_list(moves)

    # Apenas verifica o lado do rei do castelo
    def get_castle_kingside_move(self, board):
        # Estamos olhando para uma torre válida
        piece_in_corner = board.get_piece(self.x+3, self.y)
        if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
            return 0

        # Se a torre no canto não for da nossa cor, não podemos rocar (duh).
        if (piece_in_corner.color != self.color):
            return 0
        
        # Se o rei se mudou, não podemos fazer roque
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        # Se houver peças entre o rei e a torre, não podemos rocar
        if (board.get_piece(self.x+1, self.y) != 0 or board.get_piece(self.x+2, self.y) != 0):
            return 0
        
        return Move(self.x, self.y, self.x+2, self.y)

    def get_castle_queenside_move(self, board):
        # Estamos olhando para uma torre válida
        piece_in_corner = board.get_piece(self.x-4, self.y)
        if (piece_in_corner == 0 or piece_in_corner.piece_type != Rook.PIECE_TYPE):
            return 0

        # Se a torre no canto não for da nossa cor, não podemos rocar (duh).
        if (piece_in_corner.color != self.color):
            return 0
        
        # Se o rei se mudou, não podemos fazer roque
        if (self.color == Piece.WHITE and board.white_king_moved):
            return 0
        
        if (self.color == Piece.BLACK and board.black_king_moved):
            return 0

        # Se houver peças entre o rei e a torre, não podemos rocar
        if (board.get_piece(self.x-1, self.y) != 0 or board.get_piece(self.x-2, self.y) != 0 or board.get_piece(self.x-3, self.y) != 0):
            return 0
        
        return Move(self.x, self.y, self.x-2, self.y)


    def clone(self):
        return King(self.x, self.y, self.color)


class Pawn(Piece):

    PIECE_TYPE = "P"
    VALUE = 100

    def __init__(self, x, y, color):
        super(Pawn, self).__init__(x, y, color, Pawn.PIECE_TYPE, Pawn.VALUE)

    def is_starting_position(self):
        if (self.color == Piece.BLACK):
            return self.y == 1
        else:
            return self.y == 8 - 2

    def get_possible_moves(self, board):
        moves = []

        # Direção em que o peão pode se mover.
        direction = -1
        if (self.color == Piece.BLACK):
            direction = 1

        # O movimento geral de 1 passo à frente.
        if (board.get_piece(self.x, self.y+direction) == 0):
            moves.append(self.get_move(board, self.x, self.y + direction))

        # O peão pode dar 2 passos como primeiro movimento.
        if (self.is_starting_position() and board.get_piece(self.x, self.y+ direction) == 0 and board.get_piece(self.x, self.y + direction*2) == 0):
            moves.append(self.get_move(board, self.x, self.y + direction * 2))

        # Comendo peças.
        piece = board.get_piece(self.x + 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x + 1, self.y + direction))

        piece = board.get_piece(self.x - 1, self.y + direction)
        if (piece != 0):
            moves.append(self.get_move(board, self.x - 1, self.y + direction))

        return self.remove_null_from_list(moves)

    def clone(self):
        return Pawn(self.x, self.y, self.color)
