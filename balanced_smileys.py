import sys
import re

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def balanced(line):
  was_colon = False
  smileys = 0
  frownys = 0
  pairs = 0
  for c in list(line):
    if was_colon:
      if c == '(': frownys += 1
      if c == ')': smileys += 1
    else:
      if c == '(': pairs += 1
      if c == ')': pairs -= 1

    if pairs < 0: return False

    was_colon = c == ':'

  return pairs == 0

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print line
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))
  print

