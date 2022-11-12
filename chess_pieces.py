#you've got this, if anyone's got this it is you my manFUCKTHELIES.  THEY ARE LIES.  NEVER FORGET.  
from __future__ import annotations
import utils as u
#mport chess_board_test as cbt

#cur_pos = u.Vec2(self.x, self.y)
# move_l = u.Vec2(-1,0)
# move_r = u.Vec2(1,0)
# move_u = u.Vec2(0,-1)
# move_d = u.Vec2(0,1)

###DIRECTIONVECTORS###
move_down = u.Vec2(0,1)   #GOING DOWN DOWN DOWN DOWN DOWNNNN DOOOOOOWWNNN DOOOOOOOOOOWN 
move_up = u.Vec2(0,-1)	#GOING UP UP UP UP UPPPP UPPPPPPPP UPPPPPPPPP
move_right = u.Vec2(1,0)
move_left = u.Vec2(-1,0)


#useparentatts, not necessarily all methods
class Piece():

	def __init__(self, col, row, team):
		self.row = row
		self.col = col
		self.cur_space = (self.col, self.row)

		self.cur_space_vec = u.Vec2(self.col, self.row)
		self.team = team
		self.type = ''

		self.possible_moves_open = []
		self.possible_moves_enemy = []
		self.impossible_moves_team = []
		self.impossible_moves_boundary = []
		#self.board_location = 0
		#self.health = 1

		#self.set_location()

	#def set_location(self):
		#self.board_location = ((self.row -1) * 8) + self.col

	# string representation of object
	def __repr__(self):
		#if self.type != '':
		return str(self.col) + "," + str(self.row) + "," + str(self.cur_space) + "," + str(self.team) + "," + str(self.type)
		#else:
		#	return str(self.col) + "," + str(self.row) + "," + str(self.cur_space) + "," + str(self.team)

	def set_location(self, new_col, new_row):
		self.row = new_row
		self.col = new_col
		self.cur_space = (self.col, self.row)

class Pawn(Piece):
	def __init__(self, col:int, row:int, team:str) -> None:
		super().__init__(col, row, team)
		#self.type = 'P'
		self.move_type = "hopper"
		self.init_move = True
		#self.possible_moves = [] #contains vector objects
		self.possible_moves_straight = [] #one or two straight moves, Vec2 objects
		self.possible_moves_attack = [] #two diag moves, Vec2 objects
		#self.possible_en_pessant_move = []

		if self.team == "blue":
			self.direction = 1
		elif self.team == "red":
			self.direction = -1

	#nolongerneeded--appliedtoPiece()class
	# def __repr__(self):
	# 	return str(self.col) + "," + str(self.row) + "," + str(self.cur_space) + "," + str(self.team) + "," + str(self.type)

	def pawn_init_move_set_false(self):
		self.init_move = False

	#def TRANSMUTE_PAWN_INTO_ANY_OTHER_PIECETYPE_NOT_INCLUDING_KING()
	#IF current pawn piece moves to enemy starting row, ((0,n)OR(7,n))[piece.direction...?]: PAWN can CHANGE into ANY other piece kind(noKING)

	#RECHECK
	def determine_possible_moves(self):

		#move_down gets converted to up or down depending on pawn team/direction
		pawn_cur_space = u.Vec2(self.col, self.row)

		self.possible_moves_straight.append((pawn_cur_space + move_down * self.direction))
		if self.init_move == True:
			self.possible_moves_straight.append((pawn_cur_space + (move_down * 2) * self.direction))
		
		self.possible_moves_attack.append((pawn_cur_space + move_down * self.direction + move_right))
		self.possible_moves_attack.append((pawn_cur_space + move_down * self.direction + move_left))

	#enPESSANT
	#IF in turn previous...OTHERCOLOR PAWN MOVES FROM cols Pos and Neg in relate
	#to current pawn... then can kill OTHERCOLOR pawn and move to OTHERCOLOR pawn's prev location
	# (TURN ATTRIBUTE? ON CHESS BOARD??,PAWN(PIECE) PREV TURN LOCATION ATTRIBUTE??)

