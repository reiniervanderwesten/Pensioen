print("Wat is je leeftijd?")
leeftijd=int(input("Voer het aantal jaren in: "))
print("Wat is je werkstatuut?")
werkstatuut=input("voer in: medewerker, zelfstandige of ambtenaar: ")

def pensioenstatus(a,b):    #bij deze functie horen de 2 argumenten leeftijd en werkstatuut. Zie hiervoor regel 32.
    if a<65:        # De situatie dat iemand beneden de pensioengerechtigde leeftijd zit. 
        D1=False    # D1 is een boleaanse variable en is 'False' als iemand niet pensioengerechtigd is. 'True' als iemand recht heeft op pensioen.
        D2= 65-a    # als D1 'False' is, d.w.z. er is geen recht op pensioen, dan geeft D2 het aantal jaren dat iemand nog moet werken. 
    if 70>a>=65 and b=="medewerker":    # regel 10 t/m 18 geven de situatie weer dat iemand valt binnen het lage pensioen van onder de 70, binnen 1 van de beroepsgroepen.
        D1=True
        D2=350      # bij een recht op pensioen geeft D2 het pensioenbedrag weer. 
    if 70>a>=65 and b== "zelfstandige":
        D1=True
        D2=300
    if 70>a>=65 and b=="ambtenaar":
        D1=True
        D2=370
    if  a>=70 and b=="medewerker":  # regel 19 t/m 27 geven de situatie weer dat iemand boven de 70 is en recht heeft op het 'hoge' pensioen binnen 1 van de beroepsgroepen.
        D1=True
        D2=370
    if  a>=70 and b=="zelfstandige":
        D1=True
        D2=315
    if  a>=70 and b=="ambtenaar":
        D1=True
        D2=395
    
    uitvoer=[D1,D2]
    return uitvoer

uitkomst=pensioenstatus(leeftijd, werkstatuut)

recht_op_pensioen=uitkomst[0]       # recht_op_pensioen is gelijk aan D1
pensionado_vs_arbeider=uitkomst[1]  # pensionado-vs_arbeider is gelijk aan D2.

if recht_op_pensioen==False:
    print(f"Van werken wordt je gelukkig, je mag nog {pensionado_vs_arbeider} jaren genieten van je baan")
if recht_op_pensioen==True:
    print(f"Je krijgt $ {pensionado_vs_arbeider}")