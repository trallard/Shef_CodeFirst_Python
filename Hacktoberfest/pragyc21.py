def add(a, b):
  print 'ADDING %d + %d' % (a, b)
  return a + b

def subtract(a, b):
  print 'SUBTRACTING %d - %d' % (a, b)
  return a - b

def multiply(a, b):
  print 'MULTIPLYING %d * %d' % (a, b)
  return a * b

def devide(a, b):
  print 'DEVIDING %d * %d' % (a, b)
  return a / b

age = add(15, 5)
height = subtract(18, 3)
weight = multiply(100, 3)
iq = devide(100, 20)

print 'age: %d, height: %d, weight: %d, iq: %d' % (age, height, weight, iq)

#puzzle for extra credit
what = add(age, subtract(height, multiply(weight, devide(iq, 2))))
print "That becomes: ", what, "Can you do it by hand?"
