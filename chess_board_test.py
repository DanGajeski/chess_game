#goto L288
#goto L116

# 0 Based Indexing EVERYWHEREWEEREWREWRWERWEREWR you've got this even when you think you don't.  
# DDont believee the liES in your MiNd
from __future__ import annotations
from chess_pieces import Pawn, Knight, Rook, Bishop, Queen, King
import utils as u
import curses

class Board():

	def __init__(self):
		#self.y_rows = 8
		#self.x_cols = 8
		self.y_rows = 8
		self.x_cols = 8
		self.blue_turn = 0
		self.red_turn = 1
		self.current_player = ''

		###
		# self.blue_pawns = []
		# self.blue_rooks = []
		# self.blue_knights = []
		# self.blue_bishops = []
		# self.blue_queen = []
		# self.blue_king = []
		###
		# self.red_pawns = []
		# self.red_rooks = []
		# self.red_knights = []
		# self.red_bishops = []
		# self.red_queen = []
		# self.red_king = []
		###
		self.living_list = []
		self.dead_list_blue = []#move dead pieces here?
		self.dead_list_red = []
		self.dead_index = 0

		self.en_pessant = False
		self.en_pessant_coords = []#location of en_pessant piece
		self.check_mate_moves = []
		
		self.turns = [[]]#each turn saved in a list within self.turns? 

		self.potential_spaces = []  #set_potential_spaces to fill with u.Space objects

		def set_potential_spaces():
			for y in range(0, 8):
				for x in range(0, 8):
					self.potential_spaces.append(u.Space(u.Vec2(x, y)))

		set_potential_spaces()

	def set_open_closed_spaces(self) -> None:#used after every movement to update piece location on board
		for space in self.potential_spaces:
			space.closed_this_turn = False
		for space in self.potential_spaces:
			for piece in self.living_list:
				if piece.vec == space.vec:
					space.set_space_closed(piece.__class__.__name__, piece.team)
					space.closed_this_turn = True
		for space in self.potential_spaces:
			if space.closed_this_turn == False:
				space.set_space_open()

	def print_spaces_for_test(self) -> None:#TESTING_METHOD
		for space in self.potential_spaces:
			print(space)
	def print_dead_for_test(self) -> None:#TESTING_METHOD
		for dead_piece in self.dead_list:
			print(dead_piece)
	def list_active_pieces(self) -> None:#TESTING_METHOD
		for index, piece in enumerate(self.living_list):
			print("{}: {}".format(index, piece))

	def select_piece_determine_movements(self, piece_index) -> None:#determines all possible moves for selected Piece
		if self.en_pessant == True and self.living_list[piece_index].type == 'P' and abs(self.living_list[piece_index].vec.x - self.en_pessant_coords[0]) == 1 and self.living_list[piece_index].vec.y == self.en_pessant_coords[1]: #y value abs ADD
			self.living_list[piece_index].determine_possible_moves(self.potential_spaces)
			if self.living_list[piece_index].team == 'blue':
				self.living_list[piece_index].add_en_pessant_move(self.en_pessant_coords[0], (self.en_pessant_coords[1]+1))
			else:
				self.living_list[piece_index].add_en_pessant_move(self.en_pessant_coords[0], (self.en_pessant_coords[1]-1))
		else:
			self.living_list[piece_index].determine_possible_moves(self.potential_spaces)

	def reset_en_pessant(self) -> None:#resets en_pessant board attributes for tracking  en_pessant movements
		self.en_pessant = False
		self.en_pessant_coords = []

	def increment_turn(self) -> None:
		if self.blue_turn == 1:
			self.blue_turn = 0
			self.red_turn = 1
			self.current_player = 'red'
		else:
			self.blue_turn = 1
			self.red_turn = 0
			self.current_player = 'blue'

	#UPDATE_REQUEST - update method to select piece via coords instead of list index
	#def move_piece(self, selected_piece:int, x:int, y:int) -> None:#strong method used for moving a Piece AFTER Piece movements determined by [Board.select_piece_determine_movements() method]
	def move_piece(self, selected_piece:str) -> None:#strong method used for moving a Piece AFTER Piece movements determined by [Board.select_piece_determine_movements() method]	
		x = 0
		y = 0
		possible_characters = 'abcdefgh'
		active_piece = input("Please select destination to move to: (ex: 'd5')")

		x = possible_characters.find(active_piece[0])
		y = 8 - int(active_piece[1])


		

		#NEW_UPDATE_REQUEST - user input includes dipslaying information so such a function should remain separate.  
		#NEW_FUNCTION - Display Methods to acquire information to then call methods such as Board.change_piece to manipulate acquired data
		# def change_piece_input(self): -> None:
		# 	change_piece_input = ''
		# 	proper_change_piece_inputs = ['q', 'n', 'b', 'r']
		# 	while change_piece_input not in proper_change_piece_inputs:
		# 		try:
		# 			if change_piece_input
		# 			change_piece_input = input("Please select what to change your Pawn into: ")
			###!!!A start to an idea....!!!###

		#UPDATE_REQUEST_01(on_hold) - update to include user input selecting which Piece to morph into
		def change_piece(updated_piece_type:str) -> None:#morphs Pawn Piece into a new Piece(Q,N,B,R)
			x = self.living_list[selected_piece].vec.x 
			y = self.living_list[selected_piece].vec.y
			team = self.living_list[selected_piece].team
			if updated_piece_type == 'q':
				self.living_list.append(Queen(u.Vec2(x, y), team))
			elif updated_piece_type == 'n':
				self.living_list.append(Knight(u.Vec2(x, y), team))
			elif updated_piece_type == 'b':
				self.living_list.append(Bishop(u.Vec2(x, y), team))
			elif updated_piece_type == 'r':
				self.living_list.append(Rook(u.Vec2(x, y), team))
			del self.living_list[selected_piece]

		#WILL CHANGE FOR USER INPUT#
		def check_pawn_promotion() -> None:#cond for Pawn Piece change [Board.change_piece() method]
			if self.living_list[selected_piece].type == 'P':
				if self.living_list[selected_piece].team == 'blue':
					if self.living_list[selected_piece].vec.y == 7:
						change_piece('q')#CHANGE_01
				else:
					if self.living_list[selected_piece].vec.y == 0:
						change_piece('q')#CHANGE_01

		def just_move(x:int, y:int) -> None:#move Piece to new location
			self.living_list[selected_piece].vec.x = x  
			self.living_list[selected_piece].vec.y = y 

		def kill_and_move(index:int, x:int, y:int) -> None:#move Piece to target location and delete occupying Piece in target location / moves deleted Piece into respective color dead_list
			if self.living_list[index].team == 'blue':
				self.dead_list_blue.append(self.living_list[index])
				self.living_list[index].vec.x = self.dead_index - 1
				self.living_list[index].vec.y = self.dead_index - 1
				self.dead_index -= 1
				just_move(x, y)
				del self.living_list[index]
			elif self.living_list[index].team == 'red':
				self.dead_list_red.append(self.living_list[index])
				self.living_list[index].vec.x = self.dead_index - 1
				self.living_list[index].vec.y = self.dead_index - 1
				self.dead_index -= 1
				just_move(x, y)
				del self.living_list[index]

		piece_attacked = False #cond bool for Piece being directly replaced with opposite color Piece

		#checks selected_piece Piece against every active Piece in self.living_list, IF another Piece already in location, 'kill' it from self.living_list and move active Piece into dead Piece's xy coords 
		for index, piece in enumerate(self.living_list):
			if self.living_list[index].vec.x == x and self.living_list[index].vec.y == y:
				kill_and_move(index, x, y)
				self.increment_turn()
				piece_attacked = True
				check_pawn_promotion()
				self.reset_en_pessant()
				break

		if piece_attacked == False:#Piece yet unmoved due to no Pieces to kill at destination(will be moved in subsequent code)
			if self.living_list[selected_piece].type == 'P': 

				#Pawn Piece moving 2 spaces from origin enabling EN_PESSANT opportunity for next player's turn.
				if abs(self.living_list[selected_piece].vec.y - y) == 2 and self.living_list[selected_piece].vec.x == x:
					self.en_pessant = True
					self.en_pessant_coords = [x,y]
					just_move(x, y)
					self.increment_turn()

				#Selected Pawn Piece engaging in an EN_PESSANT_ATTACK
				elif u.Vec2(x, y) == self.living_list[selected_piece].en_pessant_move: #pawn en_pessant attack move
					for index, piece in enumerate(self.living_list):
						if self.living_list[selected_piece].team == 'blue':
							if u.Vec2(x, y-1) == piece.vec:
								kill_and_move(index, x, y)
								self.increment_turn()
								self.reset_en_pessant()
								break
						else:#'red'
							if u.Vec2(x, y+1) == piece.vec:
								kill_and_move(index, x, y)
								self.increment_turn()
								self.reset_en_pessant()
								break
				
				else:#Pawn Piece moving to EMPTY location
					just_move(x, y)
					self.increment_turn()
					self.reset_en_pessant()
					check_pawn_promotion()
	
			else:#NON-Pawn Piece moving to EMPTY location
				just_move(x, y)
				increment_turn()
				self.reset_en_pessant()

	#NEEDS_TESTING + INTEGRATION
	def check_for_check_mate(self, team:str):#team = 'blue': checks for red team possible moves
		self.check_mate_moves = []
		for piece in self.living_list:
			if piece.team != team:
				piece.determine_possible_moves()
				self.check_mate_moves.append(piece.possible_moves_enemy)
		for move in self.check_mate_moves:
			for piece in self.living_list:
				if piece.team == team and piece.type == 'K':
					if move == piece.vec:
						print('The king is under threat!  You must move your king or the end is near!')
						break

	def initialize_both_teams(self) -> None:#Initializes both 'red' and 'blue' teams according to their respective starting Vec2 coords
		for n in range(0,8):
			self.living_list.append(Pawn(u.Vec2(n,1),"blue"))
		self.living_list.append(Knight(u.Vec2(1,0),"blue"))
		self.living_list.append(Knight(u.Vec2(6,0),"blue"))
		self.living_list.append(Rook(u.Vec2(0,0),"blue"))
		self.living_list.append(Rook(u.Vec2(7,0),"blue"))
		self.living_list.append(Bishop(u.Vec2(2,0),"blue"))
		self.living_list.append(Bishop(u.Vec2(5,0),"blue"))
		self.living_list.append(Queen(u.Vec2(3,0),"blue"))
		self.living_list.append(King(u.Vec2(4,0),"blue"))

		for n in range(0,8):
			self.living_list.append(Pawn(u.Vec2(n,6),"red"))
		self.living_list.append(Knight(u.Vec2(1,7),"red"))
		self.living_list.append(Knight(u.Vec2(6,7),"red"))
		self.living_list.append(Rook(u.Vec2(0,7),"red"))
		self.living_list.append(Rook(u.Vec2(7,7),"red"))
		self.living_list.append(Bishop(u.Vec2(2,7),"red"))
		self.living_list.append(Bishop(u.Vec2(5,7),"red"))
		self.living_list.append(Queen(u.Vec2(3,7),"red"))
		self.living_list.append(King(u.Vec2(4,7),"red"))
	
	#you are worth something real.

	###XXXDISPLAY METHODSXXX###

	def select_piece_display_movements(self, piece_index:int) -> None:#displays to user the selected Piece's possible movements as Vec2 coords
		self.living_list[piece_index].display_moves()


	def display_board_curses(self, stdscr):
		def determine_displayed_symbol(x:int, y:int) -> str:
			unformatted_symbol = " "
			for piece in self.living_list:
				if x == piece.vec.x and y == piece.vec.y:
					unformatted_symbol = piece.type
					break
			return "_(%s)_" % unformatted_symbol

		y_index = 0
		x_index = 0
		y_reference_num = 8
		x_reference_spaced_chars = "      A    B    C    D    E    F    G    H"
		stdscr.addstr(y_index, x_index, x_reference_spaced_chars)
		for y in range(self.y_rows):#prints entire board and assigned symbols
			stdscr.addstr(y_index, x_index, y_reference_num)
			#print(y_reference_num, end='')
			stdscr.addstr(y_index, (x_index + 1), "||_")
			#print("||_", end='')
			x_sub_index = 4
			for x in range(self.x_cols):
				stdscr.addstr(y_index, x_sub_index, determine_displayed_symbol(x, y))
				x_sub_index += 5 
				#print(determine_displayed_symbol(x, y), end='')
			stdscr.addstr(y_index, (x_sub_index + 5), "_||")
			x_sub_index += 5
			#print("_||", end='')
			stdscr.addstr(y_index, (x_sub_index + 3), y_reference_num)
			print(y_reference_num, end='')
			y_reference_num -= 1
			y_index += 1
			# if y != self.y_rows - 1:	
			# 	print("\n")
			# else:
			# 	print("\n", end='')
		stdscr.addstr(y_index, x_index, x_reference_spaced_chars)
		#print(x_reference_spaced_chars)


	def display_board(self):#determines which self.living_list[] Piece symbols to print and where, then prints entire board to user screen

		def determine_displayed_symbol(x:int, y:int) -> str:#determines symbol to print according to self.living_list[] object Vec2s
			unformatted_symbol = " "
			for piece in self.living_list:
				if x == piece.vec.x and y == piece.vec.y:
					unformatted_symbol = piece.type
					break
			return "_(%s)_" % unformatted_symbol

		y_reference_num = 8
		x_reference_spaced_chars = "      A    B    C    D    E    F    G    H"
		print(x_reference_spaced_chars)
		for y in range(self.y_rows):#prints entire board and assigned symbols
			print(y_reference_num, end='')
			print("||_", end='')
			for x in range(self.x_cols):
				print(determine_displayed_symbol(x, y), end='')
			print("_||", end='')
			print(y_reference_num, end='')
			y_reference_num -= 1
			if y != self.y_rows - 1:
				print("\n")
			else:
				print("\n", end='')
		print(x_reference_spaced_chars)

	def player_select_piece(self) -> int:#prompts player for Piece selection via char and int, translates input into and returns self.living_list[] index of selected Piece.
		active_piece_x = 0
		active_piece_y = 0
		active_piece_living_list_index = 0
		possible_characters = 'abcdefgh'
		active_color_piece_in_living_list = False

		#COMEBACK HERE.   UPDATE THIS CONDITIONAL TO self.current_player........
		active_piece = input("{} player, please select a Piece to move: (ex: 'd5')".format(self.current_player.title()))

		# if self.blue_turn == 1:
		# 	active_piece = input("Blue player, please select a Piece to move: (ex: 'd5')")
		# else:
		# 	active_piece = input("Red player, please select a Piece to move: (ex: 'd5')")
		while active_color_piece_in_living_list == False:

			if active_piece == 'q':
				return active_piece

			active_piece_x = possible_characters.find(active_piece[0])
			active_piece_y = 8 - int(active_piece[1])
			found_match = False

			for index, piece in enumerate(self.living_list):
				legal_blue_move = self.blue_turn == 1 and piece.team == 'blue' #bool expression assigned to variable
				legal_red_move = self.red_turn == 1 and piece.team == 'red'
				if (legal_blue_move or legal_red_move) and piece.vec.x == active_piece_x and piece.vec.y == active_piece_y:
					active_color_piece_in_living_list = True
					found_match = True
					active_piece_living_list_index = index 
					break
				# elif self.red_turn == 1 and piece.team == 'red' and piece.vec.x == active_piece_x and piece.vec.y == active_piece_y:
				# 	active_color_piece_in_living_list = True
				# 	found_match = True 
				# 	active_piece_living_list_index = index 
				# 	break
	
			#players = ['blue', 'red']



			if found_match == False:
				active_piece = input("That piece either doesn't exist or isn't on your team.  {} player, please select a Piece to move: (ex: 'd5')".format(self.current_player))


			

			# elif found_match == False and self.red_turn == 1:
			# 	active_piece = input("That piece either doesn't exist or isn't on your team.  {}, please select a Piece to move: (ex: 'd5')", {self.current_player})

		return active_piece_living_list_index