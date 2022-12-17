#you are strong and you are not the lies in your head
#you wrote this.  you can and will write a lot more
#import rocket
import chess_board_test
import os
#os.system('cls')

user_input = ""
user_input_xy = ""
x_y = []
#player = ["player_1", "player_2"]
player = {"player_1":"blue", "player_2":"red"}
turn = 0


# fuck_2 = chess_board_test.Board()
# fuck_2.initialize_both_teams()
# fuck_2.set_open_closed_spaces()
# while user_input != 'q':
# 	#os.system('cls')
# 	fuck_2.display_board()
# 	fuck_2.list_active_pieces()
# 	if turn % 2 == 0:
# 		print("{}'s turn ({}).".format('player_1', player['player_1']))
# 	else:
# 		print("{}'s turn ({}).".format('player_2', player['player_2']))
# 	user_input = input("Select piece to move:")
# 	print("Potential moves:")
# 	fuck_2.select_piece_display_movements(int(user_input))
# 	user_input_xy = input("Select space to move to, ex: '2 2':")
# 	x_y = user_input_xy.split(' ')
# 	fuck_2.move_piece_test(int(user_input), int(x_y[0]), int(x_y[1]))
# 	fuck_2.set_open_closed_spaces()
# 	turn += 1
# 	os.system('cls')







fuck_2 = chess_board_test.Board()
#fuck_2.display_board()

#print(fuck_2.blue_pawns)
	#fuck_2.initialize_blue_pawns()
	#fuck_2.initialize_blue_knights()
#fuck = rocket.Rocket()
#print(fuck_2.blue_pawns)

fuck_2.initialize_both_teams()
fuck_2.set_open_closed_spaces()
#fuck_2.display_board()
fuck_2.list_active_pieces()
fuck_2.move_piece(0, 0, 4)
fuck_2.set_open_closed_spaces()
#fuck_2.display_board()
#print(fuck_2.en_pessant)
#print(fuck_2.en_pessant)
#print(fuck_2.en_pessant_coords)
fuck_2.move_piece(17, 1, 4)
fuck_2.set_open_closed_spaces()
fuck_2.display_board()

print(fuck_2.en_pessant)
print(fuck_2.en_pessant_coords)

fuck_2.select_piece_determine_movements(0)
fuck_2.select_piece_display_movements(0)

#fuck_2.list_active_pieces()
#fuck_2.select_piece_determine_movements(1)
#fuck_2.select_piece_display_movements(1)

fuck_2.move_piece(0, 1, 5)
fuck_2.display_board()
#don'tlistentothelies