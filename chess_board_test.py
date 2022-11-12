# 0 Based Indexing EVERYWHEREWEEREWREWRWERWEREWR
# DDont believee the liES in your MiNd
from __future__ import annotations
from chess_pieces import Pawn, Knight, Rook, Bishop, Queen, King
import utils as u

class Board():

	def __init__(self):
		self.rows = 8
		self.cols = 8
		
		###
		self.blue_pawns = []
		self.blue_rooks = []
		self.blue_knights = []
		self.blue_bishops = []
		self.blue_queen = []
		self.blue_king = []
		###
		self.red_pawns = []
		self.red_rooks = []
		self.red_knights = []
		self.red_bishops = []
		self.red_queen = []
		self.red_king = []
		###
		self.living_list = []

		self.potential_spaces = []  #set_potential_spaces to fill with u.Space objects

		def set_potential_spaces():
			for x in range(0, 8):
				for y in range(0, 8):
					self.potential_spaces.append(u.Space(u.Vec2(x, y)))

		set_potential_spaces()
		
		# self.potential_spaces = [(0, 0), (0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7),
		# 						 (1, 0), (1, 1), (1, 2), (1, 3), (1, 4), (1, 5), (1, 6), (1, 7),
		# 						 (2, 0), (2, 1), (2, 2), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7),
		# 						 (3, 0), (3, 1), (3, 2), (3, 3), (3, 4), (3, 5), (3, 6), (3, 7),
		# 						 (4, 0), (4, 1), (4, 2), (4, 3), (4, 4), (4, 5), (4, 6), (4, 7),
		# 						 (5, 0), (5, 1), (5, 2), (5, 3), (5, 4), (5, 5), (5, 6), (5, 7),
		# 						 (6, 0), (6, 1), (6, 2), (6, 3), (6, 4), (6, 5), (6, 6), (6, 7),
		# 						 (7, 0), (7, 1), (7, 2), (7, 3), (7, 4), (7, 5), (7, 6), (7, 7),
		# 						 ]

		# only to set method to check if a space is possible to move to.
		#self.open_spaces = []
		### method to ping Piece objects and determine self.open_spaces
		#	for knight in self.red_knights:
		#		knight_loc = [knight.row, knight.col]
		#		if knight_loc in self.open_spaces:
		#			knight_loc_index = self.open_spaces.index(knight_loc)
		#			self.closed_spaces.append(self.open_spaces[knight_loc_index])
		#			del self.open_spaces[knight_loc_index]


		### method to set_open_spaces, method to check_open_space

		#self.closed_spaces = [] #[[0, 3], self.blue_pawns[3].id]
		### method to ping Piece objects and determine self.closed_spaces
		
		#self.current_locations = []
		#self.zero_range = [1, 9, 17, 25, 33, 41, 49, 57]
		#self.end_range = [9, 16, 24, 32, 40, 48, 56, 64]

	def set_open_closed_spaces(self):
		for space in self.potential_spaces:
			for piece in self.living_list:
				if piece.cur_space == space.xy:
					space.set_space_closed(piece.__class__.__name__, piece.team)


	#checked possible moves
	# current move verified, space verified to be currently closed

	# previous claimed space made empty

	# piece in destination space deleted
	# selected piece location chagned to destination space
	#def move_to_closed_space(self):

		# Check state / board parameters then check piece paremeters. 

	# previous claimed space made empty

	# selected piece location changed to destination space
	#def move_to_open_space(self):

	###XXXMOVEMENTMETHODSXXX###

	###PAWNMOVEMENTS###
	

	###ROOKMOVEMENTS###
	###KNIGHTMOVEMENTS###
	###BISHOPMOVEMENTS###
	###QUEENMOVEMENTS###
	###KINGMOVEMENTS###


	###XXXDISPLAY METHODSXXX###

	def print_chessboard_rows_lmr(self, fuck, c, r):

		def will_this_fuckin_work(c, r):
			
			symbol = " "
			for d in range(len(self.living_list)):
				if c == self.living_list[d].col and r == self.living_list[d].row:
					symbol = self.living_list[d].type
			return symbol

		if fuck == 'l':
			
			symbol = will_this_fuckin_work(c, r)
			print("||__(%s)_" % symbol, end='')

		elif fuck == 'r':
			
			symbol = will_this_fuckin_work(c, r)
			print("_(%s)__||" % symbol, end='')		

		elif fuck == 'm':
			
			symbol = will_this_fuckin_work(c, r)	
			print("_(%s)_" % symbol, end='')

	def display_board(self):
		
		for r in range(self.rows):
			#print("ROW: %d ||" % r, end='')
			for c in range(self.cols):
				if c == 0:
					self.print_chessboard_rows_lmr('l', c, r)
				
				elif c == self.cols - 1:
					self.print_chessboard_rows_lmr('r', c, r)	

				else:
					self.print_chessboard_rows_lmr('m', c, r)

			print("\n")

	###XXXINITIALIZEREDANDBLUETEAMS_ADDTOself.livinglistXXX###

	def initialize_both_teams(self):
		
		def initialize_blue_team():

			def initialize_blue_pawns():
				for n in range(0,8):
					self.blue_pawns.append(Pawn(n, 1, "blue"))
					#self.blue_pawns[n].set_location().shit_my_pants() Method chaining - .set_location() would have to return self

			def initialize_blue_knights():
				#self.blue_knights.append(Knight(1, 2))
				#self.blue_knights.append(Knight(1, 7))
				self.blue_knights = [Knight(1, 0, "blue"), Knight(6, 0, "blue")]

			def initialize_blue_rooks():
				self.blue_rooks = [Rook(0, 0, "blue"), Rook(7, 0, "blue")]

			def initialize_blue_bishops():
				self.blue_bishops = [Bishop(2, 0, "blue"), Bishop(5, 0, "blue")]

			def initialize_blue_queen():
				self.blue_queen = [Queen(3, 0, "blue")]

			def initialize_blue_king():
				self.blue_king = [King(4, 0, "blue")]

			initialize_blue_pawns()
			initialize_blue_knights()
			initialize_blue_rooks()
			initialize_blue_bishops()
			initialize_blue_queen()
			initialize_blue_king()

		def initialize_red_team():

			def initialize_red_pawns():
				for n in range(0,8):
					self.red_pawns.append(Pawn(n, 6, "red"))
					
			def initialize_red_knights():
				self.red_knights = [Knight(1, 7, "red"), Knight(6, 7, "red")]

			def initialize_red_rooks():
				self.red_rooks = [Rook(0, 7, "red"), Rook(7, 7, "red")]

			def initialize_red_bishops():
				self.red_bishops = [Bishop(2, 7, "red"), Bishop(5, 7, "red")]

			def initialize_red_queen():
				self.red_queen = [Queen(4, 7, "red")]

			def initialize_red_king():
				self.red_king = [King(3, 7, "red")]

			initialize_red_pawns()
			initialize_red_knights()
			initialize_red_rooks()
			initialize_red_bishops()
			initialize_red_queen()
			initialize_red_king()

		def collect_them_all():

			def collector(collect_from):
				for n in range(len(collect_from)):
					self.living_list.append(collect_from[n])

			#for n in self.blue_team:


			collector(self.blue_pawns)
			collector(self.blue_knights)
			collector(self.blue_rooks)
			collector(self.blue_bishops)
			collector(self.blue_queen)
			collector(self.blue_king)

			collector(self.red_pawns)
			collector(self.red_knights)
			collector(self.red_rooks)
			collector(self.red_bishops)
			collector(self.red_queen)
			collector(self.red_king)

		initialize_blue_team()
		initialize_red_team()
		collect_them_all()

		# moves piece from (c,r) to (nc, nr) and if (nc, nr) already occup. deletes occupying piece
	def move_piece_test(self, c, r, nc, nr):
		piece_del_index = -1
		for test_piece in range(len(self.living_list)):
			if self.living_list[test_piece].col == c and self.living_list[test_piece].row == r:

				for test_piece_two in range(len(self.living_list)):

					if self.living_list[test_piece_two].col == nc and self.living_list[test_piece_two].row == nr:

						piece_del_index = test_piece_two 

				self.living_list[test_piece].col = nc 
				self.living_list[test_piece].row = nr

		if piece_del_index >= 0:
			del self.living_list[piece_del_index]

	# def piece_movement_logic

	# what kind of piece are we using
	# piece.__class__.__name__ to get type
	# if rook:
	# 	we check each list, in order, FOR: potential_spaces 
	# 									   open_spaces optional_space 
	# 									   if closed_spaces:  (do not check any further)
	# 									     Ally: non_optional_space
	# 									     enemy: optional_space(set to optional_space and attack_space lists) (claim space, del enemy from show list)  



























	###PAWNTURNINCREMENTFUNCS((()))

	# def increment_ll_red_pawns_turn(self):
	# 	for wk_piece in self.living_list:
	# 		if wk_piece.team == "red" and wk_piece.type == 'P':
	# 			wk_piece.init_turn += 1

	# def increment_ll_blue_pawns_turn(self):
	# 	for piece in self.living_list:
	# 		if piece.team == "blue" and piece.type == 'P':
	# 			piece.init_turn += 1


