#!/bin/python
#Basic Player-to-Player tests
from TicTacToe.engine import Game
from nose.tools import assert_equal
def ttester(P1moves, P2moves):
	main = Game()
	#Initialize players
	main.Player_init()
	winner = False
	main.print_grid()
	
	#Main game loop
	turns = 0
	for i in range(len(P1moves)):
		main.update(main.p1.Turn(main.grid, P1moves[i]), main.p1.symbol)
		turns += 1
		if main.check(): 
			winner = 1
			break
		if turns == 9:
			break
		main.update(main.p2.Turn(main.grid, P2moves[i]), main.p2.symbol)
		turns += 1
		if main.check():
			winner = 2	
			break
	
	
	if winner:
		return winner
	elif turns == 9:
		return "Tie"

	
def test_horizontal():
	P1moves = [(1,1), (1,2), (1,3)]
	P2moves = [(2,2), (3,3)]
	assert_equal(ttester(P1moves, P2moves), 1)

def test_vertical():
	P1moves = [(2,2), (2,1), (2,3)]
	P2moves = [(1,1), (3,1)]
	assert_equal(ttester(P1moves, P2moves), 1)
	
def test_diagnol1():
	P1moves = [(1,1), (2,2), (3,3)]
	P2moves = [(2,1), (2,3)]
	assert_equal(ttester(P1moves, P2moves), 1)

def test_diagnol2():
	P1moves = [(1,3), (2,2), (3,1)]
	P2moves = [(1,1), (2,1)]
	assert_equal(ttester(P1moves, P2moves), 1)

def test_tie():
	P1moves = [(1,1), (2,2), (2,3), (3,1), (3,2)]
	P2moves = [(1,2), (3,3), (2,1), (1,3)]
	assert_equal(ttester(P1moves, P2moves), "Tie")
