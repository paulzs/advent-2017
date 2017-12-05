data = open('input.txt')

jump_list = []

for line in data:
  jump_list.append(int(''.join(line.split())))

at_index = 0
jump_count = 0

while at_index < len(jump_list):
  curr_index = at_index
  jump_val = jump_list[at_index]
  at_index += jump_val
  jump_list[curr_index] += 1
  jump_count += 1

print(jump_count)