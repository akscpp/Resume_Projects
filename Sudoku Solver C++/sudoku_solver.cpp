#include <iostream>
#include <vector>

using namespace std;

const int BOARD_SIZE = 9;

// Function to print the Sudoku board
void printBoard(const vector<vector<int>> &board) {
    for (int i = 0; i < BOARD_SIZE; ++i) {
        for (int j = 0; j < BOARD_SIZE; ++j) {
            cout << board[i][j] << " ";
        }
        cout << endl;
    }
}

// Function to check if a number can be placed in a specific cell
bool isSafe(const vector<vector<int>> &board, int row, int col, int num) {
    // Check if the number is not present in the current row and column
    for (int i = 0; i < BOARD_SIZE; ++i) {
        if (board[row][i] == num || board[i][col] == num) {
            return false;
        }
    }

    // Check if the number is not present in the current 3x3 subgrid
    int startRow = row - row % 3;
    int startCol = col - col % 3;
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < 3; ++j) {
            if (board[i + startRow][j + startCol] == num) {
                return false;
            }
        }
    }

    return true;
}

// Function to solve the Sudoku using backtracking
bool solveSudoku(vector<vector<int>> &board) {
    for (int row = 0; row < BOARD_SIZE; ++row) {
        for (int col = 0; col < BOARD_SIZE; ++col) {
            if (board[row][col] == 0) {
                for (int num = 1; num <= 9; ++num) {
                    if (isSafe(board, row, col, num)) {
                        board[row][col] = num;

                        if (solveSudoku(board)) {
                            return true;  // Move to the next empty cell
                        }

                        board[row][col] = 0;  // Backtrack if the current placement is not valid
                    }
                }
                return false;  // No valid number found for the current cell
            }
        }
    }

    return true;  // All cells are filled, Sudoku is solved
}

int main() {
    vector<vector<int>> board = {
        {5, 3, 0, 0, 7, 0, 0, 0, 0},
        {6, 0, 0, 1, 9, 5, 0, 0, 0},
        {0, 9, 8, 0, 0, 0, 0, 6, 0},
        {8, 0, 0, 0, 6, 0, 0, 0, 3},
        {4, 0, 0, 8, 0, 3, 0, 0, 1},
        {7, 0, 0, 0, 2, 0, 0, 0, 6},
        {0, 6, 0, 0, 0, 0, 2, 8, 0},
        {0, 0, 0, 4, 1, 9, 0, 0, 5},
        {0, 0, 0, 0, 8, 0, 0, 7, 9}
    };

    cout << "Sudoku Puzzle:" << endl;
    printBoard(board);

    if (solveSudoku(board)) {
        cout << "\nSudoku Solution:" << endl;
        printBoard(board);
    } else {
        cout << "\nNo solution exists." << endl;
    }

    return 0;
}
