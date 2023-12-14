#include <iostream>
#define N 4
using namespace std;

void printSolution(int board[N][N])
{
    for (int i = 0; i < N; i++)
    {
        for (int j = 0; j < N; j++)
            if (board[i][j])
                cout << "Q ";
            else
                cout << ". ";
        cout << "\n";
    }
    cout << "\n";
}

bool isSafe(int board[N][N], int row, int col)
{
    int i, j;
    for (i = 0; i < col; i++)
        if (board[row][i])
            return false;
    for (i = row, j = col; i >= 0 && j >= 0; i--, j--)
        if (board[i][j])
            return false;
    for (i = row, j = col; j >= 0 && i < N; i++, j--)
        if (board[i][j])
            return false;
    return true;
}

bool solveNQUtil(int board[N][N], int col)
{
    if (col >= N)
    {
        printSolution(board);
        return true;
    }
    bool res = false;
    for (int i = 0; i < N; i++)
    {
        if (isSafe(board, i, col))
        {
            board[i][col] = 1;
            res = solveNQUtil(board, col + 1) || res;
            board[i][col] = 0; // BACKTRACK
        }
    }
    return res;
}

void solveNQ()
{
    int board[N][N] = {{0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}, {0, 0, 0, 0}};
    if (!solveNQUtil(board, 0))
    {
        cout << "Solution does not exist";
    }
}

int main()
{
    solveNQ();
    return 0;
}
