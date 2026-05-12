def print_solution(board, n):
    for i in range(n):
        for j in range(n):

            if board[i][j] == 1:
                print("Q", end=" ")
            else:
                print("-", end=" ")

        print()

    print()


def is_safe(board, row, col, n, left_diag, right_diag, col_check):

    return not (

        left_diag[row - col + n - 1] or
        right_diag[row + col] or
        col_check[col]

    )


def solve_nqueen(board, row, n, left_diag, right_diag, col_check):

    if row == n:
        print_solution(board, n)
        return

    for col in range(n):

        if is_safe(board, row, col, n,
                   left_diag, right_diag, col_check):

            board[row][col] = 1

            col_check[col] = True

            left_diag[row - col + n - 1] = True

            right_diag[row + col] = True

            solve_nqueen(board, row + 1, n,
                          left_diag, right_diag, col_check)

            board[row][col] = 0

            col_check[col] = False

            left_diag[row - col + n - 1] = False

            right_diag[row + col] = False


def main(n):

    board = [[0] * n for i in range(n)]

    left_diag = [False] * (2 * n)

    right_diag = [False] * (2 * n)

    col_check = [False] * n

    solve_nqueen(board, 0, n,
                  left_diag, right_diag, col_check)


n = int(input("Enter n:"))
main(n)