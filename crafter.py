#def check_space(self, potential_spaces): FUCK THE LIES
#	cur_move = 

def determine_possible_moves_direction(self, potential_spaces, direction):
	
	#direction can be:
	# "up"
	# "down"
	# "left"
	# "right"
	# "up_left"
	# "up_right"
	# "down_left"
	# "down_right" 

	#UPDATEWITHNEWATTRIBUTES
	#UPDATE___instead of passing the string, simply pass the move_down, move_up... etc... 

	first_index_found = False

	for n in range(0, 7):


		
		cur_move = self.cur_space_vec + direction * (n + 1)

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

								####Change cur_move or cur_space to self.cur_space = u.Vec2(self.col, self.row)####
								####Please, they are all lies.   You can do this.   You are doing this.   You are just doing this.  

def check_space(self, cur_move): #cur_move is target_vector 
		
	for x in range(len(potential_spaces)):

		action_taken = False
		if cur_move.xy == potential_spaces[x].xy:

			if potential_spaces[x].open == False:

				if potential_spaces[x].team == self.team: #notsameteam
					self.impossible_moves_team.append(cur_move) 
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
		#first_index_found = True