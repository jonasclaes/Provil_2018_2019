# Zoo kassa
from typing import List

print("---------------------------------------------")
print("***************** ZOO KASSA *****************")
print("---------------------------------------------")

# 0: prijs kind
# 1: prijs volwassene
prijslijst: List[float] = [8.5, 16.5]

print("Huidig tarief:")
print("\t\tKind: " + str(prijslijst[0]))
print("\t\tVolwassene: " + str(prijslijst[1]))
print("---------------------------------------------")

numKids = int(input("Aantal kinderen? "))
numAdult = int(input("Aantal volwassenen? "))
nameFamily = input("Familienaam? ")
print("---------------------------------------------")

print("De totale prijs zal %s euro bedragen." % (str((numKids * prijslijst[0]) + (numAdult * prijslijst[1]))))
print("Bedankt voor uw bezoek familie %s" % nameFamily.title())
