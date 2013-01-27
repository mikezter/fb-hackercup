import sys

line = sys.stdin.readline()

def readline():
  return sys.stdin.readline().rstrip()

def linelist(line):
  list(line.lower(), 0).filter(isalpha)



def counts(line):
  counts = linelist(line)
  for c in line:
    counts[c] = counts[c] + 1

  return counts

line = readline()
while line:
  print list(line)
  print counts(line)
  line = readline()

