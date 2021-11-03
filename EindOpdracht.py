import sys
import time


print("hoe heet je? ")
naam = input()
print("hoi " + naam)
print("dit spel is hoofletter gevoelig")
print("dat houd in ald je een keuzen moet maken kan je alleen met hoofletter")
print("anders werk het niet")
print("je moet vluchten je kunt naar 2 landen")
print("welke kiez je type D voor Duitsland en F voor Frankrijk ")
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
        time.sleep(2)
        print("je rit snel weg en niemand heeft het door")
        time.sleep(2)
        print("tot dat je door de bewaking van je dorp moet rijden")
        time.sleep(2)
        print("ze houden je aan om een paar vragen te stellen.")
        time.sleep(2)
        print("je heb de kans om snel door te rijden of de vragen te benatworden")
        time.sleep(2)
        print("wat ga je doen ?")
        time.sleep(2)
        print("type D voor door rijden en S voor vragen beantwoorden")
        keuzen = input()
        if keuzen == "D":
            print("SHIT, je gaan versnellen en de bewaketr zitten nu achter je aan")
            time.sleep(2)
            print("na een paar minuten beginen ze ook nog eens op je te schieten")
            time.sleep(2)
            print("je ziet in de dashboardkastje een geweer ligen")
            time.sleep(2)
            print("ga je terug schieten of blijf je rijden ?")
            time.sleep(2)
            print("type SC voor schieten en R voor rijden")
            geweer = input()
            if geweer == "SC":
                print("je begint terug te schieten en schake;t een paar autos uit")
                time.sleep(2)
                print("na een uur rijden ben je veilig alleen over de grens gekomen")
                time.sleep(2)
                print("je moet de avond overnachten")
                time.sleep(2)
                print("dat kanje doen door in een tent te slapen of door te blijven lopen")
                print("type Tvoor tent en L voor lopen")
                nacht = input()
                if nacht == "T":
                    print("je bent gaan slapen in een tent om de nacht door te komen")
                    print("maar de politie heeft je gezien zonder legitimatie en heeft je in de gevangenis gegooit")
                else:
                    print("je bent door gaan lopen en heb een veilige slaap plek gevonden")
                    time.sleep(2)
                    print("je bent eidelijk veilig aan gekomen in een dorp je moet nu wel werk zien te vinden")
                    print("na een paar solicitatie heb je de keuzen o te werken in een supermartk of als een Concierge")
                    time.sleep(2)
                    print("welke kiez je ?")
                    print("S voor supermarkt en C voor Concierge")
                    werk2 = input()
                    if werk2 == "S":
                        print("je baas zegt dat je meteen kan beginnen ")
                        print("na jaren werken heb je eindelijk genoeg om je familie te inmporter")
                        time.sleep(2)
                        print("maar de vraag is ga je het ook doen. je bent namelijk al jaren alleen")
                        print("type I voor het inporteren en N voor het niet doen")
                        inporteren = input()
                        if inporteren == "I":
                            print("je bent super blij dat je je familie weer a=kan zien en je kan niet wachten tot je weer samen bent")
                        else:
                            print("je bent niet van plan om samen met je familie te zijn en besluit om ze niet te inporteren")
                            print("en dat toch na 5 jaar ben je enzaam en ongelukig en endigt in je dood")

                    else:
                        print("nou je moet eerst wachten tot je in het systeem staat voor dat je kan beginnen")
                        print("na 2 weeken wachten kan je eindelijk beginnen")
                        time.sleep(2)
                        print("je heb genoeg geld om samen te zijn met je famile")
                        print("ga je ze inporteren of niet")
                        inporteren2 = input()
                        if inporteren2 == "ja":
                            print("jij en je familie zijn erg gelukig dat jullie erkaar weer kunnen zien en leeft een gelukig leven")
                        else:
                            print("je heb geen intresen om ze te inporteren en ben voor de rest van je leven alleen")


            else:
                print("je blijft gewoon te rijden")
                print("er blijf op je geschoten")
                time.sleep(2)
                print("en na een paar schoten word je band lek geschoot")
                print("je kanlt tegen een boom aan en word de gevangenis in gegooit")
            
        else:
            print("na het beantwoorden van de vragen denken ze dat je het land probeert uit te gaan en gooien je in de gevangenis")

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
     print("neem je het flesje water aan of niet")
     water = input()
     if water == "ja":
         print("je bedankt de medewerker en gaat snel weer op pad")
     else:
        print("je droogt uit en gaat dood")
        

     time.sleep(4)
     print("je komt er acher dat je zonder passpordt niet het land binnen kan")
     print("je moet een smokkelaar zien te vinden om een passport te krijgen na dagen zoeken vindt je er een")
     time.sleep(4)
     print("maar die vraag veel geld voor zo'n passport en zoveel heb je niet")
     print("je weet waar de man slaapt je kan een paspoort van hem stelen of je kan geld verdienen")
     print("type S voor stelen en V voor geld verdienemn")
     pasport = input()
