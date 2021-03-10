#define the initial numbers
a=1
b=1
#provide term number choice
n=int(input("the number of terms:"))
#circulate the accumulation
for m in the range(2,n):
  c=a+b
  print(c)
  a=b
  b=c
