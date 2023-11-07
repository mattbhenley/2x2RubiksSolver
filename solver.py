""" import random

cube = [
    # Front face
    [['F1', 'F2'],
     ['F3', 'F4']],
    # Back face
    [['B1', 'B2'],
     ['B3', 'B4']],
    # Left face
    [['L1', 'L2'],
     ['L3', 'L4']],
    # Right face
    [['R1', 'R2'],
     ['R3', 'R4']],
    # Up face
    [['U1', 'U2'],
     ['U3', 'U4']],
    # Down face
    [['D1', 'D2'],
     ['D3', 'D4']]
]

def scramble_cube(cube, num_moves):
    possible_moves = ["U", "U'", "R", "R'", "F", "F'"]
    for _ in range(num_moves):
        move = random.choice(possible_moves)
        apply_move(cube, move)

def apply_move(cube, move):
    # Implement the logic to apply the move to the cube.

    def solve_first_layer(cube):
    # Implement solving the first layer (e.g., one of the faces).

        def solve_second_layer(cube):
    # Implement solving the second layer.

            def is_solved(cube):
    # Implement a check to verify if the cube is solved.

                def solve_cube(cube):
    # Solve the first layer.
                    solve_first_layer(cube)

    # Solve the second layer.
    solve_second_layer(cube)

    # Check if the cube is solved.
    if is_solved(cube):
        print("Cube is solved!")
    else:
        print("Cube is not solved.")

# Main program
if __name__ == '__main__':
    scramble_cube(cube, 10)  # Scramble the cube with 10 random moves
    solve_cube(cube)
 """

import sys

#          -------
#         | 16 17 |
#         |   Y   |
#         | 18 19 |
#  ------- ------- ------- -------
# | 12 13 | 00 01 | 04 05 | 08 09 |
# |   X   |   Z   |   X   |   Z   |
# | 14 15 | 02 03 | 06 07 | 10 11 |
#  ------- ------- ------- -------
#         | 20 21 |
#         |   Y   |
#         | 22 23 |
#          -------

MOVES = [
    [0, 21, 2, 23, 6, 4, 7, 5, 19, 9, 17, 11, 12, 13, 14, 15, 16, 1, 18, 3, 20, 10, 22, 8], # CW X
    [0, 1, 14, 15, 4, 5, 2, 3, 8, 9, 6, 7, 12, 13, 10, 11, 16, 17, 18, 19, 22, 20, 23, 21], # CW Y
    [2, 0, 3, 1, 18, 5, 19, 7, 8, 9, 10, 11, 12, 20, 14, 21, 16, 17, 15, 13, 6, 4, 22, 23], # CW Z
    [0, 17, 2, 19, 5, 7, 4, 6, 23, 9, 21, 11, 12, 13, 14, 15, 16, 10, 18, 8, 20, 1, 22, 3], # CCW X
    [0, 1, 6, 7, 4, 5, 10, 11, 8, 9, 14, 15, 12, 13, 2, 3, 16, 17, 18, 19, 21, 23, 20, 22], # CCW Y
    [1, 3, 0, 2, 21, 5, 20, 7, 8, 9, 10, 11, 12, 19, 14, 18, 16, 17, 4, 6, 13, 15, 22, 23], # CCW Z
]

MOVE_NAMES = ['+X', '+Y', '+Z', '-X', '-Y', '-Z']

def do_move(state, move):
    return tuple([state[i] for i in move])

def solved(state):
    for i in range(0, 24, 4):
        for j in range(1, 4):
            if state[i] != state[i+j]:
                return False
    return True

def _solve(state, depth, moves, memo):
    if solved(state):
        return list(moves)
    if depth <= 0:
        return
    if memo.get(state, -1) >= depth:
        return
    memo[state] = depth
    for i, move in enumerate(MOVES):
        new_state = do_move(state, move)
        moves.append(i)
        result = _solve(new_state, depth - 1, moves, memo)
        moves.pop()
        if result:
            return result

def solve(state):
    memo = {}
    state = tuple(state)
    for depth in range(100):
        print(depth)
        moves = _solve(state, depth, [], memo)
        if moves:
            return moves

def main():
    args = sys.argv[1:]
    if len(args) != 1:
        print('Usage: python rubix.py STATE')
        return
    state = args[0]
    print(state)
    moves = solve(state)
    print(', '.join(MOVE_NAMES[i] for i in moves))

if __name__ == '__main__':
    main()