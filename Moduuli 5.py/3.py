lukuStr = input("Anna luku tai lopeta painamalla Enter: ")
suurin = int(lukuStr)
pienin = int(lukuStr)
while lukuStr != "": 
    lukuStr = input("Anna luku tai lopeta painamalla Enter: ")
    if lukuStr != "":
        lukuInt = int(lukuStr)
        if lukuInt > suurin:
            suurin = lukuInt
        if lukuInt < pienin:
            pienin = lukuInt
    print(suurin)
    print(pienin)