class Rook(Piece):
	def __init__(self, col:int, row:int, team:str):
		super().__init__(col, row, team)
		#self.type = 'R'
		self.move_type = "glider"
		self.possible_moves_down = []
		self.possible_moves_up = []
		self.possible_moves_right = []
		self.possible_moves_left = []

		self.possible_moves_down_real = []
		self.possible_moves_up_real = []
		self.possible_moves_right_real = []
		self.possible_moves_left_real = []

		#testatts
		self.possible_moves_down_right_real = []
		self.possible_moves_down_left_real = []
		self.possible_moves_up_right_real = []
		self.possible_moves_up_left_real = []



		#yagni youaintgonnaneedit - avoid data duplication
		self.possible_moves_open = []
		self.possible_moves_enemy = []
		self.impossible_moves_ally = []
		self.impossible_moves_boundary = []
		#condense to just self.possible_moves.   As printing out possible moves... extra specification doesn't matter

		self.impossible_moves_boundary = []
		self.impossible_moves_team = [] # Vec2 Objects
		self.possible_moves_enemy = []
		#self.out_of_bounds = []#?

		#self.cur_space = u.Vec2(self.col, self.row)

	def determine_possible_moves(self):
		
		rook_cur_space = u.Vec2(self.col, self.row)

		for n in range(0, 7):
			self.possible_moves_down.append(rook_cur_space + move_down * (n+1))
			self.possible_moves_up.append(rook_cur_space + move_up * (n+1))
			self.possible_moves_right.append(rook_cur_space + move_right * (n+1))
			self.possible_moves_left.append(rook_cur_space + move_left * (n+1))

	def determine_possible_moves_real(self, potential_spaces):
		rook_cur_space = u.Vec2(self.col, self.row)
		#cur_move = ''
		
		#potential_spaces list brought in - list full of u.Space objects

		#block = False  

		#while block == False:

			# for n in range(0, 7):
			# 	cur_move = rook_cur_space + move_down * (n+1)
			# 	for x in range(len(potential_spaces)):
			# 		if cur_move.xy 
	
		#first_index_found = False
		#action_taken = False 
		
		def determine_possible_moves_down():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + move_down * (n+1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_down_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_down_real.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_up():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + move_up * (n+1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							#print(action_taken)
							if potential_spaces[x].open == False:

								#print(action_taken)
								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									#print('A')
									break
								else:
									self.possible_moves_up_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									#print('B')
									break

							#print(action_taken)
							else:
								self.possible_moves_up_real.append(cur_move)
								action_taken = True
								#print('C')
								break
						#else:
							#pass
					#print(action_taken)
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_right():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + move_right * (n+1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_right_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_right_real.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_left():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + move_left * (n+1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_left_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_left_real.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		# determine_possible_moves_up()
		# determine_possible_moves_down()
		# determine_possible_moves_left()
		# determine_possible_moves_right()


		#######WORKSPACE###############TEMP#####################################################################################################

		def determine_possible_moves_up_right():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + (move_up + move_right) * (n + 1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_up_right_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_up_right_real.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_down_right():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + (move_down + move_right) * (n + 1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: #notsameteam
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_down_right_real.append(cur_move)
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_down_right_real.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_down_left():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + (move_down + move_left) * (n + 1)  ####CHANGE

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: 
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_down_left_real.append(cur_move)  ####CHANGE
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_down_left_real.append(cur_move)  ####CHANGE
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		def determine_possible_moves_up_left():
			first_index_found = False
			#action_taken = False

			for n in range(0, 7):
				#action_taken = False
				cur_move = rook_cur_space + (move_up + move_left) * (n + 1)  ####CHANGE  #ALSOCUR_CUR_SPACE CHANGES

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move.xy == potential_spaces[x].xy:

							if potential_spaces[x].open == False:

								if potential_spaces[x].team == self.team: 
									self.impossible_moves_team.append(cur_move) 
									first_index_found = True
									action_taken = True
									break
								else:
									self.possible_moves_up_left_real.append(cur_move)  ####CHANGE
									self.possible_moves_enemy.append(cur_move)
									first_index_found = True
									action_taken = True
									break

							else:
								self.possible_moves_up_left_real.append(cur_move)  ####CHANGE
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True


		determine_possible_moves_up()
		determine_possible_moves_down()
		determine_possible_moves_left()
		determine_possible_moves_right()
		determine_possible_moves_up_right()
		determine_possible_moves_up_left()
		determine_possible_moves_down_right()
		determine_possible_moves_down_left()




























		#######WORKSPACE###############TEMP#####################################################################################################





			# CHECK
			# cur_move 


			# 	IN 
			# 	potential_spaces.xy

			# 	 	IF IN
			# 	 	check for open vs closed 
					
			# 			IF OPEN
			# 			ADD to potential spaces 

			# 			IF CLOSED

			# 					IF ENEMY
			# 						ADD to potential spaces 
			# 						record enemy space 
			# 					IF ALLY
			# 						NO ADD to potential spaces 
			# 						record ally space 

			# 		IF OUT
			# 		NO ADD to potential spaces 
			# 		record out of bounds?
						





	# while cur_move.xy != potential_spaces[x].xy:
	# 	for n in range(0, 7):
	# 		cur_move = rook_cur_space + move_down * (n+1)
	# 		for x in range(len(potential_spaces)):
	# 			if cur_move.xy == potential_spaces[x].xy

	# 	for n in range(0, 7):
	# 		cur_move = rook_cur_space + move_down * (n+1)




	# 		for x in range(len(potential_spaces)):
	# 			if cur_move.xy == potential_spaces[x].xy:
	# 				if potential_spaces[x].team == self.__class__.__name__:
	# 					self.impossible_moves_team.append(cur_move)

	# 				else:
	# 					self.possible_moves_enemy.append(cur_move)
	# 		if  == False:




	# 		if potential_spaces[n]


	# 	block = False
	# 	for n in range(0, 7):
	# 		if block == False:
	# 			cur_move = rook_cur_space + move_down * (n+1)
	# 			if cur_move.xy in closed_spaces:



	# 			self.possible_moves_down.append(rook_cur_space + move_down * (n + 1))
				
	# 		while cur_move 


class Bishop(Piece):
	def __init__(self, col, row, team):
		super().__init__(col, row, team)
		#self.type = 'B'
		self.move_type = "glider"
		self.possible_moves_up_right = []
		self.possible_moves_down_right = []
		self.possible_moves_down_left = []
		self.possible_moves_up_left = []

	def determine_possible_moves(self):

		bishop_cur_space = u.Vec2(self.col, self.row)
		
		for n in range(0,7):
			self.possible_moves_up_right.append(bishop_cur_space + (move_up + move_right) * (n + 1))
			self.possible_moves_down_right.append(bishop_cur_space + (move_down + move_right) * (n + 1))
			self.possible_moves_down_left.append(bishop_cur_space + (move_down + move_left) * (n + 1))
			self.possible_moves_up_left.append(bishop_cur_space + (move_up + move_left) * (n + 1))


class Queen(Piece):
	def __init__(self, col, row, team):
		super().__init__(col, row, team)
		#self.type = 'Q'
		self.move_type = "glider"
		self.possible_moves_up = []
		self.possible_moves_down = []
		self.possible_moves_left = []
		self.possible_moves_right = []
		self.possible_moves_up_right = []
		self.possible_moves_up_left = []
		self.possible_moves_down_right = []
		self.possible_moves_down_left = []

	def determine_possible_moves(self):
		queen_cur_space = u.Vec2(self.col, self.row)

		for n in range(0, 7):
			self.possible_moves_up.append(queen_cur_space + move_up * (n + 1))
			self.possible_moves_down.append(queen_cur_space + move_down * (n + 1))
			self.possible_moves_left.append(queen_cur_space + move_left * (n + 1))
			self.possible_moves_right.append(queen_cur_space + move_right * (n + 1))
			self.possible_moves_up_right.append(queen_cur_space + (move_up + move_right) * (n + 1))
			self.possible_moves_up_left.append(queen_cur_space + (move_up + move_left) * (n + 1))
			self.possible_moves_down_right.append(queen_cur_space + (move_down + move_right) * (n + 1))
			self.possible_moves_down_left.append(queen_cur_space + (move_down + move_left) * (n + 1))


class Knight(Piece):
	def __init__(self, col, row, team):
		super().__init__(col, row, team)
		#self.type = 'T'
		self.move_type = "hopper"
		self.possible_moves = []#Vec2() objects

	def determine_possible_moves(self):
		knight_cur_space = u.Vec2(self.col, self.row)

		#UP-RIGHT-CLOCKWISE>

		self.possible_moves.append(knight_cur_space + move_right + move_up * 2)
		self.possible_moves.append(knight_cur_space + move_right * 2 + move_up)
		self.possible_moves.append(knight_cur_space + move_right * 2 + move_down)
		self.possible_moves.append(knight_cur_space + move_right + move_down * 2)
		self.possible_moves.append(knight_cur_space + move_left + move_down * 2)
		self.possible_moves.append(knight_cur_space + move_left * 2 + move_down)
		self.possible_moves.append(knight_cur_space + move_left * 2 + move_up)
		self.possible_moves.append(knight_cur_space + move_left + move_up * 2)


class King(Piece):
	def __init__(self, col, row, team):
		super().__init__(col, row, team)
		#self.type = 'K'
		self.move_type = "hopper"
		self.possible_moves = []#Vec2() objects

	def determine_possible_moves(self):
		king_cur_space = u.Vec2(self.col, self.row)

		#UP-RIGHT-CLOCKWISE>

		self.possible_moves.append(king_cur_space + move_up)
		self.possible_moves.append(king_cur_space + move_up + move_right)
		self.possible_moves.append(king_cur_space + move_right)
		self.possible_moves.append(king_cur_space + move_down + move_right)
		self.possible_moves.append(king_cur_space + move_down)
		self.possible_moves.append(king_cur_space + move_down + move_left)
		self.possible_moves.append(king_cur_space + move_left)
		self.possible_moves.append(king_cur_space + move_up + move_left)