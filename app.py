import datetime
import csv


# definisane variable sa defoult vrednostima 0
end_date_time = 0
id_ = 0
rn = 0
activity = 0
quantity = 0
equipment = 0
worker_id = 0

new_record = [end_date_time, id_, rn, activity, quantity, equipment, worker_id]
print(new_record)

#hardkord inputi, treba napraviti funkcije za imput od strane operatera: QR kod, brojevi itd
end_date_time = datetime.datetime.now()
print(end_date_time)
#pretvara ga u string koji excel može da poročita kao datum vreme
end_date_time = end_date_time.strftime("%x %X")
print(end_date_time)
id_ = "42509406"
rn = "1903425"
# moguće aktivnosti:    "ekstrudiranje", "čišćenje opreme", "čišćenje radnog mesta",
#                       "čekanje probe sa mlina", "kontrola", "kvar", "nema premiksa",
#                       "zagrebanje", "nema operatera"
activity = "ekstrudiranje" # ovo treba da je promenjiva koja se sama menja na osnovu odabrane aktivnosti
quantity = 520
equipment = "ZSK43" #treba da je dinaično na osnovu odabrane opreme
worker_id = "5" #id radnika je od 2 pa do 26 - stim što može da se dodaje borj kako se budu zapošljavali novi radnici

new_record = [end_date_time, id_, rn, activity, quantity, equipment, worker_id]
print(new_record)

#append new_record to CollectedData
with open("D:\Mihas\Programming\Python\Projects\OEE\OEE\CollectedData.csv", "a", encoding='UTF8', newline="") as f:
    writer = csv.writer(f)
    writer.writerow(new_record)
