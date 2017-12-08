data = open('input.txt')

registers = {}
line_count = 0
max_val = 0

for line in data:
  line_count += 1
  line = line.strip().split()
  register = line[0]
  modifier = line[1]
  amount = int(line[2])
  comparator = line[-3]
  comparison = line[-2]
  comp_amount = int(line[-1])

  result = False
  if comparator not in registers:
    registers[comparator] = 0
  if register not in registers:
    registers[register] = 0
  if comparison == '==':
    result = registers[comparator] == comp_amount
  elif comparison == '<=':
    result = registers[comparator] <= comp_amount
  elif comparison == '>=':
    result = registers[comparator] >= comp_amount
  elif comparison == '<':
    result = registers[comparator] < comp_amount
  elif comparison == '>':
    result = registers[comparator] > comp_amount
  elif comparison == '!=':
    result = registers[comparator] != comp_amount

  if result:
    if modifier == 'inc':
      registers[register] += amount
    else:
      registers[register] -= amount

  current_max = max(registers.values())
  if current_max > max_val:
    max_val = current_max

print(max_val)