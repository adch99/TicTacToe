def GUI_main(self):
	'''Starts the main gameplay.'''
	#Initialize players
	self.Player_init()
	winner = False
	self.GUI_update(self.grid)
	
	#Main game loop
	turns = 0
	while True:
		self.update(self.p1.Turn(deepcopy(self.grid)), self.p1.symbol)
		self.GUI_update(self.grid)
		turns += 1
		if self.check(): 
			winner = 1
			break
		if turns == 9:
			break
		self.update(self.p2.Turn(deepcopy(self.grid)), self.p2.symbol)
		self.GUI_update(self.grid)
		turns += 1
		if self.check():
			winner = 2	
			break
	
	#End of game
	if winner: print "Player %d Wins!" % winner
	elif turns == 9:
		print "Match Tied!"
	print "-------GAME OVER---------"

