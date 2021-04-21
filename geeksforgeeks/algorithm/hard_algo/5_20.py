Design a Chess Game



 **Problem Statement** : The problem is to design a Chess Game using Object
Oriented Principles.

 **Asked In:** Adobe, Amazon, Microsoft, etc.

 **Solution:**  
These type of questions are asked in interviews to Judge the Object-Oriented
Design skill of a candidate. So, first of all we should think about the
classes.

The main classes will be:

  1.  **Spot:** A spot represents one block of the 8×8 grid and an optional piece.
  2.  **Piece:** The basic building block of the system, every piece will be placed on a spot. Piece class is an abstract class. The extended classes (Pawn, King, Queen, Rook, Knight, Bishop) implements the abstracted operations.
  3.  **Board:** Board is an 8×8 set of boxes containing all active chess pieces.
  4.  **Player:** Player class represents one of the participants playing the game.
  5.  **Move:** Represents a game move, containing the starting and ending spot. The Move class will also keep track of the player who made the move.
  6.  **Game:** This class controls the flow of a game. It keeps track of all the game moves, which player has the current turn, and the final result of the game.

