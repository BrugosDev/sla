!pip install chess

import chess
board = chess.Board()
board

board.pieces(chess.PAWN, chess.WHITE)

len(board.pieces(chess.PAWN, chess.WHITE))

board.pieces(chess.PAWN, chess.BLACK)

for i in board.pieces(chess.PAWN, chess.WHITE):
  print(i)

pawntable = [
    0, 0, 0, 0, 0, 0, 0, 0,
    5, 10, 10, -20, -20, 10, 10, 5,
    5, -5, -10, 0, 0, -10, -5, 5,
    0, 0, 0, 20, 20, 0, 0, 0,
    5, 5, 10, 25, 25, 10, 5, 5,
    10, 10, 20, 30, 30, 20, 10, 10,
    50, 50, 50, 50, 50, 50, 50, 50,
    0, 0, 0, 0, 0, 0, 0, 0]

knightstable = [
    -50, -40, -30, -30, -30, -30, -40, -50,
    -40, -20, 0, 5, 5, 0, -20, -40,
    -30, 5, 10, 15, 15, 10, 5, -30,
    -30, 0, 15, 20, 20, 15, 0, -30,
    -30, 5, 15, 20, 20, 15, 5, -30,
    -30, 0, 10, 15, 15, 10, 0, -30,
    -40, -20, 0, 0, 0, 0, -20, -40,
    -50, -40, -30, -30, -30, -30, -40, -50]

bishopstable = [
    -20, -10, -10, -10, -10, -10, -10, -20,
    -10, 5, 0, 0, 0, 0, 5, -10,
    -10, 10, 10, 10, 10, 10, 10, -10,
    -10, 0, 10, 10, 10, 10, 0, -10,
    -10, 5, 5, 10, 10, 5, 5, -10,
    -10, 0, 5, 10, 10, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -10, -10, -10, -10, -20]

rookstable = [
    0, 0, 0, 5, 5, 0, 0, 0,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    -5, 0, 0, 0, 0, 0, 0, -5,
    5, 10, 10, 10, 10, 10, 10, 5,
    0, 0, 0, 0, 0, 0, 0, 0]

queenstable = [
    -20, -10, -10, -5, -5, -10, -10, -20,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -10, 5, 5, 5, 5, 5, 0, -10,
    0, 0, 5, 5, 5, 5, 0, -5,
    -5, 0, 5, 5, 5, 5, 0, -5,
    -10, 0, 5, 5, 5, 5, 0, -10,
    -10, 0, 0, 0, 0, 0, 0, -10,
    -20, -10, -10, -5, -5, -10, -10, -20]
    
kingstable = [
    20, 30, 10, 0, 0, 10, 30, 20,
    20, 20, 0, 0, 0, 0, 20, 20,
    -10, -20, -20, -20, -20, -20, -20, -10,
    -20, -30, -30, -40, -40, -30, -30, -20,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30,
    -30, -40, -40, -50, -50, -40, -40, -30]

def evaluate_board():
  if board.is_checkmate():
        if board.turn:
            return -9999
        else:
            return 9999
  if board.is_stalemate():
        return 0
  if board.is_insufficient_material():
        return 0

  wp = len(board.pieces(chess.PAWN, chess.WHITE))
  bp = len(board.pieces(chess.PAWN, chess.BLACK))
  wn = len(board.pieces(chess.KNIGHT, chess.WHITE))
  bn = len(board.pieces(chess.KNIGHT, chess.BLACK))
  wb = len(board.pieces(chess.BISHOP, chess.WHITE))
  bb = len(board.pieces(chess.BISHOP, chess.BLACK))
  wr = len(board.pieces(chess.ROOK, chess.WHITE))
  br = len(board.pieces(chess.ROOK, chess.BLACK))
  wq = len(board.pieces(chess.QUEEN, chess.WHITE))
  bq = len(board.pieces(chess.QUEEN, chess.BLACK))

  material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

  pawnsq = sum([pawntable[i] for i in board.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in board.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in board.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in board.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in board.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in board.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in board.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in board.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in board.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in board.pieces(chess.KING, chess.BLACK)])
  
  eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval
  else:
      return -eval

