COMS W4701 Artificial Intelligence<br/>
Project #3: Isolation Game

Assignment
----------
The purpose of this assignment was to create a program to play a game of Isolation (rules below) using a minimax algorithm with alpha-beta pruning.

Game Rules
----------
The game has two players: x and o. The players alternate turns, with player x moving first at the beginning of each game.

Player x starts at position (1,1) while o starts at (8,8).

Each turn, a player can move like a queen in chess (in any of the eight directions) as long as her path does not cross a square already filled in or occupied. After moving, the space vacated by the player is designated as filled and cannot be moved to again. Notice that only the space that was occupied is filled, not the entire path.

The game ends when one player can no longer move, leaving the other player as the winner.

The coordinate (1 1) indicates the top left hand side of the board.

The board is specified as a list of rows. Each row is a list of entries:

    - is an empty square
    * is a filled in square
    x is the current position of the x player
    o is the current position of the o player

The board will always be 8 by 8.

Evaluation Function
-------------------
The evaluation function I implemented for this project considers two main aspects of a board state: (1) The number of available moves for my piece (x or o) and (2) the average distance from my piece to each occupied space (including the opponent's position). The weights given to each of these heuristic evaluations is somewhat arbitrary, but they each affect the total heuristic value roughly equally. The second value is multiplied by a constant simply due to the fact that the number of available moves is in most cases much larger than the average distance from occupied spaces. The two weighted values are added.

The function aims to find a move that maximizes the "safety" of the piece. If a board state allows a piece to have many available moves, it is unlikely that the piece will be trapped in the next few moves. Additionally, if a piece tries to stay as far away as possible from already occupied spaces, it generally means that it will be harder to trap that piece (it has a more open area of the board in which to move around). Thus, by combining these two heuristic evaluations, the overall strategy of this function is a defensive one. It attempts to avoid losing for as long as possible by finding the "safest" board states according to the aspects described above. 

The implementation of alpha-beta is essentially equivalent to the pseudocode given in class. The program allows the user to input the time limit and ply. To ensure many branches of the search tree are reached, the evaluation function is relatively simple and takes minimal time to calculate. This means that for a ply of 5, the algorithm should be able to search through every move up in an allotted time of 60 seconds. Additionally, the search ends if time runs out and the best move found so far is returned. While a less complex evaluation function may sacrifice accuracy, the ability to quickly find an optimal board state according to the simple heuristic should do well in avoiding losing situations. Thus, given the time limit, it seemed fitting to find a quick way to calculate which board states make it harder for the piece to run out of moves.