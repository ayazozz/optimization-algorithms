# Optimization-Algorithms
## Solution of n-queens Optimization Problem

The eight queens puzzle is the problem of placing eight chess queens on an 8×8 chessboard so that no two queens threaten each other;
thus, a solution requires that no two queens share the same row, column, or diagonal. The eight queens puzzle is an example of the
more general n queens problem of placing n non-attacking queens on an n×n chessboard, for which solutions exist for all natural
numbers n with the exception of n=2 and n=3.

You can find more information about this problem on this link : http://www.wikiwand.com/en/Eight_queens_puzzle

In this solution, genetic algorithms is used for this problem. 
1. Create random board state. (for this program : 10 board - each board has a 8*8 cheeseboard)
2. Check if the board is optimal
   ... No --> 1. select the best 8 parents ( 8 board )
          2. mix the boards and craete new parents (crossover - muatate - rouletteselection rule )
          3. Check if the board is optimal
   ... Yes --> Print board
   
   ![Capture](https://user-images.githubusercontent.com/38051809/54754533-06c96780-4be4-11e9-860e-fb12645d76b8.PNG)
