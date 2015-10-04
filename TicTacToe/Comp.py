#!/bin/python
from TicTacToe.player import Player
from copy import deepcopy

class Comp(Player):
	
	def __init__(self, symbol, opp):
		super(Comp, self).__init__(symbol)
		self.opp = opp
		self.dim = 3

	def Turn(self, cur_grid):		
		'''Returns the Computer's move'''
		move = self.Minimax(deepcopy(cur_grid))
		return (move[0] + 1, move[1] + 1)
	
	# -1 == Loss
	# 1 == Win
	# 0 == Tie

	def Minimax(self, grid):
		"""Chooses the move among all possible moves which has least chance of loss."""
		return self.Max(grid)

	def Min(self, grid):		
		"""Returns the minimum chance of winning for the opponent in their turn."""
		print "Entering Min" #debug
		# Get all possible values
		moves = self.all_possible(grid)
		
		# Values for all moves
		moves_values = []
		
		for move in moves:
			sim_grid = self.simulate_move(move, self.opp, deepcopy(grid))
			if self.is_terminal(sim_grid):
				moves_values.append(self.utility(sim_grid)
			else:
				moves_values.append(self.Max(sim_grid))
		print "Min: moves_values =",moves_values #debugging
		return min(moves_values)

			
	def Max(self, grid):
		"""Returns the move with maximum chance of winning
		when simulating Computer's turn."""
		print "Entering Max" #debug
		# Get all possible moves
		moves = self.all_possible(grid)
		if moves == []: raise Exception, "No all_possible() moves."
		# Values for all moves
		moves_values = []
		
		for move in moves:
			sim_grid = self.simulate_move(move, self.symbol, deepcopy(grid))
			isterm = 
			if self.is_terminal(sim_grid):
				moves_values.append(self.utility(sim_grid))
			else:
				moves_values.append(self.Min(sim_grid))
		print "Max: moves_values =",moves_values #debugging

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
		if winner in [self.symbol, self.opp, None]:
			return True
		else:
			return False
		
	def horizontal(self, grid):
		'''Checks if any player has won in horizontal lines.'''
		for row in grid:
			if row == [row[0]]*self.dim  and row[0] != None:
				return row[0]
		return False		

	def vertical(self, grid):
		'''Checks if any player has won in vertical lines.'''
		for col in range(self.dim):
			line = []
			for row in range(self.dim):
				line.append(grid[row][col])
			if line == [line[0]]*self.dim and  line[0] != None:
				return line[0]
		return False

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
			d2.append(grid[i][(self.dim - 1) - i])
		if d2 == [d2[0]]*self.dim and d2[0] != None:
			return d2[0]
		return False
		
	def tie(self, grid):
		"""Checks if its a tie or not."""
		# This function relies on checking for winner beforehand.
		for row in grid:
			if None in row:
				return False
		return True
		
	def check(self, grid):
		'''Checks if any player has won.'''
		if self.horizontal(grid): return self.horizontal(grid)
		
		elif self.vertical(grid): return self.vertical(grid)
		
		elif self.diagnol(grid): return self.diagnol(grid)
		
		elif self.tie(grid): return None 
		
		else:
			return False
			
	def utility(self, winner):
		"""Assigns a value to each of the terminal cases."""
		if winner == self.symbol: return 1
		elif winner == self.opp: return -1
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
