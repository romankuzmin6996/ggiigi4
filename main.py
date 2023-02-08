from math import *
def funkcija(skaitlis,burts):
  rex = 0
  if burts == "d":
    rez = degrees(skaitlis)
  else:
    rez = radians(skaitlis)
  return rez
skaitlis = int(input("Ievadi skaitli:"))
burts = input("Ievadi burtu (r/d): ")
print("Rezultats = ", funkcija(skaitlis, burts))