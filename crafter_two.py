









def move_piece_test(self, piece_index:int, x:int, y:int) -> None:
		
		def change_piece(updated_piece_type:str) -> None:
			x = self.living_list[piece_index].vec.x 
			y = self.living_list[piece_index].vec.y
			team = self.living_list[piece_index].team
			if updated_piece_type == 'q':
				self.living_list.append(Queen(u.Vec2(x, y), team))
			elif updated_piece_type == 'n':
				self.living_list.append(Knight(u.Vec2(x, y), team))
			elif updated_piece_type == 'b':
				self.living_list.append(Bishop(u.Vec2(x, y), team))
			elif updated_piece_type == 'r':
				self.living_list.append(Rook(u.Vec2(x, y), team))
			del self.living_list[piece_index]

		def pawn_promotion():
			if self.living_list[piece_index].type == 'P':
				if self.living_list[piece_index].team == 'blue':
					if self.living_list[piece_index].vec.y == 7:
						change_piece('q')
				else:
					if self.living_list[piece_index].vec.y == 0:
						change_piece('q')

		def just_move(x:int, y:int) -> None:
			self.living_list[piece_index].vec.x = x  
			self.living_list[piece_index].vec.y = y 

		def kill_and_move(index:int, x:int, y:int) -> None:
			self.dead_list.append(self.living_list[index])
			self.living_list[index].vec.x = self.dead_index -= 1
			self.living_list[index].vec.y = self.dead_index
			just_move(x, y)
			del self.living_list[index]

		def kill_and_move_en_pessant(index:int, x:int, y:int) -> None:
			self.dead_list.append(self.living_list[index])

		#def reset_en_pessant():
		#	self.en_pessant = False
		#	self.en_pessant_coords = []

		piece_moved = False

		#self, piece_index, x, y
		#checks every active Piece in self.living_list, IF another Piece already in location, 'kill' it from self.living_list and move active Piece into dead Piece's xy coords 
		for index, piece in enumerate(self.living_list):
			if self.living_list[index].vec.x == x and self.living_list[index].vec.y == y:
				
				kill_and_move(index, x, y)

				piece_moved = True

				pawn_promotion()

				break

		#Piece yet unmoved due to no Pieces to kill at destination	

		if piece_moved == False:

			if self.living_list[piece_index].type == 'P': 

				#Pawn Piece moving 2 spaces from origin enabling EN_PESSANT opportunity for next player's turn.

				if abs(self.living_list[piece_index].vec.y - y) == 2 and self.living_list[piece_index].vec.x == x:
					self.reset_en_pessant()
					self.en_pessant = True
					self.en_pessant_coords = [self.living_list[piece_index].vec.x, self.living_list[piece_index].vec.y, y]
					just_move(x, y)

				#Selected Pawn Piece engaging in an EN_PESSANT_ATTACK

				elif u.Vec2(x, y) == self.living_list[piece_index].en_pessant_move[0]: #pawn en_pessant attack move
					for index, piece in enumerate(self.living_list):
						if self.living_list[piece_index].team == 'blue':
							if u.Vec2(x, y-1) == piece.vec:
								kill_and_move(index)

								self.reset_en_pessant()

								break
						else:
							if u.Vec2(x, y+1) == piece.vec:
								kill_and_move(index)

								self.reset_en_pessant()

								break
				#Pawn Piece moving to EMPTY location
				else:
					just_move(x, y)
					self.reset_en_pessant()

					pawn_promotion()

			#NON-Pawn Piece moving to EMPTY location		
			else:
				just_move(x, y)
				self.reset_en_pessant()

				pawn_promotion()