if pasport == "S":
    print("je sluipt stieken zijn kamer binnen en pak de pasport")
    time.sleep(1)
    print("je vind een auto en rijd snel weg voordsat hij wakker word")
    print("na een paar uur rijden kom je bij de grens aan en word gekontroleerd")
    print("maar na een paar vragen geantwoord laten ze je rustif door de grens")

else:
    print("na maanden werken in een bar heb je eindelijk 5000$ zien te sparen")
    time.sleep(1)
    print("maar de smokkelaar zegt opeen dat het 10,000$ gaat kosten")
    time.sleep(1)
    print("je besluit om de paspoort te stelen al hij slaapt")
    print ("na de smokkelaar gaat slapen steel je de paspoort")
    time.sleep(1)
    print("helaas word de smokkelaar wakken en gaat achter je aan met zijn gang")
    print("je heb de kans om op een bood te springen of snel in een auto te gaan welke kiezen je")
    print("type B voor bood en A voor auto ")
    antwoord3 = input()
    if antwoord3 == "B":
        print("je bent nog net snel genoeg om de bood te pakken en de smokkelaar te onwijken")
        print("na een paar dagen reizen kom je aan en kan je je nieuwe leven beginnen")
        time.sleep(1)
        print("maar je kan natuurlijk niet gelijk beginnen")

        print("je moet natuurlijk een baan zien te krijgen zodat je je familie het land binnen kan laten")

        print("na een paar solicitaties heb je eindelijk de keus om een baan te krijgen ")
        print("je heb de keuzen tussenwerken in een supermakrt of een autoshop")
        print("welke kiez je ?")
        werk = input()
        if werk == "supermark":
            print("je baas zegt dat je meteen die maandag kan beginnen")
        else:
            print("je moet eerst 2 weekend wachten tot je geregestreert bent in het bedrijf")
        print("na maanden lang werken heb je eindelijk de kans om je familie te inporteren")
        print("ga je het doen of niet")
        print("J voor j en N voor nee ")
        kans = input()
        if kans == "J":
            print("na een lanfe wacht kan je eindelijk je familie op halen bij het vliegveld")
            print("na het ophalen van je familie rij je met hun naar je huis")
              
    
        else:
            print("na het bespreken met ja familie zijn ze zeer teleurgesteld in je en hoefen je niet meer te zien")



    else:
        print("je pak een auto en rijd weg, maar hellaas zit de sokkelaar en zijn gang achter je aan")
        time.sleep(1)
        print("je ziet een wapen op de achterbank en shiet op de smokkellar")
        print("omdat je naar achtern schiet heb je geen zicht op het verkeer en komt in een botsing")
        time.sleep(1)
        print("je heb geluk gehad en ben on beschadig en moet op voet veder ")
        print("na 2 dagen op voet kom je eindelijk de grens over en kan je je nieuwe leven beginnen")
        time.sleep(1)
        print("je moet natuurlijk eers werk zien te vinden om ergens te gaan wonen")
        print("je kan werken bij een supermarkt")
        time.sleep(1)
        print("ga je het doen of niet")
        print ("type J voor ja en N voor nee")
        supermarkt = input()
        if supermarkt == "J":
            print("goed dat je wil werken je baas zeg dat je meteen kan beginnen als vakkenvuller")
            print("na maanden lang werken kan je eidnelijk een wat grooter huis/ appartement te kopen")
            print("H voor huis en A voor appertement")
            huis = input()
            if huis == "H":
                print("goed zo nu heb je een huis nu alleen nog zorgen dat je je familie het land binnen ziet te krijgen")
                print("na maanden werken heb je genoeg geld om je familie het land in te krijgen")
                time.sleep(2)
                print("na dagen nadenken of je familie wel veilig het land binnen kunnen komen")
                print("krijg je een telefontje met dat ze veilig op het vliegveld zijn")
                time.sleep(2)
                print("ga je ze ophalen of niet")
                print("ja of nee")
                ophalen = input()
                if ophalen == "ja":
                    print("bij het vliegveld ren je naar ze toe en on arm je ze en leeft geluk in een veilig land")
                else:
                    print("na een paar uur wachten beld je familie je op en vraag zich af waar je bent")
                    print("je verteld ze dat je zoganaamt had verslapen en dat je er nu aan kom ")
            

            else:
                print("een appartement is niet heel handig voor een familie")
                print("na nog een paar maanden werken heb je weer genoe geld om je familie het land in te krijgen")
                time.sleep(2)
                print("je heb de kans om het te doen of niet")
                print("type D voor doen of N voor niet doen ")
                totodile = input()
                if totodile == "D":
                    print("je familie is super blij om je weer te kunnen zien")
                    print("na dagen wachten of je familie veleig de grens over gegaan is krijg je een beletje krijg en je familie op het vleigveld zijn")
                    print("nu leeft je gelukig in een veilig land samen met je familie")
                else:
                    print("na jaren zonder je familie ben je zo eenzam dat je in een depressei valt en lijd tot je dood")                 


  
        else:
            print("jammer dan moet je een ander manier om geld te krijgen")
            print("na maanden op de straat wonen en niks te eten verhonger je ")
        
        