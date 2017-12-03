# I cheated using https://oeis.org/A141481, but here's a working python solution:

target = 289326

coords = [(1, 0), (1, -1), (0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1)]

x = y = dx = 0
dy = -1
grid = {}

while True:
  total = 0
  for offset in coords:
    ox, oy = offset
    if (x+ox, y+oy) in grid:
      total += grid[(x+ox, y+oy)]
  if total > target:
    print(total)
    break
  if (x, y) == (0, 0):
    grid[(0, 0)] = 1
  else:
    grid[(x, y)] = total
  if (x == y) or (x < 0 and x == -y) or (x > 0 and x == 1-y):
    dx, dy = -dy, dx
  x, y = x+dx, y+dy