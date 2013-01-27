import sys

line = sys.stdin.readline()

def counts(line):
  counts = dict.fromkeys(list(line), 0)
  for c in line:
    counts[c] = counts[c] + 1

  return counts

line = sys.stdin.readline().rstrip()
while line:
  print list(line)
  print counts(line)
  line = sys.stdin.readline().rstrip()

