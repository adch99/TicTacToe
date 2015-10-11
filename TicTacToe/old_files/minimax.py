	# -1 == Loss
	# 1 == Win
	# 0 == Tie

	def Minimax(self, grid):
		"""Chooses the move among all possible moves which has least chance of loss."""
		return self.Max(grid)

	def Min(self, grid, possible_moves):		
		"""Returns the minimum chance of winning for the opponent in their turn."""

		# Get all possible values
		moves = self.possible_moves(grid)
		
		# Values for all moves
		moves_values = []
		
		for move in moves:
			sim_grid = self.simulate_move(move, self.opp_sym, deepcopy(grid))
			isterm = self.is_terminal(sim_grid)
			if isterm:
				moves_values.append(isterm)
			else:
				moves_values.append(self.Max(sim_grid))
		
		return min(moves_values)

			
	def Max(self, grid):
		"""Returns the move with maximum chance of winning
		when simulating Computer's turn."""
		
		# Get all possible moves
		moves = self.possible_moves(grid)
		
		# Values for all moves
		moves_values = []
		
		for move in moves:
			sim_grid = self.simulate_move(move, self.sym, deepcopy(grid))
			isterm = self.is_terminal(sim_grid)
			if isterm:
				moves_values.append(isterm)
			else:
				moves_values.append(self.Min(sim_grid))
		
		return max(moves_values)

	def simulate_move(self, move, sym, grid):
		"""Simulates the grid after a given move."""
		grid[move[0]][move[1]] = sym
		return grid

		
	# Analysis of cases i.e. terminal or not
	# and which kind of terminal case.
	def is_terminal(self, grid):
		"""
		Checks if given case is a terminal case.
		If yes, returns the utility value of the case.
		"""
		winner  = self.check(grid)
		if winner:
			return utility(winner)
		else:
			return False
		
	def horizontal(self, grid):
		'''Checks if any player has won in horizontal lines.'''
		for row in grid:
			if row == [row[0]]*self.dim  and row[0] != None:
				return row[0]
		return None		

	def vertical(self, grid):
		'''Checks if any player has won in vertical lines.'''
		for col in range(self.dim):
			line = []
			for row in range(self.dim):
				line.append(grid[row][col])
			if line == [line[0]]*self.dim and  line[0] != None:
				return line[0]
		return None

	def diagnol(self, grid):
		'''Checks if any player has won in diagnol lines.'''
		#Diagnol 1 - from left top to right bottom.
		d1 = []
		for i in range(self.dim):
			d1.append(grid[i][i])
		if d1 == [d1[0]]*self.dim and d1[0] != None:
			return d1[0]
			
		#Diagnol 2 - from right top to left bottom.
		d2 = []
		for i in range(self.dim):
			d2.append(self.grid[i][(self.dim - 1) - i])
		if d2 == [d2[0]]*self.dim and d2[0] != None:
			return d2[0]
		return None
		
	def tie(self, grid):
		"""Checks if its a tie or not."""
		# This function relies on checking for winner beforehand.
		for row in grid:
			for col in row:
				if col == None:
					return False
		return True
		
	def check(self, grid):
		'''Checks if any player has won.'''
		if self.horizontal(grid): return self.horizontal()
		
		elif self.vertical(grid): return self.vertical()
		
		elif self.diagnol(grid): return self.diagnol()
		
		elif self.tie(grid): return None 
		
		else:
			return False
			
	def utility(self, winner):
		if winner == self.sym: return 1
		elif winner == self.opp_sym: return -1
		elif winner == None: return 0
		else:
			raise Exception, "Something is wrong!"
			
	def all_possible(self, grid):
		"""Get all possible moves i.e. empty spaces in the given grid case."""
		possible_moves = []
		for row in range(self.dim):
			for col in range(self.dim):
				if grid[row][col] == None:
					possible_moves.append((row,col))
		return possible_moves