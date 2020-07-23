# Sudoku in Python

Yet another Sudoku solver

This **doesn't** use the common backtracking algorithms to solve puzzles that are easy, medium and hard.

However,this **doesn't work for expert level puzzles**. Probably i have to look at backtracking algorithm for this.

# Usage and Description

> Empty cells must be represented as 0

There are two ways to supply input to the program

## Line (String)

`main.sudokuLine(line)`

## 9x9 Grid of numbers

`main.sudokuGrid(grid)`

# Examples

## Line

Input: `704530200008160000102000685007910068005007302680054190000700800250000473000040026`

Output: `76453821959816273413247968542791356891568734268325419734972685125689147387134592`


## Grid

Input: `[[7, 0, 4, 5, 3, 0, 2, 0, 0], [0, 0, 8, 1, 6, 0, 0, 0, 0], [1, 0, 2, 0, 0, 0, 6, 8, 5], [0, 0, 7, 9, 1, 0, 0, 6, 8], [0, 0, 5, 0, 0, 7, 3, 0, 2], [6, 8, 0, 0, 5, 4, 1, 9, 0], [0, 0, 0, 7, 0, 0, 8, 0, 0], [2, 5, 0, 0, 0, 0, 4, 7, 3], [0, 0, 0, 0, 4, 0, 0, 2, 6]]`

Output: `[[7, 6, 4, 5, 3, 8, 2, 1, 9], [5, 9, 8, 1, 6, 2, 7, 3, 4], [1, 3, 2, 4, 7, 9, 6, 8, 5], [4, 2, 7, 9, 1, 3, 5, 6, 8], [9, 1, 5, 6, 8, 7, 3, 4, 2], [6, 8, 3, 2, 5, 4, 1, 9, 7], [3, 4, 9, 7, 2, 6, 8, 5, 1], [2, 5, 6, 8, 9, 1, 4, 7, 3], [8, 7, 1, 3, 4, 5, 9, 2, 6]]`

# Releases

*24th July 2020*

* Not efficient
* Works for Easy, Medium and Hard levels
* Expert level doesn't work.

# Results

Tested using data from Sudoku.com. Time to run 100 tests each

* Easy - 0m0.211s
* Medium - 0m0.330s
* Hard - 0m0.671s
