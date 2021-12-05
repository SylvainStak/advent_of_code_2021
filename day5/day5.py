with open('input.txt') as file:
    input = file.readlines()
    input = [line.rstrip() for line in input]

def drawLine(x1, y1, x2, y2):
    line_type = ''

    if y1==y2:
        line_type = 'horizontal'
    elif x1==x2:
        line_type = 'vertical'
    elif abs(x1-x2) == abs(y1-y2):
        line_type = 'diagonal'

    if line_type == 'horizontal':
        correct_range = range(x1, x2+1) if x1 < x2 else reversed(range(x2, x1+1))
        for x in correct_range:
            board[y1][x] += 1
    elif line_type == 'vertical':
        correct_range = range(y1, y2+1) if y1 < y2 else reversed(range(y2, y1+1))
        for y in correct_range:
            board[y][x1] += 1
    elif line_type == 'diagonal':
        correct_X_range = range(x1, x2+1) if x1 < x2 else reversed(range(x2, x1+1))
        correct_Y_range = range(y1, y2+1) if y1 < y2 else reversed(range(y2, y1+1))
        for x, y in zip(correct_X_range, correct_Y_range):
            board[y][x] += 1

def checkOverlap():
    counter = 0
    for row in board:
        for cell in row:
            counter += 1 if cell >= 2 else 0
    return counter

def drawBoardLines(acceptDiagonals=False):
    for segment in input:
        origin = segment.split(' -> ')[0]
        destination = segment.split(' -> ')[1]
        X1 = int(origin.split(',')[0])
        Y1 = int(origin.split(',')[1])
        X2 = int(destination.split(',')[0])
        Y2 = int(destination.split(',')[1])
        if acceptDiagonals:
            drawLine(X1, Y1, X2, Y2)
        else:
            if X1 == X2 or Y1 == Y2:
                drawLine(X1, Y1, X2, Y2)

# Part 1
board = [[0 for i in range(1000)] for x in range(1000)]
drawBoardLines(acceptDiagonals=False)
print(checkOverlap())

# Part 2
board = [[0 for i in range(1000)] for x in range(1000)]
drawBoardLines(acceptDiagonals=True)
print(checkOverlap())
