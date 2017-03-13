# # Tic Tac Toe 
square = ['*'] 
board =  [] 

class row():
	
	row = square * 3

test = row()
print(test.row)

def display_board():

	for i in range(3):
		board.append(row())
	
	board[1].row[0] = 'X'
	return board

for each in display_board():

	print(each.row)
	
