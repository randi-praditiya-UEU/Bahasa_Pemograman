def faktorial(x):
     if x == 1:
         return 1
     else:
         return x * faktorial(x-1)
print(faktorial(5))