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

	def __init__(self, vec:Vec2, team:str) -> None:
		#self.row = row
		#self.col = col
		#self.cur_space = (self.col, self.row)

		self.vec = vec
		self.team = team
		self.type = ''
		###
		#possible death index for order of death.
		#self.death_index = 0

		self.possible_moves_open = []
		self.possible_moves_enemy = []
		self.impossible_moves_blocked = []
		self.impossible_moves_boundary = []
		#self.board_location = 0
		#self.health = 1

		#self.set_location()

	#def set_location(self):
		#self.board_location = ((self.row -1) * 8) + self.col

	# string representation of object
	def __repr__(self):
		#if self.type != '':
		return str((self.vec.x, self.vec.y)) + "," + str(self.team) + "," + str(self.type)
		#else:
		#	return str(self.col) + "," + str(self.row) + "," + str(self.cur_space) + "," + str(self.team)

	#def name_tester(self) -> None:
	#	print(self.__class__.__name__)

	def reset_possible_moves(self) -> None:
		self.possible_moves_open = []
		self.possible_moves_enemy = []
		self.impossible_moves_blocked = []
		self.impossible_moves_boundary = []

	def set_location(self, new_x:int, new_y:int) -> None:
		self.vec.x = new_x
		self.vec.y = new_y

	def determine_possible_moves_direction(self, potential_spaces:list, direction:Vec2) -> None:
		#move_down, move_up, move_left, move_right

		first_index_found = False

		for n in range(0, 7):
			cur_move = self.vec + direction * (n + 1)

			if first_index_found == False:
				for x in range(len(potential_spaces)):

					action_taken = False
					if cur_move == potential_spaces[x].vec:

						if potential_spaces[x].open == False:

							if potential_spaces[x].team == self.team:
								self.impossible_moves_blocked.append(cur_move) 
								first_index_found = True
								action_taken = True
								break
							else:
								self.possible_moves_enemy.append(cur_move)
								first_index_found = True
								action_taken = True
								break

						else:
							self.possible_moves_open.append(cur_move)
							action_taken = True
							break
					
				if action_taken == False:
					self.impossible_moves_boundary.append(cur_move)
					first_index_found = True

	def check_space(self, potential_spaces:list, cur_move:Vec2) -> None: #cur_move is target_vector 
		
		for x in range(len(potential_spaces)):

			action_taken = False
			if cur_move == potential_spaces[x].vec:

				if potential_spaces[x].open == False:

					if potential_spaces[x].team == self.team: 
						self.impossible_moves_blocked.append(cur_move) 
						action_taken = True
						break
					else:
						self.possible_moves_enemy.append(cur_move)
						action_taken = True
						break

				else:
					self.possible_moves_open.append(cur_move)
					action_taken = True
					break
			
		if action_taken == False:
			self.impossible_moves_boundary.append(cur_move)

	def convert_from_vec2_to_chess_reference_id(self, movement:Vec2) -> str:
			possible_characters = '0a1b2c3d4e5f6g7h'
			x_reference_char = possible_characters.find(str(movement.x)) + 1
			y_reference_num = 8 - movement.y
			return possible_characters[x_reference_char] + str(y_reference_num)

	def display_moves(self) -> None:
		formatted_moves = []
		
		#inverse method

		for movement in self.possible_moves_open:
			formatted_moves.append(self.convert_from_vec2_to_chess_reference_id(movement))
		for movement in self.possible_moves_enemy:
			formatted_moves.append(self.convert_from_vec2_to_chess_reference_id(movement))
		for move in formatted_moves:
			print(move) 
	#break down into small specific tasks, use that as a building block. 


	#def move_piece(self, x:int, y:int) -> None:
	#	self.vec.x = x 
	#	self.vec.y = y   



		# self.possible_moves_open = []
		# self.possible_moves_enemy = []
		# self.impossible_moves_blocked = []
		# self.impossible_moves_boundary = []

