import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def buildlist(a, b, c, r, k):
  m = []
  m.append(a)
  for i in range(k - 1):
    m.append((b * m[i] + c) % r)

  return m

for i in range(cases):
  n, k = [int(j) for j in readline().split()]
  a, b, c, r = [int(j) for j in readline().split()]

  print buildlist(a, b, c, r, k)
  print "Case #" + str(i + 1) + ": "
