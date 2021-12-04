with open('input_tables.txt') as file:
    raw_input_boards = file.readlines()
    temp_board = []
    input_boards = []
    
    for raw_line in raw_input_boards:
        line = raw_line.rstrip()
        if line == '':
            input_boards.append(temp_board)
            temp_board = []
        else:
            splitted_line = line.split(' ')
            stripped_list = [line_list for line_list in splitted_line if line_list != '']
            temp_board.append(stripped_list)

with open('input_numbers.txt') as file:
    input_numbers = file.readline()
    input_numbers = input_numbers.split(',')

marked_char = '*'

def isWinner(board):
    marked_list = []
    for row in range(len(board)):
        for column in range(len(board)):
            if board[row][column] == marked_char:
                marked_list.append({'row': row, 'column': column})

    rows_marked = []
    columns_marked = []
    for marked in marked_list: 
        rows_marked.append(marked['row'])
        columns_marked.append(marked['column'])

    most_common_rows_count = rows_marked.count(max(rows_marked, key=rows_marked.count))
    most_common_columns_count = columns_marked.count(max(columns_marked, key=columns_marked.count))

    return True if most_common_rows_count == len(board) or most_common_columns_count == len(board) else False

def sumUnmarkedNumbers(board):
    total_sum = 0
    for row in board:
        for number in row:
            total_sum += int(number) if number != '*' else 0
    
    return total_sum

def getFinalScore():
    for bingo_number in input_numbers:
        board_size = len(input_boards[0])

        for selected_board in input_boards:
            for row_number in range(board_size):
                for column_number in range(board_size):
                    if selected_board[row_number][column_number] == bingo_number:
                        selected_board[row_number][column_number] = marked_char
                        if isWinner(selected_board):
                            return  sumUnmarkedNumbers(selected_board) * int(bingo_number)

def getLastToWinFinalScore():
    completed_boards = []
    completed_scores = []
    for bingo_number in input_numbers:
        board_size = len(input_boards[0])

        for selected_board in range(len(input_boards)):
            for row_number in range(board_size):
                for column_number in range(board_size):
                    if input_boards[selected_board][row_number][column_number] == bingo_number:
                        input_boards[selected_board][row_number][column_number] = marked_char
                        if isWinner(input_boards[selected_board]) and selected_board not in completed_boards:
                            completed_boards.append(selected_board)
                            completed_scores.append(sumUnmarkedNumbers(input_boards[selected_board]) * int(bingo_number))

    return completed_scores[len(completed_scores)-1]

# Part 1
print(getFinalScore())

# Part 2
print(getLastToWinFinalScore())
