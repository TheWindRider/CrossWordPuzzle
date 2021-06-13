import numpy
import pandas
from utils import pos_range

class CrossWordPuzzle():
	def __init__(self, word_df, layout_df):
		assert len(word_df) == len(layout_df)
		self.word_list = word_df["word"]
		self.puzzle_df = pandas.concat([word_df, layout_df], axis=1)
		self.puzzle_df["len"] = [*map(len, self.word_list)]
		self.puzzle_dict = self._init_dict_().copy()
		self.num_rows, self.num_cols = self._init_size_()

	def _init_dict_(self):
		output_puzzle = {}
		word_pos = self.puzzle_df[["row", "col", "len", "direction"]].apply(
			lambda x: pos_range(*x), axis=1)
		
		for pos, word in zip(word_pos, self.word_list):
			assert len(pos) == len(word)
			for (row, col), letter in zip(pos, word):
				if (row, col) not in output_puzzle: 
					output_puzzle[(row, col)] = letter
				else:
					assert output_puzzle[(row, col)] == letter
		
		return output_puzzle

	def _init_size_(self):
		word_len = numpy.array(self.puzzle_df["len"])
		word_dir = numpy.array(self.puzzle_df["direction"])
		
		row_end = numpy.array(self.puzzle_df["row"]) + (word_dir == 'v') * word_len
		col_end = numpy.array(self.puzzle_df["col"]) + (word_dir == 'h') * word_len

		return max(row_end), max(col_end)

	def eval_cross_ratio(self):
		total_letters = sum(map(len, self.word_list))
		total_cells = len(self.puzzle_dict)
		# higher ratio => better puzzle design
		return 1 - total_cells / total_letters
	
	def eval_shape_ratio(self):
		# shape ratio closer to 1 => better puzzle design
		return self.num_rows / self.num_cols
	
	def eval_density(self):
		# density closer to 100% => better puzzle design
		return len(self.puzzle_dict) / (self.num_rows * self.num_cols)
	
	def evaluate(self):
		puzzle_quality = {
			"words_cross": self.eval_cross_ratio(),
			"board_shape": self.eval_shape_ratio(),
			"board_density": self.eval_density()
		}
		return puzzle_quality
