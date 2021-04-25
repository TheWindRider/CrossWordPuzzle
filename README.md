# CrossWordPuzzle
A canvas for future project

## Key Element
1. Words list
2. Words clue
3. Crossword puzzle layout
4. (more)

What feels interesting to me is these elements can be either input or output depending on the application.
A puzzle layout can be the input to a solver UI, but can also be the output of an automatic generator. 

## Project 0: Warm Up
`words.txt` and `layout.csv` illustrate a toy example:
| | | | | | |
| :-: | :-: | :-: | :-: | :-: | :-: |
|f| | |b| | |
|i| | |u| | |
|z|i|g|z|a|g|
|z| | |z| | |

I'm interested in **validating** a puzzle is legit, meaning no conflict at any cell of the board. I'm more interested in **evaluating** a puzzle is good, preferably populating the board densely, and also have many words "crossing" each other.
