import unittest
import chess_pieces
import chess_board_test
import utils as u

#class TestPiece(unittest.TestCase):
# class TestBoard(unittest.TestCase):
# 	myBoard = chess_board_test.Board()

# 	myBoard.initialize_both_teams()
# 	#print(myBoard.living_list)
# 	#myBoard.set_potential_spaces()
# 	myBoard.set_open_closed_spaces()

	# print("OPEN")
	# for n in range(len(myBoard.potential_spaces)):
	# 	if myBoard.potential_spaces[n].open == True:
	# 		print(myBoard.potential_spaces[n].xy)
	# print("CLOSED")
	# for n in range(len(myBoard.potential_spaces)):
	# 	if myBoard.potential_spaces[n].open == False:
	# 		print(myBoard.potential_spaces[n].xy)
	# 		print(myBoard.potential_spaces[n].occupied_by)
	




class TestPiece(unittest.TestCase):

	# self.possible_moves_open = []
	# self.possible_moves_enemy = []
	# self.impossible_moves_team = []
	# self.impossible_moves_boundary = []

	def test_determine_possible_moves_direction(self):
		potential_spaces = []
		
		for x in range(0, 8):
			for y in range(0, 8):
				potential_spaces.append(u.Space(u.Vec2(x, y)))

		move_down = u.Vec2(0,1)
		move_up = u.Vec2(0,-1)
		move_right = u.Vec2(1,0)
		move_left = u.Vec2(-1,0)

		test_piece = chess_pieces.Piece(3,0,"blue")#queen
		potential_spaces[30].set_space_closed("pawn", "red") #3,6
		potential_spaces[0].set_space_closed("pawn", "blue") #0,0
		potential_spaces[10].set_space_closed("pawn", "blue")
		#print("FUCK")
		#print(potential_spaces[10])

		#u.Vec2
		test_vecs_open = [u.Vec2(4,0),u.Vec2(5,0),u.Vec2(6,0),u.Vec2(7,0),
						  u.Vec2(4,1),u.Vec2(5,2),u.Vec2(6,3),u.Vec2(7,4),
						  u.Vec2(3,1),u.Vec2(3,2),u.Vec2(3,3),u.Vec2(3,4),u.Vec2(3,5),
						  u.Vec2(2,1),
						  u.Vec2(2,0),u.Vec2(1,0),
						 ]

		test_vecs_boundary = [u.Vec2(3,-1),u.Vec2(4,-1),u.Vec2(8,0),u.Vec2(8,5),u.Vec2(2,-1),
							 ]
		
		test_vecs_ally = [u.Vec2(1,2),u.Vec2(0,0)]
		test_vecs_enemy = [u.Vec2(3,6)]

		test_piece.determine_possible_moves_direction(potential_spaces, move_up)
		test_piece.determine_possible_moves_direction(potential_spaces, move_up + move_right)
		test_piece.determine_possible_moves_direction(potential_spaces, move_right)
		test_piece.determine_possible_moves_direction(potential_spaces, move_down + move_right)
		test_piece.determine_possible_moves_direction(potential_spaces, move_down)
		test_piece.determine_possible_moves_direction(potential_spaces, move_down + move_left)
		test_piece.determine_possible_moves_direction(potential_spaces, move_left)
		test_piece.determine_possible_moves_direction(potential_spaces, move_up + move_left)
		
		#print(test_piece.possible_moves_open)
		#print(test_piece.impossible_moves_boundary)
		#print(test_piece.impossible_moves_team)
		#print(test_piece.possible_moves_enemy)

		self.assertEqual(test_vecs_open, test_piece.possible_moves_open)
		self.assertEqual(test_vecs_boundary, test_piece.impossible_moves_boundary)
		self.assertEqual(test_vecs_ally, test_piece.impossible_moves_team)
		self.assertEqual(test_vecs_enemy, test_piece.possible_moves_enemy)

	def test_check_space(self):
		potential_spaces = []
		
		for x in range(0, 8):
			for y in range(0, 8):
				potential_spaces.append(u.Space(u.Vec2(x, y)))

		test_piece = chess_pieces.Piece(1, 7, "red") #knight

		potential_spaces[21].set_space_closed("pawn", "blue")
		potential_spaces[30].set_space_closed("pawn", "red")

		test_vecs_open = [u.Vec2(0,5)]
		test_vecs_ally = [u.Vec2(3,6)]
		test_vecs_enemy = [u.Vec2(2,5)]
		test_vecs_boundary = [u.Vec2(3,8),u.Vec2(2,9),u.Vec2(0,9),u.Vec2(-1,8),u.Vec2(-1,6)]

		test_piece.check_space(potential_spaces, u.Vec2(2, 5))
		test_piece.check_space(potential_spaces, u.Vec2(3, 6))
		test_piece.check_space(potential_spaces, u.Vec2(3, 8))
		test_piece.check_space(potential_spaces, u.Vec2(2, 9))
		test_piece.check_space(potential_spaces, u.Vec2(0, 9))
		test_piece.check_space(potential_spaces, u.Vec2(-1, 8))
		test_piece.check_space(potential_spaces, u.Vec2(-1, 6))
		test_piece.check_space(potential_spaces, u.Vec2(0, 5))

		self.assertEqual(test_vecs_open, test_piece.possible_moves_open)
		self.assertEqual(test_vecs_ally, test_piece.impossible_moves_team)
		self.assertEqual(test_vecs_enemy, test_piece.possible_moves_enemy)
		self.assertEqual(test_vecs_boundary, test_piece.impossible_moves_boundary)