#living_list[]

	# SPACES
	#	OPEN SPACE
	#	CLAIMED SPACE
	#		WHO IS CLAIMING SPACE
	
	##	THREATENED SPACES ( OPEN SPACES WHICH ARE IN MOVING DISTANCE OF APPLICABLE PIECES )
			# ping all remaining Piece objects, check for potential moves.   find ALL open spaces
			#	which are potential move locations
				# self.possible_move_locations = [(n,y),]... with a Piece class method to find this. 
					# dont listen to the lies in your head.  you've come this far.  you've worked this hard
					# you can keep going.  you can rest recoup and work harder.  You've got this.  Caps even. 

	# MOVING
	#	WHERE CAN PIECE TYPE MOVE TO
	#		OUT OF POSSIBLE SPACES TO MOVE TO - IS SPACE OPEN OR CLAIMED
	#	IF OPEN
	#		PIECE CLAIMS OPEN SPACE, PREVIOUS CLAIMED SPACE NOW BECOMES OPEN SPACE
	#	IF CLAIMED
	#		PIECE CLAIMS CLAIMED SPACE, PREVIOUS CLAIMED SPACE NOW BECOMES OPEN SPACE
	#		PREVIOUS CLAIMING PIECE GETS DESTROYED, COMPLETELY REMOVED FROM THE BOARD

	# ADV MOVING
	#	ROOK, QUEEN, BISHOP all move in a certain direction

	##	THREATENED SPACES ( OPEN SPACES WHICH ARE IN MOVING DISTANCE OF APPLICABLE PIECES  )
			# ping all remaining Piece objects, check for potential moves.   find ALL open spaces
			#	which are potential move locations




	# def get_map_locations(self):
	# 	for n in self.living_list:
	# 		if n.type == "pawn":
	# 			self.current_locations.append(["p", n.board_location])
			#if n.type == "rook":




	#def set_pawns_locations(self):
	#	for pawn in blue_pawns:
	#		pawn.set_location()


	#def initialize_blue_rooks(self):
	#def initialize_blue_knights(self):
	#def initializa_blue_bishops(self):
	#def initializa_blue_queen(self):
	#def initializa_blue_king(self):

	#def initialize_red_pawns(self):
	#def initialize_red_rooks(self):
	#def initialize_red_knights(self):
	#def initializa_red_bishops(self):
	#def initializa_red_queen(self):
	#def initializa_red_king(self):

#### NEXT STEPS
#Write method for moving when a HOPPER
	#PAWN, KNIGHT, KING
#Write method for moving when a GLIDER
	#QUEEN, BISHOP, ROOK

#CheckforCheckmateCheck....Checkkkkkkyougotthis
#if king possible moves are all in threatened_moves... checkmate!