print("--------------------------------------------------")
print("**** Seconden naar uren, minuten en seconden. ****")
print("--------------------------------------------------\n")

# Hoeveel seconden moeten we omvormen?
# We encapsuleren deze code in int() omdat we anders een string krijgen.
totaal_seconden = int(input("Geef het aantal seconden in dat u wilt omvormen: "))

# %d vraagt om een digit (integer).
print("We gaan %d seconden omvormen.\n" % totaal_seconden)

# Bereken het totaal aantal uren.
uren = totaal_seconden // 3600
seconden = totaal_seconden % 3600

# Berekene het totaal aantal minuten.
minuten = seconden // 60
seconden = seconden % 60

# Laat het resultaat zien.
print("%d uur, %d minuten en %d seconden.\n" % (uren, minuten, seconden))

# Laat de totalen zien.
print("Totaal uren: %d" % (totaal_seconden // 3600))
print("Totaal minuten: %d" % (totaal_seconden // 60))
print("Totaal seconden: %d\n" % (totaal_seconden))

# End
input("Druk op een toets om programma te beindigen.")