# Fanta Tic-Tac-Toe 
An advanced, 3x3x3x3 version of traditional Tic-Tac-Toe 
[fantatictactoe.py](https://github.com/yangx18/Fanta-Tic-Tac-Toe/blob/main/main/fantatictactoe.py "Fanta Tic-Tac-Toe")

## Table of contents
* [General info](#genneral_info)
* [Screenshots](#screenshots)
* [Technologies](#technologies)
* [Setup](#setup)
* [Features](#features)
* [Status](#status)
* [Sources](#sources)
* [Contact](#contact)
* [License](#license)

## General Info
In this game, the board will be displayed into 9 grids, and in each grids there are small 9 squares. The AI player can place ***'O'*** into any square, and the other human player will choose the other ***'X'*** and place it into the marked grid or another. And there are some obstacles named ***"P"*** which will be placed at the beginning(nobody can place at ***"P"***) .If one grid has a horizontal, vertical, or diagonal row then this grid has been completed. The player has to mark other grids. Once who has dominated 3 grids is the winner.

## Screenshots
The following images show the player competes with the computer

![display1](https://github.com/yangx18/Fanta-Tic-Tac-Toe/blob/main/display1.png)
![display2](https://github.com/yangx18/Fanta-Tic-Tac-Toe/blob/main/display2.png)

## Technologies
Project is created with:

Programming language

* Python 3

Libraries

* Numpy
* TensorFlow
* Scipy
* Pandas

Algorithm

* Mininmax Algorithm
* Alpha-Beta Pruning

## Setup
To run this project, make sure you have installed python in your computer, here is the link: <https://www.python.org/>, then install it locally using:

```
conda install numpy
```
or

```
pip install numpy
```

## Features
Main concept of this game is followed by minimax algorithm. Minimax is a kind of backtracking algorithm that is used in decision making and game theory to find the optimal move for a player, assumig that your opponent also plays optimally.

![minimax](https://github.com/yangx18/Fanta-Tic-Tac-Toe/blob/main/minmax_func.png)

## Status
Project is in progress, and there are still some problem but we will fix them in the later semaster.(descriptions in () are possible solutions)

* AI is not smart and efficient enough( do more research and hold sticks with human players)
* Rules are not as smart as we assumed before in the proposal( make completely connections from sub-grid to whole board)


## Sources
This project is inspired by 

* 柯伊伯带的咸鱼 "让井字棋变得不一样——战略井字棋！" <https://www.bilibili.com/read/cv187749/> 
*  The Coding Train "Coding Challenge 154: Tic Tac Toe AI with Minimax Algorithm" <https://www.youtube.com/watch?v=trKjYdBASyQ&ab_channel=TheCodingTrain>
*  <https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-1-introduction/>
* <https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/>

## Contact
If you have any questions, feel free to contact us with the following emails:

* <xiaoyang2333@yahoo.com>
* <yzhou01@syr.edu>
* <leonlovesparis@gmail.com>

## License:
MIT License

Copyright (c) [2020] [Xiao Yang, Zhou Yixin, Li Ang]

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
 
