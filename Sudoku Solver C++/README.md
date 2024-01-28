# Sudoku Solver

This C++ program solves a Sudoku puzzle using backtracking. The code is designed to be clean and easy to understand.

## How to Use

1. Open the `sudoku_solver.cpp` file in a C++ compiler or integrated development environment (IDE).

2. Replace the initial Sudoku board with your own puzzle. The empty cells are represented by `0`.

   ```cpp
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

