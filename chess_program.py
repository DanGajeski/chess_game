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



user_input = ''
#while user_input != 'q':
fuck_2 = chess_board_test.Board()
fuck_2.initialize_both_teams()
fuck_2.set_open_closed_spaces()


while user_input != 'q':
	fuck_2.display_board()
	balls = fuck_2.player_select_piece()
	fuck_2.select_piece_determine_movements(balls)
	fuck_2.select_piece_display_movements(balls)
	fuck_2.move_piece(balls)
	fuck_2.set_open_closed_spaces()


#fuck_2.list_active_pieces()
#fuck_2.display_board()
# fuck_2.move_piece(0, 0, 4)
# fuck_2.set_open_closed_spaces()
# fuck_2.move_piece(17, 1, 4)
# fuck_2.set_open_closed_spaces()
# fuck_2.display_board()
# print(fuck_2.en_pessant)
# print(fuck_2.en_pessant_coords)
# fuck_2.select_piece_determine_movements(0)
# fuck_2.select_piece_display_movements(0)
# fuck_2.move_piece(0, 1, 5)
# fuck_2.display_board()









#don'tlistentothelies







#fuck_2.select_piece_display_movements(0)
#fuck_2.move_piece_test(0, 1, 5)
#fuck_2.display_board()

#fuck_2.list_active_pieces()

#fuck_2.move_piece_test(23, 0, 5)
#fuck_2.display_board()

#fuck_2.move_piece_test(0, 1, 6)
#fuck_2.display_board()

#fuck_2.move_piece_test(0, 1, 7)
#fuck_2.display_board()
#fuck_2.list_active_pieces()
#fuck_2.living_list[0].name_tester()


#fuck_2.collect_them_all()
#print(fuck_2.living_list)
#fuck_2.get_map_locations()
#print(fuck_2.current_locations)




# #print(fuck_2.living_list)
# fuck_2.display_board()
# #fuck_2.list_active_pieces()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 2, 2)
# fuck_2.set_open_closed_spaces()
# fuck_2.display_board()
# #fuck_2.print_spaces_for_test()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 3, 4)
# fuck_2.set_open_closed_spaces()
# fuck_2.display_board()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 4, 6)
# fuck_2.set_open_closed_spaces()
# fuck_2.print_spaces_for_test()
# fuck_2.display_board()
# #fuck_2.list_active_pieces()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 2, 5)
# fuck_2.set_open_closed_spaces()
# fuck_2.print_spaces_for_test()
# fuck_2.display_board()
# #fuck_2.print_dead_for_test()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 0, 6)
# fuck_2.set_open_closed_spaces()
# fuck_2.display_board()
# #fuck_2.print_dead_for_test()
# fuck_2.select_piece_display_movements(8)
# fuck_2.move_piece_test(8, 2, 7)
# fuck_2.set_open_closed_spaces()
# fuck_2.display_board()
# #fuck_2.print_dead_for_test()
# #fuck_2.list_active_pieces()
# fuck_2.select_piece_display_movements(23)


#FUCKYESITWORKSSSS!!!!!SHESALIVEEEEEEEEEEEEEEFUCKTHELIESSSSSSS






#print(fuck_2.living_list[0].determine_possible_moves())
#print(fuck_2.living_list[0].team)
#print(fuck_2.living_list[10].type)
#print(fuck_2.living_list[10].determine_possible_moves_rdlu())
#print(fuck_2.living_list[0].determine_possible_moves("red"))
# print(fuck_2.living_list[8].type)
# print(fuck_2.living_list[8].determine_possible_moves())
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(0, 0, 0, 1)
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# print()
# print()
# fuck_2.move_piece_test(0, 1, 0, 2)
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(0, 2, 1, 1)
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(1, 1, 1, 5)
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(1, 5, 1, 6)
#don't listen to the lies.  You've rocked this.  
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(1, 6, 2, 4)
# fuck_2.display_board()
# print(len(fuck_2.living_list))
# fuck_2.move_piece_test(3, 0, 4, 3)
# fuck_2.display_board()
# print(len(fuck_2.living_list))