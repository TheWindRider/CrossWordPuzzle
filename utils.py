
def pos_range(pos_row, pos_col, word_len, word_dir):
	"""Produce (r, c) coordinates of all letters of a word

	:param pos_row: row position of first letter
	:param pos_col: column position of first letter
	:word_len: length of the word
	:word_dir: either 'v' for vertical or 'h' for horizontal
	:return: a list of (r, c) tuple to represent position of each letter

	>>> pos_range(1, 0, 3, 'h')
	[(1, 0), (1, 1), (1, 2)]
	"""
	if word_dir == 'v':
		row_range = range(pos_row, pos_row + word_len)
		col_range = [pos_col] * word_len
	elif word_dir == 'h':
		row_range = [pos_row] * word_len
		col_range = range(pos_col, pos_col + word_len)
	else:
		# TODO: throw exception
		row_range, col_range = None, None
	
	return [*zip(row_range, col_range)]
