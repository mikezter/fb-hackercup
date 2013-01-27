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
  return counts

def score(charcounts):
  charcounts.sort()
  charcounts.reverse()

  big = 26
  score = 0

  for i in charcounts:
    score = score + big
    big = big - 1

  return score


for i in range(1, cases):
  line = readline()
  print "Case #" + str(i) + ": " + str(score(counts(linelist(line))))

