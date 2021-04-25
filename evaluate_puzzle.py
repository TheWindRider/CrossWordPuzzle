import pandas

def add_puzzle_cells(input_letter, input_row, input_col, puzzle_cells):
	if (input_row, input_col) not in puzzle_cells:
		puzzle_cells[(input_row, input_col)] = set()
	puzzle_cells[(input_row, input_col)].add(input_letter)
	return

def represent_puzzle_cells(input_words, input_layout):
	output_cells = {}

	for idx, info in input_layout.iterrows():
		curr_word = input_words[idx]
		start_row, start_col = info["row"], info["col"]

		if info["direction"] == 'v':
			curr_col = start_col
			for letter_id, curr_letter in enumerate(curr_word):
				curr_row = start_row + letter_id
				add_puzzle_cells(curr_letter, curr_row, curr_col, output_cells)

		elif info["direction"] == 'h':
			curr_row = start_row
			for letter_id, curr_letter in enumerate(curr_word):
				curr_col = start_col + letter_id
				add_puzzle_cells(curr_letter, curr_row, curr_col, output_cells)

		else:
			print("Invalid layout for word: {}".format(curr_word))

	return output_cells

def count_letters(input_words):
	return sum([len(each_word) for each_word in input_words])

def find_invalid_cells(input_cells):
	return [pos for pos, letters in input_cells.items() if len(letters) > 1]

def measure_board(input_cells):
	all_rows = [pos[0] for pos in input_cells.keys()]
	all_cols = [pos[1] for pos in input_cells.keys()]
	min_row, max_row = min(all_rows), max(all_rows)
	min_col, max_col = min(all_cols), max(all_cols)
	return (max_row - min_row + 1, max_col - min_col + 1)

def eval_puzzle(input_words, input_cells):
	num_letters = count_letters(input_words)
	num_cells = len(input_cells.keys())
	invalid_cells = find_invalid_cells(input_cells)
	board_y, board_x = measure_board(input_cells)

	result = {
		"valid": len(invalid_cells) == 0,
		"invalid_cells": invalid_cells,
		"board_shape": board_y / board_x,
		"cross_ratio": 1 - num_cells / num_letters,
		"board_density": num_cells / (board_x * board_y)
	}
	return result

filename_words = "words.txt"
filename_layout = "layout.csv"

puzzle_words = open(filename_words, 'r').read().split('\n')
puzzle_words = [each_word for each_word in puzzle_words if len(each_word) > 0]
puzzle_layout = pandas.read_csv(filename_layout, index_col=False)

puzzle_cells = represent_puzzle_cells(puzzle_words, puzzle_layout)
print(eval_puzzle(puzzle_words, puzzle_cells))
