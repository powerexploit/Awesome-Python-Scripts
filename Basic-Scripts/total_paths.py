
# Question: Number of total ways to move from Point A (top left of the grid) to Point B (bottom right of the grid) in a square grid assuming that you can only move down and right.

# Example:
# 20 x 20 matrix, 20 right and 20 down moves ie 40 moves
# order of these steps doesnt matter
# Therefore the answer is 40 (total moves) choose 20

# grid size can be changed for any N X N matrix.
grid_size = 20
# shape of matrix
total_moves = grid_size * 2
total_ways_numerator = 1
total_ways_denominator = 1
for i in range(grid_size+1,total_moves+1,1):
    total_ways_numerator *= i
for j in range(1,grid_size+1,1):
    total_ways_denominator *= j

total_ways = total_ways_numerator/ total_ways_denominator
print(total_ways)
print(total_ways_numerator, total_ways_denominator)
