from __future__ import annotations
from chess_pieces import Pawn, Knight, Rook, Bishop, Queen, King
import curses
import chess_board_test





def display_board_curses(board, chess_board_pad):
	
	def determine_displayed_symbol(x:int, y:int, y_index, x_sub_index) -> str:
		unformatted_symbol = " "
		team_color = ""
		for piece in board.living_list:
			if x == piece.vec.x and y == piece.vec.y:
				unformatted_symbol = piece.type
				team_color = piece.team
				break
		color_pair_num = 0	
		if team_color == "blue":
			if y % 2 == 0:
				if x % 2 == 1:
					color_pair_num = 4

				else:
					color_pair_num = 1

			else:
				if x % 2 == 1:
					color_pair_num = 1

				else:
					color_pair_num = 4

		elif team_color == "red":
			if y % 2 == 0:
				if x % 2 == 1:
					color_pair_num = 3

				else:
					color_pair_num = 2

			else:
				if x % 2 == 1:
					color_pair_num = 2

				else:
					color_pair_num = 3

		else:
			if y % 2 == 0:
				if x % 2 == 1:
					color_pair_num = 5

				else:
					color_pair_num = 6

			else:
				if x % 2 == 1:
					color_pair_num = 6
					#stdscr.addstr(y_index, x_sub_index+2, unformatted_symbol, curses.color_pair(3))
				else:
					color_pair_num = 5

		chess_board_pad.addstr(y_index, x_sub_index+2, unformatted_symbol, curses.color_pair(color_pair_num) | curses.A_BOLD)

		# stdscr.addstr(y_index, x_sub_index+2, unformatted_symbol, curses.)
		# return unformatted_symbol

	#run check at beginning to see if terminal can use custom colors.
	#turn custom colors on or off depending on terminal capability. 

	y_index = 0
	#FIXXXXXXXXXXXXXXX1-21
	x_index = 1
	y_reference_num = 8
	x_reference_spaced_chars = "      A    B    C    D    E    F    G    H"
	curses.init_pair(1,curses.COLOR_BLUE,curses.COLOR_YELLOW)	#blue_WHITE
	curses.init_pair(2,curses.COLOR_MAGENTA,curses.COLOR_YELLOW)	#red_WHITE
	curses.init_pair(3,curses.COLOR_MAGENTA,curses.COLOR_BLACK)	#red_BLACK
	curses.init_pair(4,curses.COLOR_BLUE,curses.COLOR_BLACK)	#blue_BLACK
	curses.init_pair(5,curses.COLOR_BLACK,curses.COLOR_BLACK)	#black_BLACK
	curses.init_pair(6,curses.COLOR_WHITE,curses.COLOR_YELLOW)	#white_WHITE
	curses.init_pair(7,curses.COLOR_GREEN,curses.COLOR_BLACK) 	#green_BLACK


	chess_board_pad.addstr(y_index, x_index, x_reference_spaced_chars, curses.color_pair(7))
	y_index += 1
	for y in range(board.y_rows):#prints entire board and assigned symbols
		chess_board_pad.addstr(y_index, x_index, str(y_reference_num), curses.color_pair(7))
		chess_board_pad.addstr(y_index, (x_index + 1), "|| ", curses.color_pair(4))
		x_sub_index = 5
		if y % 2 == 0:
			for x in range(board.x_cols):
				if x_sub_index % 2 == 1:
					chess_board_pad.addstr(y_index, x_sub_index, " (", curses.color_pair(1))
					determine_displayed_symbol(x, y, y_index, x_sub_index)
					#stdscr.addstr(y_index, x_sub_index+2, determine_displayed_symbol(x, y))
					chess_board_pad.addstr(y_index, x_sub_index+3, ") ", curses.color_pair(1))
					x_sub_index += 5 
				else:
					chess_board_pad.addstr(y_index, x_sub_index, " (", curses.color_pair(4))
					determine_displayed_symbol(x, y, y_index, x_sub_index)
					#stdscr.addstr(y_index, x_sub_index+2, determine_displayed_symbol(x, y))
					chess_board_pad.addstr(y_index, x_sub_index+3, ") ", curses.color_pair(4))
					x_sub_index += 5
		else:
			for x in range(board.x_cols):
				if x_sub_index % 2 == 1:
					chess_board_pad.addstr(y_index, x_sub_index, " (", curses.color_pair(4))
					determine_displayed_symbol(x, y, y_index, x_sub_index)
					#stdscr.addstr(y_index, x_sub_index+2, determine_displayed_symbol(x, y))
					chess_board_pad.addstr(y_index, x_sub_index+3, ") ", curses.color_pair(4))
					x_sub_index += 5 
				else:
					chess_board_pad.addstr(y_index, x_sub_index, " (", curses.color_pair(1))
					determine_displayed_symbol(x, y, y_index, x_sub_index)
					#stdscr.addstr(y_index, x_sub_index+2, determine_displayed_symbol(x, y))
					chess_board_pad.addstr(y_index, x_sub_index+3, ") ", curses.color_pair(1))
					x_sub_index += 5
		chess_board_pad.addstr(y_index, x_sub_index, " ||", curses.color_pair(4))
		x_sub_index += 3
		chess_board_pad.addstr(y_index, x_sub_index, str(y_reference_num), curses.color_pair(7))
		y_reference_num -= 1
		y_index += 2
	chess_board_pad.addstr((y_index - 1), x_index, x_reference_spaced_chars, curses.color_pair(7))
	chess_board_pad.refresh()
	#$you are not the lies in your head.




