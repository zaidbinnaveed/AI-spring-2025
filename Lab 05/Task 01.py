import chess
import chess.engine

def beam_search_best_move(board, beam_width, depth_limit):
    engine = chess.engine.SimpleEngine.popen_uci("/usr/local/bin/stockfish")
    moves = list(board.legal_moves)
    
    beam = [(board, None, 0)]  
    
    for _ in range(depth_limit):
        new_beam = []
        for b, move, score in beam:
            for m in list(b.legal_moves)[:beam_width]:
                new_board = b.copy()
                new_board.push(m)
                info = engine.analyse(new_board, chess.engine.Limit(depth=1))
                new_score = info["score"].relative.score()
                new_beam.append((new_board, m, new_score))
        new_beam.sort(key=lambda x: x[2], reverse=True)
        beam = new_beam[:beam_width]

    best_move = max(beam, key=lambda x: x[2])[1]
    engine.quit()
    return best_move

board = chess.Board()
print(beam_search_best_move(board, beam_width=3, depth_limit=3))
