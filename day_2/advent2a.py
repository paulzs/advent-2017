data = open('input.txt')

diff_list = []

for line in data:
  tokens = line.split()
  max_tok = -1
  min_tok = -1
  for tok in tokens:
    if (int(tok) > int(max_tok)) or int(max_tok) == -1:
      max_tok = int(tok)
    if (int(tok) < int(min_tok)) or int(min_tok) == -1:
      min_tok = int(tok)
  diff = int(max_tok) - int(min_tok)
  diff_list.append(diff)

print(sum(diff_list))