class TestPawn(unittest.TestCase):
		potential_spaces = []
		
		for x in range(0, 8):
			for y in range(0, 8):
				potential_spaces.append(u.Space(u.Vec2(x, y)))

		potential_spaces[27].set_space_closed("pawn", "red")#3,3
		potential_spaces[18].set_space_closed("pawn", "red")#2,2
		potential_spaces[34].set_space_closed("pawn", "blue")#4,2
		#print(potential_spaces[34])

		test_pawn_one = chess_pieces.Pawn(3,1,"blue")
		test_pawn_one.determine_possible_moves(potential_spaces)

		# self.possible_moves_open = []  #straight moves
		# self.possible_moves_enemy = []  #diag attack moves
		# self.impossible_moves_team = []  #straight moves blocked by team-piece
		# self.impossible_moves_boundary = []  #straight moves blocked by boundary

		#(3,3)FRONT
		#(2,2)attckleft
		#(4,2)attckright

		#print(potential_spaces[27])#3,3
		#print(potential_spaces[18])#2,2
		#print(potential_spaces[34])#4,2

		

		print("FUCK")
		print(test_pawn_one.possible_moves_open)
		print(test_pawn_one.possible_moves_enemy)
		print(test_pawn_one.impossible_moves_enemy)
		print(test_pawn_one.impossible_moves_team)
		print(test_pawn_one.impossible_moves_boundary)






		

		



















# class TestKing(unittest.TestCase):
# 	def test_determine_possible_moves(self):
# 		test_king = chess_pieces.King(3,7,"red")
# 		test_king.determine_possible_moves()

# 		#UP-RIGHT-CLOCKWISE>

# 		test_vecs = [u.Vec2(3,6),
# 					 u.Vec2(4,6),
# 					 u.Vec2(4,7),
# 					 u.Vec2(4,8),
# 					 u.Vec2(3,8),
# 					 u.Vec2(2,8),
# 					 u.Vec2(2,7),
# 					 u.Vec2(2,6),
# 					 ]

# 		for vec in range(len(test_vecs)):
# 			self.assertEqual(test_vecs[vec].xy, test_king.possible_moves[vec].xy)

# class TestKnight(unittest.TestCase):
# 	def test_determine_possible_moves(self):
# 		test_knight =  chess_pieces.Knight(6,0,"blue")
# 		test_knight.determine_possible_moves()

