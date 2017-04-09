from parse import parse
from cnf import result
import sys

a = sys.argv
if len(a)<2 :
  print "Wrong cnf format : python main.py < {polish notation}"
b = parse(a[1].split())
print(b)
c = result(b)

