import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def buildlist(a, b, c, d, knowns):
  m = []
  m.append(a)
  for i in range(knowns - 1):
    m.append((b * m[i] + c) % r)

  return m

for i in range(cases):
  length, knowns = [int(i) for i in readline().split()]
  a, b, c, d = [int(i) for i in readline().split()]
  print buildlist(a, b, c, d, knowns)
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))
