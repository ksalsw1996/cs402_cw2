not_important = ['|', '(', ')'] 
def valid(a):
  prop = a.split('&')
  for clause in prop :
    if not valid_cl(clause) :
      return 0
  return 1

def valid_cl(clause) :
  list = []
  atoms = clause.split()
  while atoms :
    a=atoms.pop(0)
    if a not in not_important :
      if a == '-' :
        b=atoms.pop(0)
        if b in list : return 1
        else : list.append(a+b)
      else :
        b = '-'+a
        if b in list : return 1
        else : list.append(a)
  return 0
