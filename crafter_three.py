def player_select_piece():
		active_piece = input("Please select Piece to move: (ex: 'd5')")
		active_piece_x = 0
		active_piece_y = 0
		possible_characters = 'abcdefgh'
		active_piece_x = possible_characters.find(active_piece[0])
		active_piece_y = 8 - int(active_piece[1])
		print(active_piece_x, active_piece_y)

player_select_piece()