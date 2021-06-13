import argparse
import pandas
from puzzle import CrossWordPuzzle

if __name__ == "__main__":
	parser = argparse.ArgumentParser()
	parser.add_argument("--word_file", help="Filename of list of words", default="words.txt")
	parser.add_argument("--layout_file", help="Filename of position of words", default="layout.csv")
	args = parser.parse_args()

	puzzle_words = pandas.read_csv(args.word_file, index_col=False, header=None, names=["word"])
	puzzle_layout = pandas.read_csv(args.layout_file, index_col=False)
	puzzle = CrossWordPuzzle(puzzle_words, puzzle_layout)
	print(puzzle.evaluate())
