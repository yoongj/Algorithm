def solution(board):
    answer = 0
    
    board= board
    for row, i in enumerate(board):
        for col, j in enumerate(i):
            if j == 1:
                for cnt3 in range(3):
                    num_col= col-1+cnt3
                    if num_col>-1 and num_col<len(board):
                        if (row-1>-1) and (board[row-1][num_col] != 1):
                            board[row-1][num_col]= 2
                        if (row+1<len(board))and (board[row+1][num_col] != 1):
                            board[row+1][num_col]= 2
                        if board[row][num_col] != 1:
                            board[row][num_col]= 2
    for i in board:
        for j in i:
            if j == 0:
                answer += 1
                
    return answer
