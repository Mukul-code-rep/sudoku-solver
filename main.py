def solve(board):
    find = empty_space(board)
    if find is None:
        return True
    row, col = find

    for i in range(1, 10):
        if is_valid(board, i, (row, col)):
            board[row][col] = i

            if solve(board):
                return True

            board[row][col] = 0

    return False


def is_valid(board, num, pos):
    for i in range(len(board[0])):
        if board[pos[0]][i] == num and pos[1] != i:
            return False

    for i in range(len(board)):
        if board[i][pos[1]] == num and pos[0] != i:
            return False

    x = pos[1]//3
    y = pos[0]//3
    for i in range(y*3, y*3+3):
        for j in range(x*3, x*3+3):
            if board[i][j] == num and (i, j) != pos:
                return False

    return True


def empty_space(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i, j)
    return None


def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("- - - - - - - - - - - - - -")
        for j in range(len(bo[0])):
            if j % 3 == 0:
                print(" | ",end="")

            if j == 8:
                print(bo[i][j], end="\n")
            else:
                print(str(bo[i][j]) + " ", end="")


if __name__ == "__main__":
    board = [
        [8, 0, 0, 9, 1, 0, 0, 0, 0],
        [2, 0, 6, 0, 0, 8, 7, 0, 0],
        [0, 7, 0, 0, 0, 0, 5, 4, 0],
        [0, 0, 4, 0, 0, 6, 9, 7, 0],
        [6, 8, 0, 0, 0, 5, 0, 1, 2],
        [3, 0, 7, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 2, 0, 4, 0, 5, 0],
        [4, 0, 0, 3, 0, 0, 0, 8, 0],
        [0, 9, 0, 7, 0, 0, 0, 0, 3]
    ]
    play_board = []
    for i in range(len(board)):
        play_board.append([board[i][j] for j in range(len(board[i]))])
    print("Welcome to sudoku!")
    print("Here's your puzzle.\n")
    print_board(board)
    res = solve(board)
    if not res:
        print("This is not solvable.")
    else:
        count = 0
        while count < 3 and play_board != board:
            num = int(input("Enter the number you wish to enter (1-9): "))
            print("Where would you like this to go?")
            row = int(input("Row: "))
            col = int(input("Column: "))
            if num == board[row-1][col-1]:
                play_board[row-1][col-1] = num
                print("")
                print_board(play_board)
            else:
                print("Sorry, that's wrong. Try again!\n")
                count += 1

        if count > 2:
            print("You lost!")
            print("Here's the final board.\n")
            print_board(board)
        else:
            print("Congratulations! You win.")