def display_current_loc(stdscr, cur_loc, origin):
		y_coord_ref = origin[0]
		x_coord_ref = origin[1]

		x_dict = {}
		y_dict = {}
		x_additive = 5
		y_additive = 2 
		letters = ('A','B','C','D','E','F','G','H')

		for x in range(0,8):
			x_dict[origin[1]+x*x_additive] = letters[x]
		for y in range(0,8):
			y_dict[origin[0]+y*y_additive] = 8-y

		stdscr.addstr(22,2,"({},{})".format(cur_loc[0], cur_loc[1]))
		print_string = '({}, {})'.format(y_dict[cur_loc[0]], x_dict[cur_loc[1]])
		stdscr.addstr(21,2,"CursorLoc: {}".format(print_string))

def move_cb_cursor(stdscr,cb_y_pos,cb_x_pos):
	origin = [0,0]
	origin[0] = cb_y_pos + 1
	origin[1] = cb_x_pos + 7
	def check_move_in_limit(move_location, old_cur_loc):
		y_limit = list(range(origin[0],origin[0]+15))
		x_limit = list(range(origin[1],origin[1]+36))

		if move_location[0] in y_limit and move_location[1] in x_limit:
		
			stdscr.move(move_location[0], move_location[1])
			stdscr.refresh()
			
			cur_loc = (move_location[0],move_location[1])		
			display_current_loc(stdscr, cur_loc, origin)
			
			stdscr.refresh()
			stdscr.move(move_location[0], move_location[1])
			stdscr.refresh()

			return (move_location[0], move_location[1])

		else:
			return old_cur_loc

	left = 260
	right = 261
	up = 259
	down = 258
	q = 113
	stdscr.move(origin[0], origin[1])
	stdscr.refresh()
	cur_loc = [origin[0],origin[1]]
	cursor_direction = 0

	
	move_location = [0, 0]

	while cursor_direction != 113:
		cursor_direction = stdscr.getch()


		if cursor_direction == left:
			move_location[0] = cur_loc[0]
			move_location[1] = cur_loc[1] - 5
			cur_loc = check_move_in_limit(move_location, cur_loc)
		elif cursor_direction == right:
			move_location[0] = cur_loc[0]
			move_location[1] = cur_loc[1] + 5
			cur_loc = check_move_in_limit(move_location, cur_loc)
		elif cursor_direction == up:
			move_location[0] = cur_loc[0] - 2
			move_location[1] = cur_loc[1]
			cur_loc = check_move_in_limit(move_location, cur_loc)
		elif cursor_direction == down:
			move_location[0] = cur_loc[0] + 2
			move_location[1] = cur_loc[1]
			cur_loc = check_move_in_limit(move_location, cur_loc)
		elif cursor_direction == q:
			break

		stdscr.refresh()









