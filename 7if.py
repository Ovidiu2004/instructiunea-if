a=int(input("dati 1 numar"))
b=int(input("dati 2 numar"))
c=int(input("dati 3 numar"))
if a>=0 and b>=0 and c>=0:
    if b>c:
        print(b)
    if b==c:
         print(b,c)
    else:
        print(c)
if a<0 or b<0 or c<0:
    print(a+b)