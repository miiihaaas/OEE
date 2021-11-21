import datetime
import csv
from pprint import pprint

# Menu tree
menu_tree = {1: "ekstrudiranje",
            11: "ZSK43",
            110: "ekstrudiranje",
            111: "čišćenje",
            112: "čišćenje radnog mesta",
            113: "čekanje probe sa mlina",
            114: "kontrola",
            115: "kvar",
            116: "nema premiksa",
            117: "nema konejnera za čips",
            118: "zagrevanje",
            119: "nema operatera",
            12: "APV",
            120: "ekstrudiranje",
            121: "čišćenje",
            122: "čišćenje radnog mesta",
            123: "čekanje probe sa mlina",
            124: "kontrola",
            125: "kvar",
            126: "nema premiksa",
            127: "nema konejnera za čips",
            28: "zagrevanje",
            129: "nema operatera",
            2: "mlevenje",
            21: "ACM20",
            210: "mlevenje",
            211: "čišćenje",
            212: "čišćenje radnog mesta",
            213: "kontrola",
            214: "kvar",
            215: "nema čipsa",
            216: "pražnjenje filtera",
            217: "nema operatera",
            22: "ACM30",
            220: "mlevenje",
            221: "čišćenje",
            222: "čišćenje radnog mesta",
            223: "kontrola",
            224: "kvar",
            225: "nema čipsa",
            226: "pražnjenje filtera",
            227: "nema operatera"
      }

pprint(menu_tree)
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
    print("     110 = ekstrudiranje")
    print("     111 = čišćenje")
    print("     112 = čišćenje radnog mesta")
    print("     113 = čekanje probe sa mlina")
    print("     114 = kontrola")
    print("     115 = kvar")
    print("     116 = nema premiksa")
    print("     117 = nema konejnera za čips")
    print("     118 = zagrevanje")
    print("     119 = nema operatera")
    choose = input(f"Izabei aktivnost: ")
if choose == "12":
    print("1 = ekstrudiranje")
    print(" 12 = APV")
    print("     120 = ekstrudiranje")
    print("     121 = čišćenje")
    print("     122 = čišćenje radnog mesta")
    print("     123 = čekanje probe sa mlina")
    print("     124 = kontrola")
    print("     125 = kvar")
    print("     126 = nema premiksa")
    print("     127 = nema konejnera za čips")
    print("     128 = zagrevanje")
    print("     129 = nema operatera")
    choose = input(f"Izabei aktivnost: ")
if choose == "2":
    print("2 = mlevenje")
    print(" 21 = ACM20")
    print(" 22 = ACM30")
    choose = input(f"Izabei mlin: ")
if choose == "21":
    print("2 = mlevenje")
    print(" 21 = ACM20")
    print("     210 = mlevenje")
    print("     211 = čišćenje")
    print("     212 = čišćenje radnog mesta")
    print("     213 = kontrola")
    print("     214 = kvar")
    print("     215 = nema čipsa")
    print("     216 = pražnjenje filtera")
    print("     217 = nema operatera")
    choose = input(f"Izabei aktivnost: ")
if choose == "22":
    print("2 = mlevenje")
    print(" 22 = ACM20")
    print("     220 = mlevenje")
    print("     221 = čišćenje")
    print("     222 = čišćenje radnog mesta")
    print("     223 = kontrola")
    print("     224 = kvar")
    print("     225 = nema čipsa")
    print("     226 = pražnjenje filtera")
    print("     227 = nema operatera")
    choose = input(f"Izabei aktivnost: ")


quantity = 0


if choose[:2] == "11":
    equipment = "ZSK43"
elif choose[:2] == "12":
    equipment = "APV"
elif choose[:2] == "21":
    equipment = "ACM20"
elif choose[:2] == "22":
    equipment = "ACM30"


file_name = f"{equipment}.csv"
print(equipment)
print(file_name)

id_ = input("unesi ID materijala: ")
rn = input("unesi broj RN: ")

if choose[:1] == "1":
    atribut_ = "Ekstrudirana"
elif choose[:1] == "2":
    atribut_ = "Samlevena"


if choose[-1:] == "0":
    quantity = input(f"{atribut_} količina: ")



activity = menu_tree[int(choose)]
worker_id = input("unesi ID operatera: ")




# definisane variable sa defoult vrednostima 0
file_path = "D:\Mihas\Programming\Python\Projects\OEE\OEE\\"
file_name = "CollectedData.csv"


end_date_time = datetime.datetime.now()
#pretvara ga u string koji excel može da poročita kao datum vreme
end_date_time = end_date_time.strftime("%x %X")




#hardkord inputi, treba napraviti funkcije za imput od strane operatera: QR kod, brojevi itd

# moguće aktivnosti:    "ekstrudiranje", "čišćenje opreme", "čišćenje radnog mesta",
#                       "čekanje probe sa mlina", "kontrola", "kvar", "nema premiksa",
#                       "zagrebanje", "nema operatera"
# activity = "čišćenje radnog mesta" # ovo treba da je promenjiva koja se sama menja na osnovu odabrane aktivnosti

new_record = [end_date_time, id_, rn, quantity, equipment, activity, worker_id]
print(new_record)

#append new_record to CollectedData
with open(file_path + file_name, "a", encoding='UTF8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_record)
