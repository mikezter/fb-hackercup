import sys
import re

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def balanced(line):
  if line == "": return True
  if re.match("^[a-z :]+$", line): return True

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))

