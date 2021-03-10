a="hello "
b="world"
a+b

a=280502
b=190784
c=100321
d=abs(a-c)
e=abs(a-b)
if d<e:
  print("e is greater")
  elif d==e:
    print("d and e are the same")
    else:
      print("d is greater")
      
X=False
Y=True
Z=(X and not Y) or (Y and not X)
print(Z)
W=(X!=Y)
if Z==W:
  print("W and Z are always the same, no matter the values of X and Y.")
