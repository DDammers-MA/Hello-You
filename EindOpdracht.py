import sys

print("hoe heet je? ")
naam = input()
print("hoi " + naam)
print("je moet vluchten je kunt naar 2 landen")
print("type D voor Duitsland en F voor Frankrijk ")
antwoord = input()
if antwoord == "D":
    print ("oke hoe wil je gaan reizen ?")
else:
    print("oke goed hoe wil je gaan reizen ?")

print("je kan kiezen tussen lopen of met de auto welke kiez je ?")
print("type L voor lopen en A voor auto")
antwoord2 = input()
if antwoord2 == "L":
    print("goed dat je wil lopen maaar het gaat wel lang duuren")
else:
    print("oke goed nu nog opzoek naar een auto")

    print("er staat een auto om de hoek maar er staan bewaakers naast")
    print("ga je wachten tot de bewaarkers weg gaan of ga je ze confronteren ?")
    print("voor wachten type W voor confronteren type C")
    inp = input()
    if inp == "W":
        print("na een paar uur wachten lopen de soldaten weg van de auto ")
        print("je rit snel weg en niemand heeft het door en rijd vijlig de grens over")
    else:
        print("ooh nee je ben opgepackt en de gevengenis gegooit")
    sys.exit()

print("na uren lopen heb je dorst")
print("je komt een winkeltje tegen ga je iets kopen of loop je door?")
print("type K voor kopen en voor door lopen DL")
inp = input()
if inp == "DL":
 print("het blijkt dat je geen water heb gedronken en uitgedrocht ben")
 print("hellaas heb je niert de kracht om door te lopen en gaat langzaam dood")

else:
 print("water kost 1,90 en je hebt maar 1,50 op op je")
 print("je hebt de keuze om het te stelen of weg te gaan")
 print("type S voor stelen en W voor weg gaan")
 inp2 = input()
if inp2 == "S":
  print("de medewerker heeft de politie gebeld en word nu opgejaacht")
else:
     print("je bent wegggaan van de winkel.")
     print("een van de medewerkers heb medelijden voor je en geeft je en flesje met water")
     print("je bedankt de medewerker en gaat snel weer op pad")
     print("je komt er acher dat je zonder passpordt niet het land binnen kan")
     print("je moet een smokkelaar zien te vinden om een passport te krijgen na dagen zoeken vindt je er een")
     print("maar die vraag veel geld voor zo'n passport en zoveel heb je niet")
     print("je weet waar de man slaapt je kan een paspoort van hem stelen of je kan geld verdienen")
     print("type S voor stelen en V voor geld verdienemn")
     pasport = input()
if pasport == "S":
    print("je sluipt stieken zijn kamer binnen en pak de pasport")
    print("je vind een auto en rijd snel weg voordsat hij wakker word")
    print("na een paar uur rijden kom je bij de grens aan en word gekontroleerd")
    print("maar na een paar vragen geantwoord laten ze je rustif door de grens")

else:
    print("na maanden werken in een bar heb je eindelijk 5000$ zien te sparen")
    print("maar de smokkelaar zegt opeen dat het 10,000$ gaat kosten")
    print("je besluit om de paspoort te stelen al hij slaapt")
    print ("na de smokkelaar gaat slapen steel je de paspoort")
    print("helaas word de smokkelaar wakken en gaat achter je aan met zijn gang")
    print("je heb de kans om op een bood te springen of snel in een auto te gaan welke kiezen je")
    print("type B voor bood en A voor auto ")
    antwoord3 = input()
    if antwoord3 == "B":
        print("je bent nog net snel genoeg om de bood te pakken en de smokkelaar te onwijken")
        print("na een paar dagen reizen kom je aan en kan je je nieuwe leven beginnen")
        print("maar je kan natuurlijk niet gelijk beginnen")

        print("na")

    else:
        print("je pak een auto en rijd weg, maar hellaas zit de sokkelaar en zijn gang achter je aan")
        print("je ziet een wapen op de achterbank en shiet op de smokkellar")
        print("omdat je naar achtern schiet heb je geen zicht op het verkeer en komt in een botsing")
        print("je heb geluk gehad en ben on beschadig en moet op voet veder ")
        print("na 2 dagen op voet kom je eindelijk de grens over en kan je je nieuwe leven beginnen")
        print("je moet natuurlijk eers werk zien te vinden om ergens te gaan wonen")
        print("je kan werken bij een supermarkt")
        print("ga je het doen of niet")
        print ("type J voor ja en N voor nee")
        supermarkt = input()
        if supermarkt == "J":
            print("goed dat je wil werken je baas zeg dat je meteen kan beginnen als vakkenvuller")
        else:
            print("jammer dan moet je een ander manier om geld te krijgen")
            print("na maanden op de straat wonen en niks te eten verhonger je ")


