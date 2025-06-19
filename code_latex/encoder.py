def createBoardRep(self, board):
    """
    Erzeugt eine mehrschichtige 8x8-Darstellung des Schachbretts.
    Weisse Figuren: 1, schwarze: -1.
    Zusaetzliche Layer: legale Zugquellen, Zugziele, Spielerfarbe am Zug (1/-1).
    Rueckgabe: np.array mit Form (9, 8, 8).
    """
        pieces = ['p', 'r', 'n', 'b', 'q', 'k']
        layers = []

        for piece in pieces:
            layer = [[0 for _ in range(8)] for _ in range(8)]
            for square, piece_obj in board.piece_map().items():
                piece_type = piece_obj.symbol().lower()
                if piece_type == piece:
                    row = 7 - (square // 8)
                    col = square % 8
                    layer[row][col] = -1 if piece_obj.color == chess.BLACK else 1

            layers.append(layer)

        from_layer = np.zeros((8, 8), dtype=int)
        for move in board.legal_moves:
          from_square = move.from_square
          row = 7 - (from_square // 8)
          col = from_square % 8
          from_layer[row][col] = 1
        layers.append(from_layer)

        # "To" squares layer
        to_layer = np.zeros((8, 8), dtype=int)
        for move in board.legal_moves:
          to_square = move.to_square
          row = 7 - (to_square // 8)
          col = to_square % 8
          to_layer[row][col] = 1
        layers.append(to_layer)

        # Turn indicator layer
        turn_layer = np.full((8, 8), 1 if board.turn == chess.WHITE else -1, dtype=int)
        layers.append(turn_layer)

        return np.stack(layers)  # Shape: (9, 8, 8)