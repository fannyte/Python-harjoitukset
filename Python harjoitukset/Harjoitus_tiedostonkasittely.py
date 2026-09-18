# with open("save.txt", "w") as tiedosto:
    # tiedosto.write("Ohjelmointi on kivaa perjantaisin")

with open("save.txt", "r") as tiedosto:
    data = tiedosto.read()
    print(data)