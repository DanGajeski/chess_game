from __future__ import annotations

#2 dimensional vector class
class Vec2():
	def __init__(self, x:int, y:int):
		self.x = x
		self.y = y

	def __add__(self, other_vec:Vec2) -> Vec2:
		return Vec2(self.x + other_vec.x, self.y + other_vec.y)

	def __sub__(self, other_vec:Vec2) -> Vec2:
		return Vec2(self.x - other_vec.x, self.y - other_vec.y)

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
		return other_vec is not None and self.x == other_vec.x and self.y == other_vec.y 

class Space():
	def __init__(self, vec:Vec2):
		self.vec = vec
		self.open = True
		self.piece = ''
		self.team = ''
		self.closed_this_turn = False

	def __repr__(self):
		return "Space({},{},{})".format(self.vec, self.open, self.piece)

	def set_space_closed(self, piece_name, team):
		self.open = False
		self.team = team
		self.piece = piece_name

	def set_space_open(self):
		self.open = True 
		self.team = ''
		self.piece = ''