def n_queens(n):
    col = set()
    posDiag = set()  # (r + c)
    negDiag = set()  # (r - c)
    res = []

    # Initialize board with all 0's
    board = [["0"] * n for _ in range(n)]

    # Step 1: Place the first Queen manually (first row, first column)
    board[0][0] = "1"
    col.add(0)
    posDiag.add(0 + 0)
    negDiag.add(0 - 0)

    # Step 2: Backtrack for remaining queens starting from row 1
    def backtrack(r):
        if r == n:
            copy = [" ".join(row) for row in board]
            res.append(copy)
            return

        for c in range(n):
            if c in col or (r + c) in posDiag or (r - c) in negDiag:
                continue

            col.add(c)
            posDiag.add(r + c)
            negDiag.add(r - c)
            board[r][c] = "1"

            backtrack(r + 1)

            # Undo (backtrack)
            col.remove(c)
            posDiag.remove(r + c)
            negDiag.remove(r - c)
            board[r][c] = "0"

    backtrack(1)  # start from 2nd row

    # Step 3: Print all solutions
    for sol in res:
        for row in sol:
            print(row)
        print()

if __name__ == "__main__":
    n_queens(8)
