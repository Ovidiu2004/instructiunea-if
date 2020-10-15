n1=int(input("Introduceti numarul curen n1="))
p1=int(input("Introduceti punctajul"))
n2=int(input("Introduceti numarul curent n2="))
p2=int(input("Introduceti punctajul"))
n3=int(input("Introduceti numarul curent n3="))
p3=int(input("Introduceti punctajul"))
if(p1>p2)and(p1>p3) : 
  print("n1")
if(p2>p1)and(p2>p3) :
  print("n2")
if(p3>p1)and(p3>p2) :
  print("n3")
if(p1==p2)and(p1>p3)and(p2>p3):
  print("n1 and n2 acelasi punctaj")
if(p1==p3)and(p1>p2)and(p3>p2):
  print("n1 and n2 acelasi punctaj")
if(p2==p3)and(p2>p3)and(p3>p1):
  print("n2 and n3 acelasi punctaj")