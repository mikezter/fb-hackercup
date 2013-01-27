import sys
import re

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def balanced(line):
  if line == "": return True
  if re.match(r"^[a-z :]+$", line): return True

  m = re.search(r"(?<!:)\(.*\)", line)

  if m:
    pre = line[:m.start()]
    post = line[m.end():]
    inner = line[m.start() + 1:m.end() - 1]
  #  print "Pre: " + pre
  #  print "Inner: " + inner
  #  print "Post: " + post
    return balanced(pre) & balanced(inner) & balanced(post)

  if re.search(r"(?<!:)\)", line): return False

  return False

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print "Case #" + str(i + 1) + ": " + answer(balanced(line))

