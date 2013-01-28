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

def nextlist(m):
  l = list(m)
  l.sort()
  new = l[0] - 1
  if new < 0:
    for i in l:
      new = i + 1
      if new not in l: break

  del(m[0])
  m.append(new)
  return m


for i in range(cases):
  n, k = [int(j) for j in readline().split()]
  a, b, c, r = [int(j) for j in readline().split()]

  memo = buildlist(a, b, c, r, k)

  for x in range(n - k):
    print memo
    memo = nextlist(memo)

  print "Case #" + str(i + 1) + ": " + str(memo[-1])