# 		#UP-RIGHT-CLOCKWISE>

# 		test_vecs = [u.Vec2(7,-2),
# 	     			 u.Vec2(8,-1),
# 					 u.Vec2(8,1),
# 					 u.Vec2(7,2),
# 					 u.Vec2(5,2),
# 					 u.Vec2(4,1),
# 					 u.Vec2(4,-1),
# 					 u.Vec2(5,-2),
# 				    ]

# 		for vec in range(len(test_vecs)):
# 			self.assertEqual(test_vecs[vec].xy, test_knight.possible_moves[vec].xy)

# class TestQueen(unittest.TestCase):
# 	def test_determine_possible_moves(self):
# 		test_queen = chess_pieces.Queen(3,0,"blue")
# 		test_queen.determine_possible_moves()

# 		test_vecs_up = [u.Vec2(3,-1),
# 				   	    u.Vec2(3,-2),
# 				    	u.Vec2(3,-3),
# 						u.Vec2(3,-4),
# 						u.Vec2(3,-5),
# 						u.Vec2(3,-6),
# 						u.Vec2(3,-7),
# 						]
# 		test_vecs_down = [u.Vec2(3,1),
# 						  u.Vec2(3,2),
# 						  u.Vec2(3,3),
# 						  u.Vec2(3,4),
# 						  u.Vec2(3,5),
# 						  u.Vec2(3,6),
# 						  u.Vec2(3,7),
# 						 ]
# 		test_vecs_right = [u.Vec2(4,0),
# 						   u.Vec2(5,0),
# 						   u.Vec2(6,0),
# 						   u.Vec2(7,0),
# 						   u.Vec2(8,0),
# 						   u.Vec2(9,0),
# 						   u.Vec2(10,0),
# 						  ]
# 		test_vecs_left = [u.Vec2(2,0),
# 						  u.Vec2(1,0),
# 						  u.Vec2(0,0),
# 						  u.Vec2(-1,0),
# 						  u.Vec2(-2,0),
# 						  u.Vec2(-3,0),
# 						  u.Vec2(-4,0),
# 						 ]
# 		test_vecs_up_right = [u.Vec2(4,-1),
# 							  u.Vec2(5,-2),
# 							  u.Vec2(6,-3),
# 							  u.Vec2(7,-4),
# 							  u.Vec2(8,-5),
# 							  u.Vec2(9,-6),
# 							  u.Vec2(10,-7),
# 							 ]
# 		test_vecs_up_left = [u.Vec2(2,-1),
# 							 u.Vec2(1,-2),
# 							 u.Vec2(0,-3),
# 							 u.Vec2(-1,-4),
# 							 u.Vec2(-2,-5),
# 							 u.Vec2(-3,-6),
# 							 u.Vec2(-4,-7),
# 							 ]
# 		test_vecs_down_right = [u.Vec2(4,1),
# 							    u.Vec2(5,2),
# 							    u.Vec2(6,3),
# 							    u.Vec2(7,4),
# 							    u.Vec2(8,5),
# 							    u.Vec2(9,6),
# 							    u.Vec2(10,7),
# 							   ]
# 		test_vecs_down_left = [u.Vec2(2,1),
# 							   u.Vec2(1,2),
# 							   u.Vec2(0,3),
# 							   u.Vec2(-1,4),
# 							   u.Vec2(-2,5),
# 							   u.Vec2(-3,6),
# 							   u.Vec2(-4,7),
# 							  ]

# 		for vec in range(len(test_vecs_up)):
# 			self.assertEqual(test_vecs_up[vec].xy, test_queen.possible_moves_up[vec].xy)
# 			self.assertEqual(test_vecs_down[vec].xy, test_queen.possible_moves_down[vec].xy)
# 			self.assertEqual(test_vecs_left[vec].xy, test_queen.possible_moves_left[vec].xy)
# 			self.assertEqual(test_vecs_right[vec].xy, test_queen.possible_moves_right[vec].xy)
# 			self.assertEqual(test_vecs_up_right[vec].xy, test_queen.possible_moves_up_right[vec].xy)
# 			self.assertEqual(test_vecs_up_left[vec].xy, test_queen.possible_moves_up_left[vec].xy)
# 			self.assertEqual(test_vecs_down_right[vec].xy, test_queen.possible_moves_down_right[vec].xy)
# 			self.assertEqual(test_vecs_down_left[vec].xy, test_queen.possible_moves_down_left[vec].xy)
	

