BOARD_SIDE_LEN = 5 # number of digits in each row and column of the game board

class BingoSpot:
    def __init__(self, val):
        self.val = val
        self.marked = False
        self.row = None
        self.col = None

    def __eq__(self, rhs):
        return isinstance(rhs, BingoSpot) and self.val == rhs.val and self.marked == rhs.marked
    
    def __str__(self):
        s = str(self.val)
        if self.marked:
            s += '\''
        return s.rjust(3)

    def __repr__(self):
        return str(self)

class Board:
    def __init__(self, board):
        self.last_spot_marked = None
        self.board_grid = board
        self.board_dict = {}
        for row in range(BOARD_SIDE_LEN):
            for col in range(BOARD_SIDE_LEN):
                bingo_spot = board[row][col]
                bingo_spot.row = row
                bingo_spot.col = col
                self.board_dict[bingo_spot.val] = bingo_spot
    
    def __str__(self):
        s = ''
        for row in self.board_grid:
            s += ', '.join(list(map(lambda spot: str(spot), row))) + '\n'
        return s
    
    def __repr__(self):
        return str(self)

    def mark(self, drawing):
        # board -- an instance of Board
        # drawing -- the most recently drawn bingo number
        # marks the bingo spot corresponding to the drawing, returns the marked BingoSpot
        if drawing in self.board_dict.keys():
            bingo_spot = self.board_dict[drawing]
            bingo_spot.marked = True
            self.last_spot_marked = bingo_spot
            return True
        else:
            return False

    def is_winner(self):
        # last_spot_marked -- the instance of BingoSpot corresponding to the most recently drawn number
        # returns True if the last_spot_marked is in a completed row or column
        grid = self.board_grid
        # check if entire row completed
        marked_cols = 0
        for col in range(BOARD_SIDE_LEN):
            if grid[self.last_spot_marked.row][col].marked:
                marked_cols += 1
        if marked_cols == BOARD_SIDE_LEN:
            return True
        # check if entire column completed
        marked_rows = 0
        for row in range(BOARD_SIDE_LEN):
            if grid[row][self.last_spot_marked.col].marked:
                marked_rows += 1
        return marked_rows == BOARD_SIDE_LEN
    
    def sum_not_marked(self):
        sum_not_marked = 0
        for spot in self.board_dict.values():
            if not spot.marked:
                sum_not_marked += spot.val
        return sum_not_marked

def read_input(filename):
    return open(filename, 'r').readlines()

def process_input_row(row):
    # example input: '22 13 17 11  0'
    # expected output: [22, 13, 17, 11, 0]
    return list(map(lambda s: BingoSpot(int(s)), row.split()))

def process_drawings(lines):
    # first line of the file contains the drawings, a series of comma-separated integers
    return list(map(lambda s: int(s), lines[0].split(',')))

def process_boards(lines):
    lines = lines[2:] # game boards are after the first 2 lines in the file
    row = 0
    boards = []
    board = None
    for line in lines:
        if row % 6 == 0:
            board = []
        if row % 6 >= 0 and row % 6 < 5:
            board.append(process_input_row(line))
        else: # row % 6 == 5
            boards.append(Board(board))
        row += 1
    boards.append(Board(board)) # board at end of file
    return boards

def part1(boards, drawings):
    numbers_drawn = 0
    for drawing in drawings:
        numbers_drawn += 1
        for board in boards:
            is_marked = board.mark(drawing)
            if is_marked and numbers_drawn >= BOARD_SIDE_LEN:
                if board.is_winner():
                    print('Winning number:' + str(drawing))
                    print('Winning board:\n' + str(board))
                    sum_not_marked = board.sum_not_marked()
                    score = drawing * sum_not_marked
                    print('Sum not marked: ' + str(sum_not_marked))
                    print('Score = ' + str(drawing) + ' * ' + str(sum_not_marked) + ' = ' + str(score))
                    return score
    print("There was no winner.")
    return 0

def part2(boards, drawings):
    numbers_drawn = 0
    score = 0
    winning_draw = 0
    winning_board = None
    for drawing in drawings:
        numbers_drawn += 1
        board_id = 0
        for board in boards:
            is_marked = board.mark(drawing)
            if is_marked and numbers_drawn >= BOARD_SIDE_LEN:
                if board.is_winner():
                    score = drawing * board.sum_not_marked()
                    winning_draw = drawing
                    winning_board = board
                    boards.pop(board_id)
            board_id += 1
    if winning_board is not None:
        print('Winning number:' + str(winning_draw))
        print('Winning board:\n' + str(board))
        print('Score = ' + str(score))
        return score
    else:
        print("There was no winner")
        return 0

def test_bingospot_equality():
    a = BingoSpot(1)
    b = BingoSpot(1)
    c = BingoSpot(2)
    assert(a == b)
    assert(a != c)

def test_process_input_row():
    processed = process_input_row(' 8  2 23  4 24')
    assert(processed == [BingoSpot(8),BingoSpot(2),BingoSpot(23),BingoSpot(4),BingoSpot(24)])

def test_process_boards():
    lines = read_input('04 - Test Input.txt')
    boards = process_boards(lines)
    assert(boards[0].board_grid[0] == [BingoSpot(22), BingoSpot(13), BingoSpot(17), BingoSpot(11), BingoSpot(0)])

def test_process_drawings():
    lines = read_input('04 - Test Input.txt')
    drawings = process_drawings(lines)
    assert (drawings == [7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1])

def test_part1():
    lines = read_input('04 - Test Input.txt')
    drawings = process_drawings(lines)
    boards = process_boards(lines)
    score = part1(boards, drawings)
    assert(score == 4512)

def test_part2():
    lines = read_input('04 - Test Input.txt')
    drawings = process_drawings(lines)
    boards = process_boards(lines)
    score = part2(boards, drawings)
    assert(score == 1924)

def run_tests():
    test_bingospot_equality()
    test_process_input_row()
    test_process_boards()
    test_part1()
    test_part2()

def main():
    lines = read_input('04 - Bingo.txt')
    drawings = process_drawings(lines)
    boards = process_boards(lines)
    print('--- PART 1 ---\n\n')
    part1(boards, drawings)
    print('\n\n--- PART 2 ---\n\n')
    part2(boards, drawings)

run_tests()