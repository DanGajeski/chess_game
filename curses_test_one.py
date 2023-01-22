#from __future__ import 
import __future__
import curses
import chess_board_test
from curses.textpad import Textbox, rectangle


# from curses import wrapper

# def main(stdscr):
# 	#Clear screen
# 	stdscr.clear()

# 	#This raises ZeroDivisionError when i == 10
# 	for i in range(0, 11):
# 		v = i-10
# 		stdscr.addstr(i, 0, '10 divided by {} is {}'.format(v, 10/v))

# 	stdscr.refresh()
# 	stdscr.getkey()   

# wrapper(main)

# def main(stdscr):
# 	stdscr.addstr(0, 0, "Enter IM message: (hit Ctrl-G to send)")

# 	editwin = curses.newwin(5,30, 2,1)
# 	rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
# 	stdscr.refresh()

# 	box = Textbox(editwin)

# 	box.edit()

# 	message = box.gather()

# screen = curses.initscr()
# curses.noecho()
# curses.cbreak()
# screen.keypad(True)

# #curses.curs_set(1)
# screen.addstr(0,0,'fuckyeah')
# curses.curs_set(0)
# screen.refresh()
# screen.getch()

# curses.nocbreak()
# screen.keypad(False)
# curses.echo()
# curses.endwin()

new_board = chess_board_test.Board()
new_board.initialize_both_teams()
new_board.set_open_closed_spaces()
new_board.increment_turn()

#THEY ARE LIES.  DON'T LISTEN.   

def display_current_loc(stdscr, cur_loc):
		x_dict = {8: 'A',
				  13: 'B',
				  18: 'C',
				  23: 'D',
				  28: 'E',
				  33: 'F',
				  38: 'G',
				  43: 'H',
				 }
		y_dict = {5: 8,
				  7: 7,
				  9: 6,
				  11: 5,
				  13: 4,
				  15: 3,
				  17: 2,
				  19: 1,
				 }

		#curses.init_pair(1,1,7)#blue_WHITE
		#curses.init_pair(2,4,7)#red_WHITE
		#curses.init_pair(3,1,0)#blue_BLACK
		#curses.init_pair(4,4,0)#red_BLACK
		stdscr.addstr(22,2,"({},{})".format(cur_loc[0], cur_loc[1]))
		print_string = '({}, {})'.format(y_dict[cur_loc[0]], x_dict[cur_loc[1]])
		stdscr.addstr(21,2,"CursorLoc: {}".format(print_string))

# while cursor_direction != 113:#113ASCIIq
		
# 		cursor_direction = stdscr.getch()
# 		stdscr.addstr(1,1,str(cursor_direction))
		
# 		if cursor_direction == left:
# 			stdscr.move(cur_loc[0], (cur_loc[1] - 5))
# 		elif cursor_direction == right:
# 			stdscr.move(cur_loc[0], (cur_loc[1] + 5))
# 		elif cursor_direction == up:
# 			stdscr.move((cur_loc[0] - 2), cur_loc[1])
# 		elif cursor_direction == down:
# 			stdscr.move((cur_loc[0] + 2), cur_loc[1])
# 		if cursor_direction == 113:
# 			break

def move_cursor(stdscr):
	def check_move_in_limit(move_location, old_cur_loc):
		y_limit = list(range(5,20))
		x_limit = list(range(8,44))

		if move_location[0] in y_limit and move_location[1] in x_limit:
		
			stdscr.move(move_location[0], move_location[1])
			stdscr.refresh()
			cur_loc = curses.getsyx()
			display_current_loc(stdscr, cur_loc)
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
	stdscr.move(5, 8)
	stdscr.refresh()
	#chess_board_pad.refresh(0,0,4,1,19,50)
	cur_loc = curses.getsyx()#(y,x)tuple returned
	#cur_loc = list(cur_loc_tuple)
	#cur_loc = cur_loc_tuple[0] - 4
	#cur_loc.append(cur_loc_tuple[1] - 1)
	#cur_loc[0] -= 4
	#cur_loc[1] -= 1
	cursor_direction = 0

	
	move_location = [0, 0]

	while cursor_direction != 113:
		#stdscr.addstr(2,2,str(cursor_direction))
		#stdscr.refresh()
		cursor_direction = stdscr.getch()


		if cursor_direction == left:
			move_location[0] = cur_loc[0]
			move_location[1] = cur_loc[1] - 5
			cur_loc = check_move_in_limit(move_location, cur_loc)
			# stdscr.move(cur_loc[0], (cur_loc[1] - 5))
		elif cursor_direction == right:
			move_location[0] = cur_loc[0]
			move_location[1] = cur_loc[1] + 5
			cur_loc = check_move_in_limit(move_location, cur_loc)
			# stdscr.move(cur_loc[0], (cur_loc[1] + 5))
		elif cursor_direction == up:
			move_location[0] = cur_loc[0] - 2
			move_location[1] = cur_loc[1]
			cur_loc = check_move_in_limit(move_location, cur_loc)
			# stdscr.move((cur_loc[0] - 2), cur_loc[1])
		elif cursor_direction == down:
			move_location[0] = cur_loc[0] + 2
			move_location[1] = cur_loc[1]
			cur_loc = check_move_in_limit(move_location, cur_loc)
			# stdscr.move((cur_loc[0] + 2), cur_loc[1])
		elif cursor_direction == q:
			break
			#UPDATELATER

		stdscr.refresh()
		#chess_board_pad.refresh(0,0,4,1,19,50)

		#stdscr.addstr(2,2,str(move_location[0]))
		#stdscr.addstr(3,2,str(move_location[1]))
	


	# stdscr.refresh()
	# cur_loc = curses.getsyx()
	# 	#stdscr.addstr(2,2,str(cur_loc))
	# display_current_loc(stdscr, cur_loc)
	# #stdscr.move(cur_loc[0], cur_loc[1])
	# stdscr.refresh()


