import sys
import re

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def balanced(line, openings = 0):
  if line == "": return True
  if re.match(r"^[a-z :]+$", line): return True

  m = re.search(r"(?<!:)\(", line)

  if m:
    pre = line[:m.start()]
    post = line[m.end():]
    return balanced(pre, 0) & balanced(post, openings + 1)

  return False

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))

