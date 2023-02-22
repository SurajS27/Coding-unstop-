a= input()
if (a[0]=='a' or a[0]=='c' or a[0]=='e' or a[0]=='g' ):
    s= 1
else:
    s=0
c = a[1]
d = int(c)
b = d+ s 
if (b%2==0):
    print("Black")
else:
    print("White")