class Pawn(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'P'
		self.move_type = "hopper"
		self.init_move = True
		self.en_pessant_move = None
		#self.en_pessant_move = u.Vec2(0,0)

		#self.possible_en_pessant_move = []

		if self.team == "blue":
			self.direction = 1
		elif self.team == "red":
			self.direction = -1

	#nolongerneeded--appliedtoPiece()class
	# def __repr__(self):
	# 	return str(self.col) + "," + str(self.row) + "," + str(self.cur_space) + "," + str(self.team) + "," + str(self.type)


	def add_en_pessant_move(self, x, y):
		self.possible_moves_open.append(u.Vec2(x, y))
		self.en_pessant_move = u.Vec2(x, y)



	def pawn_init_move_set_false(self) -> None:
		self.init_move = False

	#def TRANSMUTE_PAWN_INTO_ANY_OTHER_PIECETYPE_NOT_INCLUDING_KING()
	#IF current pawn piece moves to enemy starting row, ((0,n)OR(7,n))[piece.direction...?]: PAWN can CHANGE into ANY other piece kind(noKING)

	def determine_possible_moves_straight_pawn(self, potential_spaces:list) -> None:
		#move_down, move_up, move_left, move_right

		if (self.team == 'blue' and self.vec.y == 1) or (self.team == 'red' and self.vec.y == 6):
			first_index_found = False

			for n in range(0, 2):
				cur_move = self.vec + move_down * self.direction * (n + 1)

				if first_index_found == False:
					for x in range(len(potential_spaces)):

						action_taken = False
						if cur_move == potential_spaces[x].vec:

							if potential_spaces[x].open == False:

								self.impossible_moves_blocked.append(cur_move)
								first_index_found = True 
								action_taken = True 
								break

							else:
								self.possible_moves_open.append(cur_move)
								action_taken = True
								break
						
					if action_taken == False:
						self.impossible_moves_boundary.append(cur_move)
						first_index_found = True

		else:	#check one space in front
			cur_move = self.vec + move_down * self.direction #* 2

			for x in range(len(potential_spaces)):

				action_taken = False
				if cur_move == potential_spaces[x].vec:

					if potential_spaces[x].open == False:

						self.impossible_moves_blocked.append(cur_move)
						first_index_found = True 
						action_taken = True 
						break

					else:
						self.possible_moves_open.append(cur_move)
						action_taken = True 
						break

			if action_taken == False:
				self.impossible_moves_boundary.append(cur_move)

	def check_space_pawn(self, potential_spaces:list, cur_move:Vec2) -> None: #cur_move is target_vector, checks one space diag to attack
		
			for x in range(len(potential_spaces)):

				action_taken = False
				if cur_move == potential_spaces[x].vec:

					if potential_spaces[x].open == False:

						if potential_spaces[x].team != self.team:
							self.possible_moves_enemy.append(cur_move)					

	def determine_possible_moves(self, potential_spaces:list) -> None:

		self.en_pessant_move = None
		self.reset_possible_moves()

		self.determine_possible_moves_straight_pawn(potential_spaces)
		self.check_space_pawn(potential_spaces, (self.vec + (move_down * self.direction) + move_left))
		self.check_space_pawn(potential_spaces, (self.vec + (move_down * self.direction) + move_right))

class Rook(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'R'
		self.move_type = "glider"

	def determine_possible_moves(self, potential_spaces:list) -> None:
		#move_up, move_down, move_left, move_right
		self.reset_possible_moves()

		self.determine_possible_moves_direction(potential_spaces, move_up)
		self.determine_possible_moves_direction(potential_spaces, move_down)
		self.determine_possible_moves_direction(potential_spaces, move_left)
		self.determine_possible_moves_direction(potential_spaces, move_right)

class Bishop(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'B'
		self.move_type = "glider"

	def determine_possible_moves(self, potential_spaces:list) -> None:

		self.reset_possible_moves()

		self.determine_possible_moves_direction(potential_spaces, (move_up + move_right))
		self.determine_possible_moves_direction(potential_spaces, (move_down + move_right))
		self.determine_possible_moves_direction(potential_spaces, (move_down + move_left))
		self.determine_possible_moves_direction(potential_spaces, (move_up + move_left))

class Queen(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'Q'
		self.move_type = "glider"

	def determine_possible_moves(self, potential_spaces:list) -> None:

		self.reset_possible_moves()

		self.determine_possible_moves_direction(potential_spaces, move_up)
		self.determine_possible_moves_direction(potential_spaces, move_down)
		self.determine_possible_moves_direction(potential_spaces, move_left)
		self.determine_possible_moves_direction(potential_spaces, move_right)
		self.determine_possible_moves_direction(potential_spaces, (move_up + move_right))
		self.determine_possible_moves_direction(potential_spaces, (move_down + move_right))
		self.determine_possible_moves_direction(potential_spaces, (move_down + move_left))
		self.determine_possible_moves_direction(potential_spaces, (move_up + move_left))

class Knight(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'T'
		self.move_type = "hopper"

	def determine_possible_moves(self, potential_spaces:list) -> None:

		self.reset_possible_moves()

		self.check_space(potential_spaces, (self.vec + (move_up * 2) + move_right))
		self.check_space(potential_spaces, (self.vec + move_up + (move_right * 2)))
		self.check_space(potential_spaces, (self.vec + move_down + (move_right * 2)))
		self.check_space(potential_spaces, (self.vec + (move_down * 2) + move_right))
		self.check_space(potential_spaces, (self.vec + (move_down * 2) + move_left))
		self.check_space(potential_spaces, (self.vec + move_down + (move_left * 2)))
		self.check_space(potential_spaces, (self.vec + move_up + (move_left * 2)))
		self.check_space(potential_spaces, (self.vec + (move_up * 2) + move_left))


class King(Piece):
	def __init__(self, vec:Vec2, team:str) -> None:
		super().__init__(vec, team)
		self.type = 'K'
		self.move_type = "hopper"

	def determine_possible_moves(self, potential_spaces:list) -> None:

		self.reset_possible_moves()

		self.check_space(potential_spaces, (self.vec + move_up))
		self.check_space(potential_spaces, (self.vec + move_up + move_right))
		self.check_space(potential_spaces, (self.vec + move_right))
		self.check_space(potential_spaces, (self.vec + move_down + move_right))
		self.check_space(potential_spaces, (self.vec + move_down))
		self.check_space(potential_spaces, (self.vec + move_down + move_left))
		self.check_space(potential_spaces, (self.vec + move_left))
		self.check_space(potential_spaces, (self.vec + move_up + move_left))