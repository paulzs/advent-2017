def day_6_part_one():
  mem = open('input.txt')
  mem_list = mem.readline().split()
  mem_list = list(map(int, mem_list))
  states = []
  states.append(mem_list)
  reallocate_count = 0
  block_list = reallocate(list(mem_list))
  while block_list not in states:
    states.append(block_list)
    reallocate_count += 1
    block_list = reallocate(list(block_list))
  reallocate_count += 1
  print(reallocate_count)

def reallocate(block_list):
  b_list = block_list
  max_val = max(b_list)
  max_index = b_list.index(max_val)
  next_index = max_index + 1
  b_list[max_index] = 0
  while max_val > 0:
    if next_index >= len(b_list):
      next_index = 0
    b_list[next_index] += 1
    next_index += 1
    max_val -= 1
  return b_list

day_6_part_one()