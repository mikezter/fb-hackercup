import sys

line = sys.stdin.readline()

def score(line):
  counts = dict.fromkeys(list(line), 0)
  for c in line:
    counts[c] = counts[c] + 1

  return counts["A"]

line = sys.stdin.readline().rstrip()
while line:
  print list(line)
  print score(line)
  line = sys.stdin.readline().rstrip()

