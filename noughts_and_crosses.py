def create_state(width):
	#Creates a board as a list of Nones 
	
	table = [None for cells in range(0, width**2)]

	return table

def play_game():

	x_state = create_state(3)
	y_state = create_state(3)
	turn = 1
	board = print_board(x_state, y_state)

	while turn < 10:
		state = take_turn(turn, x_state, y_state, board)
		turn = state[0]
		x_state = state[1]
		y_state = state[2]
		board = print_board(x_state, y_state)
		if check_winner(x_state):
			print("Crosses win!")
			break
		elif check_winner(y_state):
			print('Noughts win!')
			break

	play_again()


def take_turn(turn, x_state, y_state, board):

	play = 0

	while play < 1 or play > 9:
		try:
			play = int(input("Where would you like to play? (1-9) \n"))
		except: 
			print("this is not a number")

	if board[play - 1] == (None, None):

		if turn % 2:
			x_state[play - 1] = play
		else:
			y_state[play - 1] = play

		turn += 1

	else:
		print("This spot is taken")

	return [turn, x_state, y_state]

def print_board(x_state, y_state):

	board = list(zip(x_state, y_state))
	board_irl = []

	for x, y in board:
		if x:
			board_irl.append("X")
		elif y:
			board_irl.append('0')
		else:
			board_irl.append(' ')

	current_position = []
	width = int(len(board_irl)**(1/2))

	current_position = [board_irl[i:i + width] for i in range(0, width**2, width)]

	row_num = 0
	for rows in current_position:
		print("|".join(rows))
		row_num += 1
		if row_num < len(rows):
			print("__" * len(rows))

	return board

def check_winner(state):
	winning_positions = [[1,2,3], [4,5,6], [7,8,9], [1,4,7], [2,5,8], [3,6,9], [1,5,9], [3,5,7]]
	for perm in winning_positions:
		if set(perm) <= set(state):
			return True
	else:
		return False

def play_again():

	ans = 0

	while ans != 'yes' and ans != 'no':
		ans = input("Do you want to play again? \n").lower()

	if ans == 'yes':
		play_game()

play_game()