def alphabeta(alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(alpha, beta)
    for move in board.legal_moves:
        board.push(move)
        score = -alphabeta(-beta, -alpha, depthleft - 1)
        board.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

def selectmove(depth):
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in board.legal_moves:
        board.push(move)
        boardValue = -alphabeta(-beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        board.pop()
    return bestMove

def quiesce(alpha, beta):
    stand_pat = evaluate_board()
    if (stand_pat >= beta):
        return beta
    if (stand_pat > alpha):
        alpha = stand_pat

    for move in board.legal_moves:
        if board.is_capture(move):
            board.push(move)
            score = -quiesce(-beta, -alpha)
            board.pop()
            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

def devmove():
  move = selectmove(3)
  board.push(move)
devmove()
display(board)

for i in range(20):
  devmove()
  display(board)

def evaluate_board(tabuleiro):
  if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
  if tabuleiro.is_stalemate():
        return 0
  if tabuleiro.is_insufficient_material():
        return 0

  wp = len(tabuleiro.pieces(chess.PAWN, chess.WHITE))
  bp = len(tabuleiro.pieces(chess.PAWN, chess.BLACK))
  wn = len(tabuleiro.pieces(chess.KNIGHT, chess.WHITE))
  bn = len(tabuleiro.pieces(chess.KNIGHT, chess.BLACK))
  wb = len(tabuleiro.pieces(chess.BISHOP, chess.WHITE))
  bb = len(tabuleiro.pieces(chess.BISHOP, chess.BLACK))
  wr = len(tabuleiro.pieces(chess.ROOK, chess.WHITE))
  br = len(tabuleiro.pieces(chess.ROOK, chess.BLACK))
  wq = len(tabuleiro.pieces(chess.QUEEN, chess.WHITE))
  bq = len(tabuleiro.pieces(chess.QUEEN, chess.BLACK))

  material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)

  pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.KING, chess.BLACK)])
  
  eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval
  else:
      return -eval

