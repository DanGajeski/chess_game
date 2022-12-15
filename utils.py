from __future__ import annotations

#rep 2 dim vector
class Vec2():
	def __init__(self, x:int, y:int):
		self.x = x
		self.y = y
		#self.xy = (self.x, self.y)

	def __add__(self, other_vec:Vec2) -> Vec2:
		x = self.x + other_vec.x
		y = self.y + other_vec.y 
		return Vec2(x, y)

	def __sub__(self, other_vec:Vec2) -> Vec2:
		x = self.x - other_vec.x
		y = self.y - other_vec.y 
		return Vec2(x, y)

	def __mul__(self, scalar:float) -> Vec2:
		return Vec2(self.x * scalar, self.y * scalar)

	def __div__(self, scalar:float) -> Vec2:
		return Vec2(self.x / scalar, self.y / scalar)

	def __repr__(self):
		return "Vec2({},{})".format(self.x, self.y)
		#return "HELLO {}, HOW ARE YOU DOING {}?".format(self.x, self.y)
		#return f"hello {self.x}"
		#return "Hello %s!" % self.x

	def __eq__(self, other_vec:Vec2) -> Bool:
	#	if other_vec == None:
	#		return False
	#	return False
		return other_vec is not None and self.x == other_vec.x and self.y == other_vec.y
		#	return True
		#else:
	#		return False
		# return True if self.x == other_vec.x and if self.y == other_vec.y

	#def give_position(self) -> tuple:
	#	return (self.x, self.y) 

class Space():
	def __init__(self, vec:Vec2):
		self.vec = vec
		#self.x = vec.x 
		#self.y = vec.y 
		#self.xy = (self.x, self.y)
		self.open = True
		#self.closed = False
		self.piece = ''
		self.team = ''
		self.closed_this_turn = False


	def __repr__(self):
		return "Space({},{},{})".format(self.vec, self.open, self.piece)

	def set_space_closed(self, piece_name, team):
		self.open = False
		#self.occupied_by = piece_type
		self.team = team
		self.piece = piece_name

	def set_space_open(self):
		self.open = True 
		self.team = ''
		self.piece = ''


# class Movement():
# 	def __init__(self, cur_space:Space, space:Space, potential_spaces:list):
# 		self.cur_space = cur_space
# 		self.space = space
# 		self.potential_spaces = potential_spaces

# 	def is_in_bounds(self):
# 		for n in range(len(self.potential_spaces)):
# 			if self.space.xy == self.potential_spaces[n].xy:
# 				return True 
# 	def is_occupied(self):
# 		if self.space.open != True:
# 			return True 
# 	def is_enemy(self):
# 		if self.cur_space.occupy_team != self.space.occupy_team:
# 			return True

# class Movement():
# 	def __init__(self, cur_space:Space, direction:Movement2):


# Movement2(u.Vec2(0,1)) > down_movement
# # Movement2(u.Vec2(1,1)) > up_right_movement
# # Movement2(u.Vec2(0,1)) > right_movement
# # Movement2(u.Vec2(0,1)) > down_right_movement
# # Movement2(u.Vec2(0,1)) > down_movement
# # Movement2(u.Vec2(0,1)) > down_left_movement
# # Movement2(u.Vec2(0,1)) > left_movement
# # Movement2(u.Vec2(0,1)) > up_left_movement

# class Movement2():
# 	def __init__(self, vec:Vec2, team:str, potential_spaces:list):
# 		self.cur_team = team
# 		self.vec_direction = vec  
# 		self.potential_spaces = potential_spaces





		#self.closed = True 


# position = Vec2(0,0)

# move_r = Vec2(1,0)
# move_l = Vec2(-1,0)
# move_u = Vec2(0,-1)
# move_d = Vec2(0,1)

# move_diag_dr = Vec2(1,1)
# move_diag_dl = Vec2(-1,1)
# move_diag_ur = Vec2(1,-1)
# move_diag_ul = Vec2(-1,-1)

# #.....

# #position.add(move_right)
# print(position + move_r)
# new_pos = Vec2(0,0)
# print(new_pos.x)
# print(new_pos.y)
# new_pos = position + (move_r * 2)
# print(new_pos.x)
# print(new_pos.y)
