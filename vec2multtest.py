import utils as u

new_vec = u.Vec2(0,1)
print(new_vec)

output = new_vec * 1
print(output)
output2 = new_vec * 2
print(output2)

potential_spaces = []
def set_potential_spaces():
			for x in range(0, 8):
				for y in range(0, 8):
					potential_spaces.append(u.Space(u.Vec2(x, y)))
set_potential_spaces()
print(potential_spaces)

right_move = u.Movement(potential_spaces[0], potential_spaces[1], potential_spaces)
#print(right_move.is_in_bounds())
#print(right_move.is_occupied())
#print(right_move.is_enemy())