# class TestBishop(unittest.TestCase):
# 	def test_determine_possible_moves(self):
# 		test_bishop = chess_pieces.Bishop(2, 0, "blue")
# 		test_bishop.determine_possible_moves()

# 		#(2, 0)
# 		test_vecs_up_right = [u.Vec2(3,-1),
# 							  u.Vec2(4,-2),
# 							  u.Vec2(5,-3),
# 							  u.Vec2(6,-4),
# 							  u.Vec2(7,-5),
# 							  u.Vec2(8,-6),
# 							  u.Vec2(9,-7),
# 							 ]

# 		test_vecs_up_left = [u.Vec2(1,-1),
# 							 u.Vec2(0,-2),
# 							 u.Vec2(-1,-3),
# 							 u.Vec2(-2,-4),
# 							 u.Vec2(-3,-5),
# 							 u.Vec2(-4,-6),
# 							 u.Vec2(-5,-7),
# 							 ]

# 		test_vecs_down_right = [u.Vec2(3,1),
# 							    u.Vec2(4,2),
# 							    u.Vec2(5,3),
# 							    u.Vec2(6,4),
# 							    u.Vec2(7,5),
# 							    u.Vec2(8,6),
# 							    u.Vec2(9,7),
# 							   ]

# 		test_vecs_down_left = [u.Vec2(1,1),
# 							   u.Vec2(0,2),
# 							   u.Vec2(-1,3),
# 							   u.Vec2(-2,4),
# 							   u.Vec2(-3,5),
# 							   u.Vec2(-4,6),
# 							   u.Vec2(-5,7),
# 							  ]

# 		for vec in range(len(test_vecs_up_right)):
# 			self.assertEqual(test_vecs_up_right[vec].xy, test_bishop.possible_moves_up_right[vec].xy)
# 			self.assertEqual(test_vecs_up_left[vec].xy, test_bishop.possible_moves_up_left[vec].xy)
# 			self.assertEqual(test_vecs_down_right[vec].xy, test_bishop.possible_moves_down_right[vec].xy)
# 			self.assertEqual(test_vecs_down_left[vec].xy, test_bishop.possible_moves_down_left[vec].xy)

# class TestRook(unittest.TestCase):
# 	def test_determine_possible_moves(self):
		

# 		test_vecs_up = [u.Vec2(0,6),
# 				   	    u.Vec2(0,5),
# 				    	u.Vec2(0,4),
# 						u.Vec2(0,3),
# 						u.Vec2(0,2),
# 						u.Vec2(0,1),
# 						u.Vec2(0,0),
# 						]
# 		test_vecs_down = [u.Vec2(0,8),
# 						  u.Vec2(0,9),
# 						  u.Vec2(0,10),
# 						  u.Vec2(0,11),
# 						  u.Vec2(0,12),
# 						  u.Vec2(0,13),
# 						  u.Vec2(0,14),
# 						 ]
# 		test_vecs_right = [u.Vec2(1,7),
# 						   u.Vec2(2,7),
# 						   u.Vec2(3,7),
# 						   u.Vec2(4,7),
# 						   u.Vec2(5,7),
# 						   u.Vec2(6,7),
# 						   u.Vec2(7,7),
# 						  ]
# 		test_vecs_left = [u.Vec2(-1,7),
# 						  u.Vec2(-2,7),
# 						  u.Vec2(-3,7),
# 						  u.Vec2(-4,7),
# 						  u.Vec2(-5,7),
# 						  u.Vec2(-6,7),
# 						  u.Vec2(-7,7),
# 						 ]


		

