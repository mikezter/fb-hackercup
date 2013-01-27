import sys

line = sys.stdin.readline()

def readline():
  line = sys.stdin.readline().rstrip().lower()

def counts(line):
  counts = dict.fromkeys(list(line), 0)
  for c in line:
    counts[c] = counts[c] + 1

  return counts

line = readline()
while line:
  print list(line)
  print counts(line)
  line = readline()

