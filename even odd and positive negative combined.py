#even/odd and positive/negatuve combined.
num=int(input("enter the number"))
if num%2==0 and num>0 :
  print("even and positive")
elif num%2==0 and num<0 :
  print("even and negative")
elif num%2!=0 and num>0 :
  print("odd and positive")
elif num%2!=0 and num<0:
  print("odd and negative")
else:
  print("the number is zero")
  enter the number-42
even and negative
