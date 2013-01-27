import sys

line = sys.stdin.readline()

def score(line):
  dict.fromkeys(list(line), 0)

line = sys.stdin.readline().rstrip()
while line:
  print list(line)
  print score(line)
  line = sys.stdin.readline().rstrip()

