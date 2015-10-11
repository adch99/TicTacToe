#!/bin/python
from TicTacToe.player import Player
from itertools import permutations

class Comp(Player):
	
	def __init__(self, symbol, opp)
		super(Comp, self).__init__(symbol)
		self.opp = opp

	def lines(self, cur_grid):
		'''Returns a dictionary of all horizontal, vertical and 
		diagnol lines.'''
		line_dict = {}
		
		def horizontal():
			h_lines = ()
			for line in cur_grid:
				h_lines += tuple(line)
			return h_lines	
		
		def vertical():
			v_lines = ()
			for col in range(self.dim):
				line = ()
				for row in range(self.dim):
					line += (cur_grid[row][col],)
				v_lines += line
			return v_lines
		
		def diagnol():
			# diagnol 1
			d1 = ()
			for i in range(self.dim):
				d1 += (cur_grid[i][i],)
				
			# diagnol 2
			d2 = ()
			for i in range(self.dim):
				d2 += (cur_grid[i][self.dim - i],)
			d_lines = (d1, d2)
			return d_lines
			
			line_dict["Horizontal"] = horizontal()
			line_dict["Vertical"] = vertical()
			line_dict["Diagnol"] = diagnol()
			return line_dict


	def Turn(self, cur_grid):		
		'''Returns the Computer's move'''
		self.dim = self.dim
		lines = self.lines(cur_grid)
		if self.Can_I_win(cur_grid): return self.Can_I_win(cur_grid)
		elif self.Can_I_prevent(cur_grid): return self.Can_I_prevent()
		else: return self.Do_something_else(cur_grid)


	def Can_I_win(self, grid):
		'''Can the computer win in the next move?'''
		print "Can_I_Win"
		
		req_line = [self.sym] * (self.dim - 1) + [None]
		
		lines = self.lines()
		def horizontal():
			h_lines = lines["Horizontal"]
			for line in range(len(h_lines)):
				if line in permutations(req_line):
					return (h_lines.index(line) + 1, h_lines[line].index(None) + 1)
		
		def vertical():
			v_lines = lines["Vertical"]
			for line in range(len(v_lines)):
				if v_lines[line] in permutations(req_line):
					return (v_lines[line].index(None) + 1, line + 1)
		
		def diagnol():
			d_lines = lines["Diagnol"]
			# diagnol 1
			line = d_lines[0]
			if line in permutations(req_line):
				return (line.index(None) + 1,)*2
			
			# diagnol 2
			line = d_lines[1]
			if line in permutations(req_line):
				return (line.index(None) + 1, self.dim + 1 - line.index(None))
			 
		if horizontal(): return horizontal()
		elif vertical(): return vertical()
		elif diagnol(): return diagnol()
		else: return None
		
		
	def Can_I_prevent(self, grid):
		'''Can the Computer prevent the other player from winning?'''
		print "Can_I_prevent"
		
		req_line = [self.opp] * (self.dim - 1) + [None]
		
		lines = self.lines()
		def horizontal():
			h_lines = lines["Horizontal"]
			for line in range(len(h_lines)):
				if h_lines[line] in permutations(req_line):
					return (line + 1, h_lines[line].index(None) + 1)
		
		def vertical():
			v_lines = lines["Vertical"]
			for line in range(v_lines):
				if v_lines[line] in permutations(req_line):
					return(v_lines[line].index(None), line + 1)			

					
		def diagnol():
			d_lines = lines["Diagnol"]
			# Diagnol 1
			line = d_lines[0]
			if line in permutations(req_line):
				return (line.index(None) + 1,)*2
			
			#Diagnol 2 
			line = d_lines[1]
			if line in permutations(req_line):
				return (line.index(None) + 1, self.dim - line.index(None))
			
		if horizontal(): return horizontal()
		elif vertical(): return vertical()
		elif diagnol(): return diagnol()
		else: return None


	def Do_something_else(self, grid):
		'''Returns a move in case Computer can't win or prevent
		opponent from winning.'''
		print "Do_something_else"
		
