def decorator(f):
  print("After function")
  def func(a,b,c):
    f(a,b,c)
    print("Before function")
  return func

@decorator
def sumMult(a,b,c):
  return print((a + b) * c)

sumMult(5,4,10)