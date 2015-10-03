import Tkinter

def GUI():
	"""Runs a GUI frontend for the TicTacToe program."""
	window = Tkinter.Tk()
	window.title("TicTacToe - Khotti Patelli Inc.")
	
	Buttons = [[],[],[]]
	
	for i in range(3):
		for j in range(3):
			Button = Tkinter.Button(window, )#,text=)
			Buttons.append(Button)
			Button.grid(row=i, column=j,ipadx=10, ipady=10)
	window.mainloop()
	
def GUI_update(grid):
	"""Updates the the GUI"""
	for row in range(len(Buttons)):
		for col in range(len(row)):
			Buttons[row][col].configure(text=grid[row][col])
	
def GUI_Turn(turn):
	"""Pushes the turns to the global turn stack."""
	global input_stack
	input_stack.append(turn)

GUI()
