bin_op = ['&','|']
uni_op = ['-']

def polish(a):
  b = a[0]
  if b in bin_op :
    return b + " " + polish(a[1]) + polish(a[2])
  elif b in uni_op :
    return b + " " + polish(a[1])
  else :
    return b + " "

def inflix(a):
  b = a[0]
  if b == '&' :
    if a[1][0] == '&':
      return inflix(a[1]) + " & " + inflix(a[2])
    else :
      return "( " + inflix(a[1]) + ") " + b + " ( " + inflix(a[2]) + ")"
  elif b == '|' :
    return inflix(a[1]) + "| " + inflix(a[2]) 
  elif b == '-' :
    return b + " " + inflix(a[1])
  else :
    return b + " "
