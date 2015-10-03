#!/bin/python
# The basic player class

class Player(object):
	
	def __init__(self,symbol):
		self.symbol = symbol
		
	def legal(self, move, grid):
		'''Checks if move is legal.'''
		try:		
			if grid[move[0] - 1][move[1] - 1] == None:
				return True
			else:
				print "The place is already occupied!"
				return False
		except IndexError:
			print "The place doesn't exist!"
			return False
		
	def help(self):
		'''Prints a help message in case of illegal move.'''
		print """

		  1   2   3
		-------------
	1	|   |   |   |
		-------------
	2	|   |   |   |
		-------------
	3	|   |   |   |
		-------------
		
		"""

	def take(self):
		'''Takes the move from user's console and returns in the form of a tuple.'''
		move = raw_input("Player %s, Enter your move: " % self.symbol)
		move = move.split(",")
		try:
			return ( int(move[0]), int(move[1]) )
		except ValueError:
			print """
	Move should be in the form: row,col
	Like 1,2 or 3,1
"""
			self.help()
			return self.take()
			
	def Turn(self, cur_grid, turn=None):
		'''Returns the players move.'''
		# If input is already given take that
		if turn: return turn
		
		#else take from console
		else:
			turn = self.take()
			

		while(not self.legal(turn, cur_grid)):
			print "Your move is not legal.\n"
			self.help()
			turn = self.take()
		return turn
			
		
		
		

			
		
		
