import sys

line = sys.stdin.readline()

def readline():
  return sys.stdin.readline().rstrip()

def linelist(line):
  filter(isalpha, list(line.lower()))



def counts(line):
  counts = dict.fromkeys(linelist(line), 0)
  for c in line:
    counts[c] = counts[c] + 1

  return counts

line = readline()
while line:
  print list(line)
  print counts(line)
  line = readline()

