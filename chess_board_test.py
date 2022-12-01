# 0 Based Indexing EVERYWHEREWEEREWREWRWERWEREWR you've got this even when you think you don't.  
# DDont believee the liES in your MiNd
from __future__ import annotations
from chess_pieces import Pawn, Knight, Rook, Bishop, Queen, King
import utils as u

class Board():

	def __init__(self):
		self.rows = 8
		self.cols = 8
		
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
		self.dead_list =[]#move dead pieces here?
		self.dead_index = 0

		self.en_pessant = False
		self.en_pessant_coords = []#0index=x, 1index=init_y, 2index=final_y
		
		self.turn_zero = []
		self.turn_one = []
		self.turn_two = []#...saving turns in lists? 

		self.potential_spaces = []  #set_potential_spaces to fill with u.Space objects

		def set_potential_spaces():
			for y in range(0, 8):
				for x in range(0, 8):
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
			space.closed_this_turn = False
		for space in self.potential_spaces:
			for piece in self.living_list:
				if piece.vec == space.vec:
					space.set_space_closed(piece.__class__.__name__, piece.team)
					space.closed_this_turn = True
		for space in self.potential_spaces:
			if space.closed_this_turn == False:
				space.set_space_open()

	def print_spaces_for_test(self):
		for space in self.potential_spaces:
			print(space)
	def print_dead_for_test(self):
		for dead_piece in self.dead_list:
			print(dead_piece)



	def list_active_pieces(self) -> None:
		for index, piece in enumerate(self.living_list):
			print("{}: {}".format(index, piece))

	def select_piece_display_movements(self, piece_index) -> None:
		if self.en_pessant == True and self.living_list[piece_index].type == 'P' and abs(self.living_list[piece_index].vec.x - self.en_pessant_coords[0]) == 1:
			self.living_list[piece_index].determine_possible_moves(self.potential_spaces)
			if self.living_list[piece_index].team == 'blue':
				self.living_list[piece_index].add_en_pessant_move(self.en_pessant_coords[0], (self.en_pessant_coords[1]-1))
			else:
				self.living_list[piece_index].add_en_pessant_move(self.en_pessant_coords[0], (self.en_pessant_coords[1]+1))
			self.living_list[piece_index].display_moves()
		else:
			self.living_list[piece_index].determine_possible_moves(self.potential_spaces)
			self.living_list[piece_index].display_moves()
		#if self.en_pessant == True and if self.living_list[piece_index].type == 'P' and if abs(self.living_list[piece_index].x - self.en_pessant[0]) == 1:
		#you are kicking ass.  keep ignoring the lies in your head.  

	def move_piece_test(self, piece_index:int, x:int, y:int) -> None:
		self.en_pessant = False
		self.en_pessant_coords = []
		completed = False
		for index, piece in enumerate(self.living_list):
			if self.living_list[index].vec.x == x and self.living_list[index].vec.y == y:
				self.dead_list.append(self.living_list[index])
				self.living_list[index].vec.x = self.dead_index - 1
				self.living_list[index].vec.y = self.dead_index -1
				self.dead_index -= 1
				# if self.living_list[piece_index].type == 'P':
				# 	if abs(self.living_list[piece_index].vec.y - y) == 2:
				# 		self.en_pessant = True
				# 		self.en_pessant_coords = [self.living_list[piece_index].vec.x, self.living_list[piece_index].vec.y, y]
				self.living_list[piece_index].vec.x = x  
				self.living_list[piece_index].vec.y = y
				del self.living_list[index]
				completed = True
				break
		if completed == False:
			if self.living_list[piece_index].type == 'P':
				if abs(self.living_list[piece_index].vec.y - y) == 2 and self.living_list[piece_index].vec.x == x:
					self.en_pessant = True
					self.en_pessant_coords = [self.living_list[piece_index].vec.x, self.living_list[piece_index].vec.y, y]
					self.living_list[piece_index].vec.x = x 
					self.living_list[piece_index].vec.y = y 
				elif u.Vec2(x, y) == self.living_list[piece_index].en_pessant_move[0]:
					for index, piece in enumerate(self.living_list):
						if self.living_list[piece_index].team == 'blue':
							if u.Vec2(x, y-1) == piece.vec:
								self.dead_list.append(self.living_list[index])
								self.living_list[index].vec.x = self.dead_index - 1
								self.living_list[index].vec.y = self.dead_index - 1
								self.dead_index -= 1

								self.living_list[piece_index].vec.x = x 
								self.living_list[piece_index].vec.y = y 
								del self.living_list[index]
								break
						else:
							if u.Vec2(x, y+1) == piece.vec:
								self.dead_list.append(self.living_list[index])
								self.living_list[index].vec.x = self.dead_index - 1
								self.living_list[index].vec.y = self.dead_index - 1
								self.dead_index -= 1

								self.living_list[piece_index].vec.x = x 
								self.living_list[piece_index].vec.y = y 
								del self.living_list[index]
								break
					#self.dead_list.append()
				else:
					self.living_list[piece_index].vec.x = x 
					self.living_list[piece_index].vec.y = y
			else:
				self.living_list[piece_index].vec.x = x 
				self.living_list[piece_index].vec.y = y 

		# if self.living_list[piece_index].type == 'P':
		# 	if |self.living_list[piece_index].vec.y - y| == 2:
		# 		self.en_pessant = True:
		# 		self.en_pessant_coords = [self.living_list[piece_index].vec.x, self.living_list[piece_index].vec.y, y]






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
				if c == self.living_list[d].vec.x and r == self.living_list[d].vec.y:
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



		# def initialize_blue_team():


			


			# def initialize_blue_pawns():
			# 		#self.blue_pawns[n].set_location().shit_my_pants() Method chaining - .set_location() would have to return self
			# def initialize_blue_knights():
			# 	#self.blue_knights.append(Knight(1, 2))
			# 	#self.blue_knights.append(Knight(1, 7))
			# def initialize_blue_rooks():
			# def initialize_blue_bishops():
			# def initialize_blue_queen():
			# def initialize_blue_king():

			# initialize_blue_pawns()
			# initialize_blue_knights()
			# initialize_blue_rooks()
			# initialize_blue_bishops()
			# initialize_blue_queen()
			# initialize_blue_king()

		# def initialize_red_team():

			


			# def initialize_red_pawns():
			# def initialize_red_knights():
			# def initialize_red_rooks():
			# def initialize_red_bishops():
			# def initialize_red_queen():
			# def initialize_red_king():
				
			# initialize_red_pawns()
			# initialize_red_knights()
			# initialize_red_rooks()
			# initialize_red_bishops()
			# initialize_red_queen()
			# initialize_red_king()

		# def collect_them_all():

		# 	def collector(collect_from):
		# 		for n in range(len(collect_from)):
		# 			self.living_list.append(collect_from[n])

			#for n in self.blue_team:

		# 	collector(self.blue_pawns)
		# 	collector(self.blue_knights)
		# 	collector(self.blue_rooks)
		# 	collector(self.blue_bishops)
		# 	collector(self.blue_queen)
		# 	collector(self.blue_king)

		# 	collector(self.red_pawns)
		# 	collector(self.red_knights)
		# 	collector(self.red_rooks)
		# 	collector(self.red_bishops)
		# 	collector(self.red_queen)
		# 	collector(self.red_king)

		# initialize_blue_team()
		# initialize_red_team()
		# collect_them_all()

		# moves piece from (c,r) to (nc, nr) and if (nc, nr) already occup. deletes occupying piece
	
	# def move_piece_test(self, c, r, nc, nr):
	# 	piece_del_index = -1
	# 	for test_piece in range(len(self.living_list)):
	# 		if self.living_list[test_piece].vec.x == c and self.living_list[test_piece].vec.y == r:

	# 			for test_piece_two in range(len(self.living_list)):





	# 				if self.living_list[test_piece_two].vec.x == nc and self.living_list[test_piece_two].vec.y == nr:

	# 					piece_del_index = test_piece_two 

	# 			self.living_list[test_piece].vec.x = nc 
	# 			self.living_list[test_piece].vec.y = nr
	# 			#self.living_list[test_piece].vec.xy = (nc, nr)

	# 	if piece_del_index >= 0:
	# 		del self.living_list[piece_del_index]

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