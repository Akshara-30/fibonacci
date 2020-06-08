n=int(input("enter the value:"))
a=0
b=1
sum=0
if (n<=0):
 print("sorry enter positive number")
else:
 print(a,"\t", b ,"\t",end="")
 for x in range(2,n):
    sum=a+b
    print(sum,"\t",end="")
    a=b
    b=sum
