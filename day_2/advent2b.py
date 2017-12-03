data = open('input.txt')

diff_list = []

for line in data:
  tokens = line.split()
  for i in range(0,len(tokens)):
    for j in range(0,len(tokens)):
      if i==j:
        continue
      else:
        if int(tokens[i]) % int(tokens[j]) == 0:
          diff_list.append(int(tokens[i]) / int(tokens[j]))

print(sum(diff_list))