#def game_menu(stdscr):


def draw_screen(stdscr):

	# curses.echo()
	# stdscr.getstr(0,0,8)
	# curses.noecho()

	stdscr.keypad(1)
	stdscr.clear()
	#stdscr.border()

	stdscr.addstr(1,2,"F8(Game_Menu)")

	chess_board_pad = curses.newpad(17,49)
	new_board.display_board_curses(chess_board_pad)


	#new_board.display_board_curses(stdscr)



	#stdscr.resize(50,100)
	stdscr.border()
	stdscr.refresh()
	chess_board_pad.refresh(0,0,4,1,20,50)
	move_cursor(stdscr)

	# curses.mousemask(1)

	# while True:
	# 	event = stdscr.getch()
	# 	if event == ord("q"):
	# 		break
	# 	if event == curses.KEY_MOUSE:
	# 		stdscr.addstr(20,0,"youclickedbud")
	# 		_, mx, my, _, _ = curses.getmouse()
	# 		y, x = stdscr.getyx()
	# 		stdscr.addstr(20,0,"hello")
	# 		stdscr.refresh()
	#stdscr.addstr(20,0,"hello")
	#stdscr.getch()

	# pad_one = curses.newpad(30,30)
	# pad_one.border()
	# xcoord = 0 
	# x = 0
	
	# testy=0
	# for n in range(10):
	
	# 	testx = 0
	# 	#y=0
	# 	for b in range(10):
	# 		pad_one.addstr(testy,testx,'x')
	# 		testx+=1
	# 	testy+=1


	#pad_one.addstr(0,0,'x')
	# x = 0
	# y = 0
	# for n in range(10):
	# 	for n in range(20):
	# 		pad_one.addstr(y,x, 'X')
	# 		y += 1	
	# 	x += 1



	#pad_one.bkgdset(' ', curses.COLOR_RED)

	#stdscr.clear()
	#stdscr.refresh()
	
	# curses.init_pair(1,curses.COLOR_RED, curses.COLOR_BLACK)
	# stdscr.addstr(10,10, str(curses.LINES), curses.color_pair(1) | curses.A_BLINK | curses.A_BOLD)
	# curses.curs_set(0)

	

	# stdscr.refresh()
	# curses.napms(1000)
	# pad_one.refresh(0,0, 0,0, 30,30)
	

	
	####TEMPCOMMENTEDOUT###
	
	# left = 260
	# right = 261
	# up = 259
	# down = 258
	# stdscr.move(2, 7)
	# stdscr.refresh()	
	# cur_loc = curses.getsyx()#(y,x)tuple returned
	# cursor_direction = 0


	#window.move(new_y,new_x)
	# while cursor_direction != 113:#113ASCIIq
		
		
	# 	cursor_direction = stdscr.getch()
	# 	stdscr.addstr(1,1,str(cursor_direction))
		
	# 	if cursor_direction == left:
	# 		stdscr.move(cur_loc[0], (cur_loc[1] - 5))
	# 	elif cursor_direction == right:
	# 		stdscr.move(cur_loc[0], (cur_loc[1] + 5))
	# 	elif cursor_direction == up:
	# 		stdscr.move((cur_loc[0] - 2), cur_loc[1])
	# 	elif cursor_direction == down:
	# 		stdscr.move((cur_loc[0] + 2), cur_loc[1])
	# 	if cursor_direction == 113:
	# 		break

	# 	#stdscr.refresh()
		
		
	# 	stdscr.refresh()
	# 	cur_loc = curses.getsyx()
	# 	#stdscr.addstr(2,2,str(cur_loc))
	# 	display_current_loc(stdscr, cur_loc)
	# 	stdscr.move(cur_loc[0], cur_loc[1])
	# 	stdscr.refresh()

	####TEMPCOMMENTEDOUT###






		#cur_loc = curses.getsyx()
		#return cursor_direction

		#cur_loc passed in as (y,x)
	


		#A:7
		#B:12
		#C:17
		#D:22
		#E:27
		#F:32
		#G:37
		#H:42

		#8:2
		#7:4
		#6:6
		#5:8
		#4:10
		#3:12
		#2:14
		#1:16



		#UR(2,37)
		#UL
		# L -> 260
		# R -> 261
		# U -> 259
		# D -> 258



	# curses.curs_set(2)

curses.wrapper(draw_screen)

# def main(stdscr):
# 	stdscr.addstr(0,0,"Enter IM Message: (hit Ctrl-G to send)")

# 	editwin = curses.newwin(5,30, 2,1)
# 	rectangle(stdscr, 1,0, 1+5+1, 1+30+1)
# 	stdscr.refresh()

# 	box = Textbox(editwin)

# 	box.edit()

# 	message = box.gather()

# curses.wrapper(main)









