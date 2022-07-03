import json
global json_object

def load (file,):
    a_file = open(str(file)+".json", "r")
    global json_object
    json_object = json.load(a_file)
    a_file.close()

def dump (file):
    a_file = open(str(file)+".json", "w")
    json.dump(json_object, a_file, indent=4)
    a_file.close()

def write(name, type = None, eigenschaften = None, crafting = None, efekt = None, wert = 0, quelle = None):
    load("daten")
    data = json_object
    try:
        data["items"][name]
        if str(type) == "":
            type = data["items"][name]["Type"]
        if str(eigenschaften) == "":
            eigenschaften = data["items"][name]["Eigenschaften"]
        if str(crafting) == "":
            crafting = data["items"][name]["Crafting"]
        if str(efekt) == "":
            efekt = data["items"][name]["Efekt"]
        if str(wert) == "":
            wert = data["items"][name]["Wert"]
        if str(quelle) == "":
            quelle = data["items"][name]["Quelle"]
    except:
        None
    x = {
        "Type": str(type),
        "Wert": str(wert),
        "Crafting": str(crafting),
        "Efekt": str(efekt),
        "Eigenschaften": str(eigenschaften),
        "Quelle": str(quelle)
    }
    data["items"][str(name)] = x
    dump("daten")
    print(str(name)+ " wurde hinzugefüght")

def eingabe():
    name = input("Item Name: ")
    type = input("Item type: ")
    wert = input("Wert: ")
    efekt = input("Efekt: ")
    eingenschaften = input("eigenschaften: ")
    crafting = input("Crafting: ")
    quelle = input("Quelle: ")
    write(name, type = type, wert = wert, eigenschaften = eingenschaften, efekt = efekt, crafting=crafting, quelle=quelle)

def entfernen():
    item = input("Name: ")
    load("daten")
    data = json_object
    try:
        print(data)
        data = data["items"].pop(item)
        dump("daten")
    except:
        print("Item konnte nicht gelöscht werden")

load("daten")
print("item hinzufügen: 1 \nitem löschen: 2")
a_d = input()
if a_d == "1":
    while 1 == 1:
        eingabe()

if a_d == "2":
    while 1 == 1:
        entfernen()