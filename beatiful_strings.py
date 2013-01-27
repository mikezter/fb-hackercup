import sys

line = sys.stdin.readline()

def readline():
  return sys.stdin.readline().rstrip()

def linelist(line):
  return filter(lambda c: c.isalpha(), list(line.lower()))

def counts(line):
  counts = dict.fromkeys(line, 0)
  for c in line:
    counts[c] = counts[c] + 1

  return counts

line = readline()
while line:
  print list(line)
  print counts(linelist(line))
  line = readline()

