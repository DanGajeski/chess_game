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


def draw_screen(stdscr):

	# curses.echo()
	# stdscr.getstr(0,0,8)
	# curses.noecho()

	stdscr.clear()
	#stdscr.border()

	new_board.display_board_curses(stdscr)



	#stdscr.resize(50,100)
	stdscr.border()
	stdscr.refresh()

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
	stdscr.getch()
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









