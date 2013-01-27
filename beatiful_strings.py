import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def linelist(line):
  return filter(lambda c: c.isalpha(), list(line.lower()))

def counts(line):
  counts = dict.fromkeys(line, 0)
  for c in line:
    counts[c] = counts[c] + 1

  counts = counts.values()
  counts.sort()
  counts.reverse()
  return counts

def score(charcounts):
  big = 26
  score = 0

  for i in charcounts:
    score = score + big
    big = big - 1

  return score


line = readline()
while line:
  print score(counts(linelist(line)))
  line = readline()

