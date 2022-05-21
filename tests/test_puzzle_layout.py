import unittest
import pandas
from puzzle import CrossWordPuzzle


class SimpleCorrectCase(unittest.TestCase):
	puzzle_words = pandas.read_csv("tests/data/words.txt", index_col=False, header=None, names=["word"])
	puzzle_layout = pandas.read_csv("tests/data/layout.csv", index_col=False)
	puzzle = CrossWordPuzzle(puzzle_words, puzzle_layout)

	def test_board_size(self):
		self.assertEqual(self.puzzle.num_rows, 4)
		self.assertEqual(self.puzzle.num_cols, 6)

	def test_letter_count(self):
		self.assertEqual(len(self.puzzle.puzzle_dict), 12)
		self.assertEqual(sum(map(len, self.puzzle.word_list)), 14)

if __name__ == '__main__':
    unittest.main()
