passphrases = open('input.txt')

count = 0

for line in passphrases:
  foo = line.split()
  for i in range(len(foo)):
    foo[i] = ''.join(sorted(foo[i]))
  unique = list(set(foo))
  if len(foo) == len(unique):
    count += 1

print(count)