def create_board():
	board = chess_board_test.Board()
	board.initialize_both_teams()
	board.set_open_closed_spaces()
	board.increment_turn()
	return board

board_one = create_board()
board_two = create_board()



class ChessBoardComponent():
	def __init__(self,board,x,y):
		self.x = x
		self.y = y
		self.board = board
		row_count = 17
		col_count = 49
		self.window = curses.newwin(row_count,col_count,self.y,self.x)
		self.window.keypad(1)

	def refresh(self):
		display_board_curses(self.board, self.window)
		self.window.refresh()

	def move_cb_cursor(self):
		origin = [1,7]
		def check_move_in_limit(move_location, old_cur_loc):
			y_limit = list(range(origin[0],origin[0]+15))
			x_limit = list(range(origin[1],origin[1]+36))

			if move_location[0] in y_limit and move_location[1] in x_limit:
				
				cur_loc = (move_location[0],move_location[1])		
				#display_current_loc(stdscr, cur_loc, origin)
				self.window.move(move_location[0], move_location[1])

				return (move_location[0], move_location[1])

			else:
				return old_cur_loc

		left = 260
		right = 261
		up = 259
		down = 258
		q = 113

		self.window.move(origin[0], origin[1])
		#self.window.move(0, 0)
		self.window.refresh()
		cur_loc = [origin[0],origin[1]]
		cursor_direction = 0

		
		move_location = [0, 0]

		while cursor_direction != 113:
			cursor_direction = self.window.getch()


			if cursor_direction == left:
				move_location[0] = cur_loc[0]
				move_location[1] = cur_loc[1] - 5
				cur_loc = check_move_in_limit(move_location, cur_loc)
			elif cursor_direction == right:
				move_location[0] = cur_loc[0]
				move_location[1] = cur_loc[1] + 5
				cur_loc = check_move_in_limit(move_location, cur_loc)
			elif cursor_direction == up:
				move_location[0] = cur_loc[0] - 2
				move_location[1] = cur_loc[1]
				cur_loc = check_move_in_limit(move_location, cur_loc)
			elif cursor_direction == down:
				move_location[0] = cur_loc[0] + 2
				move_location[1] = cur_loc[1]
				cur_loc = check_move_in_limit(move_location, cur_loc)
			elif cursor_direction == q:
				break

			self.window.refresh()






def draw_screen(stdscr):

	stdscr.keypad(1)
	stdscr.clear()

	stdscr.border()
	stdscr.addstr(1,2,"F8(Game_Menu)")
	stdscr.refresh()

	chess_board_comp = ChessBoardComponent(board_one,10,10)
	chess_board_comp.refresh()
	chess_board_comp_two = ChessBoardComponent(board_two,50,50)
	chess_board_comp_two.refresh()
	chess_board_comp.move_cb_cursor()
	chess_board_comp_two.move_cb_cursor()
	#stdscr.getch()

	# cb_y_pos = 10
	# cb_x_pos = 44
	# cb_col_num = 17
	# cb_row_num = 49
	# chess_board_win = curses.newwin(cb_col_num,cb_row_num,cb_y_pos,cb_x_pos)
	# display_board_curses(board, chess_board_win)

	# chess_board_win.refresh()
	
	#move_cb_cursor(stdscr,cb_y_pos,cb_x_pos)

curses.wrapper(draw_screen)