def alphabeta(tabuleiro, alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(tabuleiro, alpha, beta)
    for move in tabuleiro.legal_moves:
        tabuleiro.push(move)
        score = -alphabeta(tabuleiro, -beta, -alpha, depthleft - 1)
        tabuleiro.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

def quiesce(tabuleiro, alpha, beta):
    stand_pat = evaluate_board(tabuleiro)
    if (stand_pat >= beta):
        return beta
    if (stand_pat > alpha):
        alpha = stand_pat

    for move in tabuleiro.legal_moves:
        if tabuleiro.is_capture(move):
            tabuleiro.push(move)
            score = -quiesce(tabuleiro, -beta, -alpha)
            tabuleiro.pop()
            if (score >= beta):
                return beta
            if (score > alpha):
                alpha = score
    return alpha

def selectmove(tabuleiro, depth):
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000
    for move in tabuleiro.legal_moves:
        tabuleiro.push(move)
        boardValue = -alphabeta(tabuleiro, -beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        tabuleiro.pop()
    return bestMove

class Chess:
  def __init__(self):
    self.tabuleiro = chess.Board()
  def move(self, k):
    for i in range(k):
      move = selectmove(self.tabuleiro, 3)
      self.tabuleiro.push(move)
      display(self.tabuleiro)
    return self
Chess().move(2)
Collecting chess
  Downloading chess-1.8.0-py3-none-any.whl (147 kB)
     |██▎                             | 10 kB 20.1 MB/s eta 0:00:01
     |████▌                           | 20 kB 26.6 MB/s eta 0:00:01
     |██████▊                         | 30 kB 12.5 MB/s eta 0:00:01
     |█████████                       | 40 kB 9.3 MB/s eta 0:00:01
     |███████████▏                    | 51 kB 5.5 MB/s eta 0:00:01
     |█████████████▍                  | 61 kB 5.8 MB/s eta 0:00:01
     |███████████████▋                | 71 kB 5.2 MB/s eta 0:00:01
     |█████████████████▉              | 81 kB 5.7 MB/s eta 0:00:01
     |████████████████████            | 92 kB 5.6 MB/s eta 0:00:01
     |██████████████████████▎         | 102 kB 5.1 MB/s eta 0:00:01
     |████████████████████████▌       | 112 kB 5.1 MB/s eta 0:00:01
     |██████████████████████████▊     | 122 kB 5.1 MB/s eta 0:00:01
     |█████████████████████████████   | 133 kB 5.1 MB/s eta 0:00:01
     |███████████████████████████████▏| 143 kB 5.1 MB/s eta 0:00:01
     |████████████████████████████████| 147 kB 5.1 MB/s 
Installing collected packages: chess
Successfully installed chess-1.8.0
8
8
9
10
11
12
13
14
15
<__main__.Chess at 0x7f07cfdb12d0>

class MaterialScore:
  def score(self, tabuleiro):
      wp = len(tabuleiro.pieces(chess.PAWN, chess.WHITE))
      bp = len(tabuleiro.pieces(chess.PAWN, chess.BLACK))
      wn = len(tabuleiro.pieces(chess.KNIGHT, chess.WHITE))
      bn = len(tabuleiro.pieces(chess.KNIGHT, chess.BLACK))
      wb = len(tabuleiro.pieces(chess.BISHOP, chess.WHITE))
      bb = len(tabuleiro.pieces(chess.BISHOP, chess.BLACK))
      wr = len(tabuleiro.pieces(chess.ROOK, chess.WHITE))
      br = len(tabuleiro.pieces(chess.ROOK, chess.BLACK))
      wq = len(tabuleiro.pieces(chess.QUEEN, chess.WHITE))
      bq = len(tabuleiro.pieces(chess.QUEEN, chess.BLACK))

      material = 100 * (wp - bp) + 320 * (wn - bn) + 330 * (wb - bb) + 500 * (wr - br) + 900 * (wq - bq)
      return material


def evaluate_board(tabuleiro):
  if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
  if tabuleiro.is_stalemate():
        return 0
  if tabuleiro.is_insufficient_material():
        return 0

  material = MaterialScore().score(tabuleiro)

  pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.KING, chess.BLACK)])
  
  eval = material + pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval
  else:
      return -eval

Chess().move(3)

class MaterialScore:
  def score(self, tabuleiro):
      wp = len(tabuleiro.pieces(chess.PAWN, chess.WHITE))
      bp = len(tabuleiro.pieces(chess.PAWN, chess.BLACK))
      wn = len(tabuleiro.pieces(chess.KNIGHT, chess.WHITE))
      bn = len(tabuleiro.pieces(chess.KNIGHT, chess.BLACK))
      wb = len(tabuleiro.pieces(chess.BISHOP, chess.WHITE))
      bb = len(tabuleiro.pieces(chess.BISHOP, chess.BLACK))
      wr = len(tabuleiro.pieces(chess.ROOK, chess.WHITE))
      br = len(tabuleiro.pieces(chess.ROOK, chess.BLACK))
      wq = len(tabuleiro.pieces(chess.QUEEN, chess.WHITE))
      bq = len(tabuleiro.pieces(chess.QUEEN, chess.BLACK))

      material = 100 * (wp + bp) + 320 * (wn + bn) + 330 * (wb + bb) + 500 * (wr + br) + 900 * (wq + bq)
      return material
Chess().move(10)


def evaluate_board(tabuleiro):
  if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
  if tabuleiro.is_stalemate():
        return 0
  if tabuleiro.is_insufficient_material():
        return 0

  material = MaterialScore().score(tabuleiro)

  pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.KING, chess.BLACK)])
  
  eval = pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval - material
  else:
      return -eval - material
Chess().move(10)

def evaluate_board(tabuleiro):
  if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
  if tabuleiro.is_stalemate():
        return 0
  if tabuleiro.is_insufficient_material():
        return 0

  material = MaterialScore().score(tabuleiro)

  pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.KING, chess.BLACK)])
  
  eval = -(pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq)
  if board.turn:
      return eval - material
  else:
      return -eval - material
Chess().move(6)

