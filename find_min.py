import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def buildlist(a, b, c, d, knowns):
  m = list(knowns)
  m[0] = a
  for i in range(knowns - 1):
    m[i + 1] = (b * m[i] + c) % r

  return m

for i in range(cases):
  length, knowns = readline().split()
  a, b, c, d = readline().split()
  print buildlist(a, b, c, d, knowns)
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))