# 		test_rook_red = chess_pieces.Rook(0,7,"red")
# 		test_rook_red.determine_possible_moves()



# 		for vec in range(len(test_vecs_up)):
# 			self.assertEqual(test_vecs_up[vec].xy, test_rook_red.possible_moves_up[vec].xy)
# 		for vec in range(len(test_vecs_down)):
# 			self.assertEqual(test_vecs_down[vec].xy, test_rook_red.possible_moves_down[vec].xy)
# 		for vec in range(len(test_vecs_right)):
# 			self.assertEqual(test_vecs_right[vec].xy, test_rook_red.possible_moves_right[vec].xy)
# 		for vec in range(len(test_vecs_left)):
# 			self.assertEqual(test_vecs_left[vec].xy, test_rook_red.possible_moves_left[vec].xy)


	# def test_determine_possible_moves_real(self):

	# 	#print("FUCK")


	# 	# test_vecs_down_real = [u.Vec2(0,8),
	# 	# 				       u.Vec2(0,9),
	# 	# 				  	   u.Vec2(0,10),
	# 	# 				  	   u.Vec2(0,11),
	# 	# 				  	   u.Vec2(0,12),
	# 	# 				  	   u.Vec2(0,13),
	# 	# 				  	   u.Vec2(0,14),
	# 	# 				 	   ]

	# 	test_potential_pieces_real = []
		
	# 	for x in range(0, 8):
	# 		for y in range(0, 8):
	# 			test_potential_pieces_real.append(u.Space(u.Vec2(x, y)))



	# 	#test_potential_pieces_real = [u.Space(u.Vec2(3,9))]
	# 	#test_potential_pieces_real[0].set_space_closed("red")

	# 	#print(test_potential_pieces_real)
	# 	print(test_potential_pieces_real[31])
	# 	print(test_potential_pieces_real[13])
	# 	print(test_potential_pieces_real[24])
	# 	test_potential_pieces_real[31].set_space_closed(test_potential_pieces_real[31].__class__.__name__,"red")
	# 	test_potential_pieces_real[13].set_space_closed(test_potential_pieces_real[13].__class__.__name__,"blue")
	# 	test_potential_pieces_real[24].set_space_closed(test_potential_pieces_real[24].__class__.__name__,"red")

	# 	test_rook_red_real = chess_pieces.Rook(3,5,"red")
	# 	print(test_rook_red_real)

	# 	test_rook_red_real.determine_possible_moves()
	# 	test_rook_red_real.determine_possible_moves_real(test_potential_pieces_real)
		
	# 	print("FUCK")
	# 	print(test_rook_red_real.possible_moves_down_real)
	# 	print(test_rook_red_real.possible_moves_up_real)
	# 	print(test_rook_red_real.possible_moves_left_real)
	# 	print(test_rook_red_real.possible_moves_right_real)
	# 	print(test_rook_red_real.possible_moves_down_right_real)
	# 	print(test_rook_red_real.possible_moves_up_left_real)
	# 	print(test_rook_red_real.possible_moves_down_left_real)
	# 	print(test_rook_red_real.possible_moves_up_right_real)
	# 	print("FUCK")
	# 	print(test_rook_red_real.possible_moves_right)
	# 	print(test_rook_red_real.impossible_moves_team)
	# 	print(test_rook_red_real.possible_moves_enemy)
	# 	print(test_rook_red_real.impossible_moves_boundary)

		#BLOCKDIAGTEST



		# test_rook_blue = chess_pieces.Rook(0,0,"blue")

		# for vec in range(len(test_vecs_forward)):
		# 	self.assertEqual(test_vecs_forward[vec].xy, test_rook_blue.possible_moves_forward[vec].xy)
		# for vec in range(len(test_vecs_backward)):
		# 	self.assertEqual(test_vecs_backward[vec].xy, test_rook_blue.possible_moves_backward[vec].xy)
		# for vec in range(len(test_vecs_right)):
		# 	self.assertEqual(test_vecs_right[vec].xy, test_rook_blue.possible_moves_right[vec].xy)
		# for vec in range(len(test_vecs_left)):
		# 	self.assertEqual(test_vecs_left[vec].xy, test_rook_blue.possible_moves_left[vec].xy)

