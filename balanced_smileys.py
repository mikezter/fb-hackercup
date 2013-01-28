import sys

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def invalid(c):
  return ord(c) not in range(97, 110) or c not in [' ', ':', '(', ')']

def balanced(line):
  was_colon = False
  smileys = 0
  frownys = 0
  pairs = 0

  for c in list(line):
    if invalid(c): return False
    if was_colon:
      if c == '(': frownys += 1
      if c == ')': smileys += 1
    else:
      if c == '(': pairs += 1
      if c == ')': pairs -= 1

    if pairs == -1:
      if frownys > 0:
        frownys -= 1
        pairs += 1
      else:
        return False

    was_colon = c == ':'

  if pairs > 0: return pairs == smileys
  return pairs == 0

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))

