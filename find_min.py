import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def buildlist(a, b, c, d, length, knowns):
  l = list(length)
  for i in range(knowns):
    if i == 0: l[i] = a



for i in range(cases):
  length, knowns = readline().split()
  a, b, c, d = readline().split()
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))