# class TestPawn(unittest.TestCase):

# 	def test_determine_possible_moves(self):
# 		test_pawn_red = chess_pieces.Pawn(0,6,"red")

# 		test_vecs_straight = [u.Vec2(0,5),
# 					  		  u.Vec2(0,4),
# 					  		 ]
					 
# 		test_vecs_attack = [u.Vec2(1,5),
# 					  	  u.Vec2(-1,5),
# 					   	 ]

# 		test_pawn_red.determine_possible_moves()

# 		for vec in range(len(test_vecs_straight)):
# 			self.assertEqual(test_vecs_straight[vec].xy, test_pawn_red.possible_moves_straight[vec].xy)
# 		for vec in range(len(test_vecs_attack)):
# 			self.assertEqual(test_vecs_attack[vec].xy, test_pawn_red.possible_moves_attack[vec].xy)

# 		test_pawn_blue = chess_pieces.Pawn(0,0,"blue")

# 		test_vecs_blue_straight = [u.Vec2(0,1),
# 						  		   u.Vec2(0,2),
# 						  		  ]
					
# 		test_vecs_blue_attack = [u.Vec2(1,1),
# 						  		 u.Vec2(-1,1),
# 						  		]

# 		test_pawn_blue.determine_possible_moves()

# 		for vec in range(len(test_vecs_blue_straight)):
# 			self.assertEqual(test_vecs_blue_straight[vec].xy, test_pawn_blue.possible_moves_straight[vec].xy)
# 		for vec in range(len(test_vecs_blue_attack)):
# 			self.assertEqual(test_vecs_blue_attack[vec].xy, test_pawn_blue.possible_moves_attack[vec].xy)
# 	# def test_determine_possible_moves_blue(self):
# 	# 	#arrange,act,assert
# 	# 	#arrange:
# 	# 	test_pawn = chess_pieces.Pawn(0,0,"blue")
# 	# 	#arrange:
# 	# 	#test_board = chess_board_test.Board()
# 	# 	#calling the  MethodUnderTest == ACT
# 	# 	possible_moves = test_pawn.determine_possible_moves() 

# 	# 	#assert
# 	# 	self.assertEqual(2, len(possible_moves))

# 	# 	self.assertEqual((-1, 1), possible_moves[0])
# 	# 	self.assertEqual((1, 1), possible_moves[1])
	
# 	# def test_determine_possible_moves_red(self):
# 	# 	test_pawn = chess_pieces.Pawn(0, 6, "red")
# 	# 	possible_moves = test_pawn.determine_possible_moves()

# 	# 	self.assertEqual(2, len(possible_moves))

# 	# 	self.assertEqual((1, 5), possible_moves[0])
# 	# 	self.assertEqual((-1, 5), possible_moves[1])
# 	def test_pawn_init_move_set_false(self):
# 		test_pawn = chess_pieces.Pawn(0,0,"blue")

# 		test_pawn.pawn_init_move_set_false()

# 		self.assertEqual(False, test_pawn.init_move)


	






						







	#TEST --> CALL initialize_both_teams()
		#ARRANGE, ACT, ASSERT 

# class TestBoard(unittest.TestCase):
# 	test_board = chess_board_test.Board()
# 	test_board.initialize_both_teams()

# 	cool_list = []
# 	for test_piece in test_board.living_list:
# 		if test_piece.team == "red" and test_piece.type == 'P':
			
# 			cool_list.append(test_piece.init_turn)

# 	def increment_ll_red_pawns_turn(self):
# 	def increment_ll_blue_pawns_turn(self):




if __name__ == '__main__':
	unittest.main()


#class TestBoard