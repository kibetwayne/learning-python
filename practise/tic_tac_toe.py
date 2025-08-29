
#**horizontal winner in tic tac toe
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")

def winner(board):
    return row_winner(board) or column_winner(board) or diagonal_winner(board)
        
def row_winner(board):
    for row in board:
        status = True
        first_entry = row[0]
        for single_char in row:
            if single_char == ' ' or first_entry != single_char:
                status = False
                break
        if status:
            return True
    return False


#**vertical winner in tic tac toe
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
        
def column_winner(board):
    for col in range(len(board[0])):
        status = True
        first_entry = board[0][col]
        for row in range(len(board)):
            if board[row][col] == ' ' or first_entry != board[row][col]:
                status = False
                break
        if status:
            return True
    return False



#**diagonal winner in tic tac toe
def assert_equal(actual, expected):
    if actual == expected:
        print("OK")
    else:
        print(f"Error! {repr(actual)} != {repr(expected)}")
        
def diagonal_winner(board):
    first = board[0][0]
    last = board[0][len(board)-1]
    first1 = 1
    first2 = len(board) - 2
    status1 = True
    status2 = True

    
    for i in range(len(board)):
        if first != board[i][i] or first == ' ':
            status1 = False
            break
        

    for i in range(len(board) -1):
        if last != board[first1][first2] or last == ' ':
            status2 = False
            break
        first1 += 1
        first2 -= 1
    # diagonal1 = []
    # diagonal2 = []
    # for i in range(len(board)):
    #     diagonal1.append(board[i][i])
    #     diagonal2.append(board[i][-i-1])
            
    return status1 or status2

assert_equal(
    winner(
        [
            ['X', 'X', 'X', ' '],
            ['X', 'X', ' ', ' '],
            ['X', ' ', 'O', 'X'],
            [' ', ' ', 'O', 'X']
        ]
    ),
    False
)


