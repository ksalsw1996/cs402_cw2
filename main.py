from parse import parse
from printer import polish, inflix
from cnf import result
from valid import valid
import sys

a = sys.argv

if len(a)<2 :
  print "Wrong cnf format"

b = parse(a[1].split())
c = result(b)

print(polish(c))
d = inflix(c)
print(d)

if(valid(d)):
  print "Valid"

else :
  print "Not Valid"
