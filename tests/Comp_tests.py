# Test cases for Comp
from TicTacToe.Comp import Comp
from nose.tools import assert_equal
def test_is_terminal():
	testComp = Comp("X", "O")
	gridh = [
			["X", "X", "X"],
			[None, "O", "O"],
			["X", "O", None]
	]
	
	gridv = [
			["X", "O", None],
			[None, "O", "X"],
			["X", "O", None]
	]
	
	gridd = [
			["X", "O", "O"],
			["O", "X", "X"],
			["X", "O", "O"]
	]

	assert_equal(testComp.is_terminal(gridh), 1)
	assert_equal(testComp.is_terminal(gridv), -1)
	assert_equal(testComp.is_terminal(gridd), 0)