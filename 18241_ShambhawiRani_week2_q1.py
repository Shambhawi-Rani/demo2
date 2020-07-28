import math

n = int(input("N = "))
k = int(input("K = "))

if 1<=n & n<=k & k<=10e5:
  result = (math.factorial(k)/math.factorial(k-n)) % (10**9+7)
  print(int(result))
else:
  print("Input Error")