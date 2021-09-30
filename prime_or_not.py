x = int(input("Enter a number: "))
if x > 1:
   for n in range(2, x):
      if (x % n) == 0:
         print(x, "is not prime")
         
         break
   else:
      print(x, "is a prime number")
else:
    print(x, "is not prime number")