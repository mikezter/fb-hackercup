import sys
import re

cases = int(sys.stdin.readline())

def readline():
  return sys.stdin.readline().rstrip()

def balanced(line, openings):
  if line == "": return True
  if re.match(r"^[a-z :]+$", line): return True

  m = re.match(r"\(", line)
  if m:
    pre = line[:m.start()]
    post = line[m.end():]
    print "Pre: " + pre
    print "Post: " + post
    return balanced(pre, openings) & balanced(post, openings + 1)

  m = re.match(r"\)", line)
  if m:
    pre = line[:m.start()]
    post = line[m.end():]
    print "Pre: " + pre
    print "Post: " + post
    return balanced(pre, openings - 1) & balanced(post, openings)

  return openings == 0

def answer(answer):
  if answer: return "YES"
  return "NO"

for i in range(cases):
  line = readline()
  print line
  print "Case #" + str(i + 1) + ": " + answer(balanced(line, 0))
  print

