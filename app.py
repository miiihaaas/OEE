import datetime
import csv
from pprint import pprint
from objects import menu_tree, breakdown_tree

while True:
    #input meni za terminal - naslediće ga kiwy
    print("1 = ekstrudiranje")
    print("2 = mlevenje")
    choose = input(f"Izabei zonu: ")
    if choose == "1":
        print("1 = ekstrudiranje")
        print(" 11 = ZSK43")
        print(" 12 = APV")
        choose = input(f"Izabei ekstruder: ")
    if choose == "11":
        print("1 = ekstrudiranje")
        print(" 11 = ZSK43")
        for i in range (110,120):
            print(f"     {i} = {menu_tree[i]}")
            i += 1
        choose = input(f"Izabei aktivnost: ")
    if choose == "12":
        print("1 = ekstrudiranje")
        for i in range (120,130):
            print(f"     {i} = {menu_tree[i]}")
            i += 1
        choose = input(f"Izabei aktivnost: ")
    if choose == "2":
        print("2 = mlevenje")
        print(" 21 = ACM20")
        print(" 22 = ACM30")
        choose = input(f"Izabei mlin: ")
    if choose == "21":
        print("2 = mlevenje")
        print(" 21 = ACM20")
        for i in range (210,218):
            print(f"     {i} = {menu_tree[i]}")
            i += 1
        choose = input(f"Izabei aktivnost: ")
    if choose == "22":
        print("2 = mlevenje")
        print(" 22 = ACM30")
        for i in range (220,228):
            print(f"     {i} = {menu_tree[i]}")
            i += 1
        choose = input(f"Izabei aktivnost: ")

    if int(choose) < 1:
        break

    file_path = "D:\Mihas\Programming\Python\Projects\OEE\OEE\CollectedData\\"

    # po defoultu je količina 0
    quantity = 0

    # bira opremu na osnovu odabrane aktivnosti
    if choose[:2] in ("11", "12", "21", "22"):
        equipment = menu_tree[int(choose[:2])]

    # definiše ime fajla
    file_name = f"{equipment}.csv"

    print(f"odabrana oprema: {equipment} \\ {menu_tree[int(choose)]}")

    # input id, rn...
    id_ = input("unesi ID materijala: ")
    rn = input("unesi broj RN: ")

    # ako je mlevenje ili ektrudiranje, traži input za količinu
    if choose[:1] == "1":
        atribut_ = "Ekstrudirana"
    elif choose[:1] == "2":
        atribut_ = "Samlevena"


    if choose[-1:] == "0":
        quantity = input(f"{atribut_} količina: ")


    # input aktivnost, operater...
    activity = menu_tree[int(choose)]
    worker_id = input("unesi ID operatera: ")

    # trentno vreme
    end_date_time = datetime.datetime.now()
    # pretvara ga u string koji excel može da poročita kao datum vreme
    end_date_time = end_date_time.strftime("%x %X")


    new_record = [end_date_time, id_, rn, quantity, equipment, activity, worker_id]
    print(new_record)

    #append new_record to CollectedData
    with open(file_path + file_name, "a", encoding='UTF8', newline="") as f:
        writer = csv.writer(f)
        writer.writerow(new_record)
