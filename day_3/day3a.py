import math

square = 289326

x = 1

while (square - pow(x,2)) > 0:
  x += 2

lower_right = pow(x,2)
bottom_mid = lower_right - int(x/2)
left_mid = bottom_mid - x + 1
top_mid = left_mid - x + 1
right_mid = top_mid - x + 1

mid_dist = int(x/2)

diff_list = [abs(square-bottom_mid),
             abs(square-left_mid),
             abs(square-top_mid),
             abs(square-right_mid)]

distance = min(diff_list) + mid_dist

print(distance)