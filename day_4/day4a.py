passphrases = open('input.txt')

count = 0

for line in passphrases:
  foo = line.split()
  unique = list(set(foo))
  if len(foo) == len(unique):
    count += 1

print(count)