def is_capture_moves(tabuleiro, moves):
  return [move for move in moves if tabuleiro.is_capture(move)]

def new_legal_moves(tabuleiro):
  legal_moves = tabuleiro.legal_moves
  captures = is_capture_moves(tabuleiro, legal_moves)
  if len(captures) > 0:
    return captures
  return legal_moves

def selectmove(tabuleiro, depth):
    bestMove = chess.Move.null()
    bestValue = -99999
    alpha = -100000
    beta = 100000

    for move in new_legal_moves(tabuleiro):
        tabuleiro.push(move)
        boardValue = -alphabeta(tabuleiro, -beta, -alpha, depth - 1)
        if boardValue > bestValue:
            bestValue = boardValue
            bestMove = move
        if boardValue > alpha:
            alpha = boardValue
        tabuleiro.pop()

    return bestMove

def evaluate_board(tabuleiro):
  if tabuleiro.is_checkmate():
        if tabuleiro.turn:
            return -9999
        else:
            return 9999
  if tabuleiro.is_stalemate():
        return 0
  if tabuleiro.is_insufficient_material():
        return 0

  material = MaterialScore().score(tabuleiro)

  pawnsq = sum([pawntable[i] for i in tabuleiro.pieces(chess.PAWN, chess.WHITE)])
  pawnsq = pawnsq + sum([-pawntable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.PAWN, chess.BLACK)])
  knightsq = sum([knightstable[i] for i in tabuleiro.pieces(chess.KNIGHT, chess.WHITE)])
  knightsq = knightsq + sum([-knightstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.KNIGHT, chess.BLACK)])
  bishopsq = sum([bishopstable[i] for i in tabuleiro.pieces(chess.BISHOP, chess.WHITE)])
  bishopsq = bishopsq + sum([-bishopstable[chess.square_mirror(i)]
                            for i in tabuleiro.pieces(chess.BISHOP, chess.BLACK)])
  rooksq = sum([rookstable[i] for i in tabuleiro.pieces(chess.ROOK, chess.WHITE)])
  rooksq = rooksq + sum([-rookstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.ROOK, chess.BLACK)])
  queensq = sum([queenstable[i] for i in tabuleiro.pieces(chess.QUEEN, chess.WHITE)])
  queensq = queensq + sum([-queenstable[chess.square_mirror(i)]
                          for i in tabuleiro.pieces(chess.QUEEN, chess.BLACK)])
  kingsq = sum([kingstable[i] for i in tabuleiro.pieces(chess.KING, chess.WHITE)])
  kingsq = kingsq + sum([-kingstable[chess.square_mirror(i)]
                        for i in tabuleiro.pieces(chess.KING, chess.BLACK)])
  
  eval = pawnsq + knightsq + bishopsq + rooksq + queensq + kingsq
  if board.turn:
      return eval - material
  else:
      return -eval - material

Chess().move(10)

def quiesce(tabuleiro, alpha, beta):
    stand_pat = evaluate_board(tabuleiro)
    if (stand_pat >= beta):
        return beta
    if (stand_pat > alpha):
        alpha = stand_pat

    for move in is_capture_moves(tabuleiro, tabuleiro.legal_moves):
        tabuleiro.push(move)
        score = -quiesce(tabuleiro, -beta, -alpha)
        tabuleiro.pop()
        if (score >= beta):
            return beta
        if (score > alpha):
            alpha = score
    return alpha

def alphabeta(tabuleiro, alpha, beta, depthleft):
    bestscore = -9999
    if (depthleft == 0):
        return quiesce(tabuleiro, alpha, beta)

    for move in new_legal_moves(tabuleiro):
        tabuleiro.push(move)
        score = -alphabeta(tabuleiro, -beta, -alpha, depthleft - 1)
        tabuleiro.pop()
        if (score >= beta):
            return score
        if (score > bestscore):
            bestscore = score
        if (score > alpha):
            alpha = score
    return bestscore

jogo = Chess().move(10)
jogo = jogo.move(10)
jogo = jogo.move(10)
jogo = jogo.move(20)





