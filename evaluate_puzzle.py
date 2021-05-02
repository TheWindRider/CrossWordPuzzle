import numpy
import pandas
from collections import defaultdict

filename_words = "words.txt"
filename_layout = "layout.csv"

def pos_range(pos_row, pos_col, word, word_dir):
	word_len = len(word)
	if word_dir == 'v':
		row_range = range(pos_row, pos_row + word_len)
		col_range = [pos_col] * word_len
	elif word_dir == 'h':
		row_range = [pos_row] * word_len
		col_range = range(pos_col, pos_col + word_len)
	else:
		# throw exception
		row_range, col_range = None, None
	
	return [*zip(row_range, col_range, word)]

def represent_cells(input_puzzle):
	output_cells = defaultdict(set)
	puzzle_cells = input_puzzle[["row", "col", "word", "direction"]].apply(lambda x: pos_range(*x), axis=1)
	for word_cells in puzzle_cells:
		for row, col, letter in word_cells:
			output_cells[(row, col)].add(letter)
	
	return output_cells

def count_letters(input_words):
	return sum(map(len, input_words["word"]))

def measure_board(input_puzzle):
	word_length = numpy.array([*map(len, input_puzzle["word"])])
	word_dir = numpy.array(input_puzzle["direction"])
	row_end = numpy.array(input_puzzle["row"]) + (word_dir == 'v') * word_length
	col_end = numpy.array(input_puzzle["col"]) + (word_dir == 'h') * word_length
	return max(row_end), max(col_end)

def find_invalid_cells(input_cells):
	return [pos for pos, letters in input_cells.items() if len(letters) > 1]

def eval_puzzle(input_words, input_layout):
	input_puzzle = pandas.concat([input_words, input_layout], axis=1)
	input_cells = represent_cells(input_puzzle)
	
	num_letters = count_letters(input_words)
	board_y, board_x = measure_board(input_puzzle)
	num_cells = len(input_cells.keys())
	invalid_cells = find_invalid_cells(input_cells)
	
	result = {
		"valid": len(invalid_cells) == 0,
		"invalid_cells": invalid_cells,
		"board_shape": board_y / board_x,
		"cross_ratio": 1 - num_cells / num_letters,
		"board_density": num_cells / (board_x * board_y)
	}
	return result

puzzle_words = pandas.read_csv(filename_words, index_col=False, header=None, names=["word"])
puzzle_layout = pandas.read_csv(filename_layout, index_col=False)
print(eval_puzzle(puzzle_words, puzzle_layout))
