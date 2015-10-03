#!/bin/python
#The main game class that runs the game
#import Exception
from random import randint
from TicTacToe.player import Player
from copy import deepcopy
from TicTacToe.Comp import Comp
class PlaceError(Exception):
	def __init__(self, msg):
		print msg

class Game(object):
	
	def __init__(self):
		self.grid = [[None, None, None], [None, None, None], [None, None, None]]
		#if changing the dimensions of the grid, pls 
		#change the generation of the grid itself as
		#well as the below attribute. 
		self.dim = 3 #dimensions of the grid
		#self.main()		
				
	def print_grid(self):
		'''Prints the grid to the screen.'''
		#local copy of the grid
		grid = deepcopy(self.grid)
		
		#Replacing None by " "
		for row in range(self.dim):
			for box in range(len(grid[row])):
				if grid[row][box] == None:
					grid[row][box] = " "
		
		#Printing to the screen
		print "-"*6
		for row in grid:
			print "|".join(row)
			print "-"*6
	

			
	
	def check(self):
		'''Checks if any player has won.'''
		if self.horizontal(): return self.horizontal()
		
		if self.vertical(): return self.vertical()
		
		if self.diagnol(): return self.diagnol()
		
		return None
		
	"""def horizontal(self):
		'''Checks if any player has won in hoizontal lines.'''
		for row in self.grid:
			if row[0] == row[1] == row[2] and row[0] != None:
				return(row[0])
				
	def vertical(self):
		'''Checks if any player has won in vertical lines.'''
		for col in range(self.grid):
			if self.grid[0][col] == self.grid[1][col] == self.grid[2][col] and self.grid[0][col] != None:
				return self.grid[0][col]
	"""			
	#more portable versions:
	
	def horizontal(self):
		'''Checks if any player has won in horizontal lines.'''
		for row in self.grid:
			if row == [row[0]]*self.dim  and row[0] != None:
				return row[0]
		return None		

	def vertical(self):
		'''Checks if any player has won in vertical lines.'''
		for col in range(self.dim):
			line = []
			for row in range(self.dim):
				line.append(self.grid[row][col])
			if line == [line[0]]*self.dim and  line[0] != None:
				return line[0]
		return None
	
	def diagnol(self):
		'''Checks if any player has won in diagnol lines.'''
		#Diagnol 1 - from left top to right bottom.
		d1 = []
		for i in range(self.dim):
			d1.append(self.grid[i][i])
		if d1 == [d1[0]]*self.dim and d1[0] != None:
			return d1[0]
			
		#Diagnol 2 - from right top to left bottom.
		d2 = []
		for i in range(self.dim):
			d2.append(self.grid[i][(self.dim - 1) - i])
		if d2 == [d2[0]]*self.dim and d2[0] != None:
			return d2[0]
		return None
		
	def update(self, coord, sym):
		'''Changes box at co-ordinates coord to symbol sym.'''
		if self.grid[coord[0] - 1][coord[1] - 1] == None:
			self.grid[coord[0] - 1][coord[1] - 1] = sym
			return True
		else:
			raise PlaceError("Location " + str(coord) + " not empty!")
	
	def Player_init(self):
		'''Initializes players.'''
		self.p1 = Player('X')
		self.p2 = Player('O')

	def main(self):
		'''Starts the main gameplay.'''
		#Initialize players
		self.Player_init()
		winner = False
		self.print_grid()
		
		#Main game loop
		turns = 0
		while True:
			self.update(self.p1.Turn(deepcopy(self.grid)), self.p1.symbol)
			self.print_grid()
			turns += 1
			if self.check(): 
				winner = 1
				break
			if turns == 9:
				break
			self.update(self.p2.Turn(deepcopy(self.grid)), self.p2.symbol)
			self.print_grid()
			turns += 1
			if self.check():
				winner = 2	
				break
		
		#End of game
		if winner: print "Player %d Wins!" % winner
		elif turns == 9:
			print "Match Tied!"
		print "-------GAME OVER---------"
		

class CompGame(Game):
	def Player_init(self):
		'''Initializes players.'''
		Compturn = randint(1,2)
		if Compturn == 1:
			self.p1 = Comp("X", "O")
			self.p2 = Player("O")
		else:
			self.p1 = Player("X")
			self.p2 = Comp("O", "X")
		
