from Actions import Actions
import datetime
from pprint import pprint

# hardkord inputi, treba napraviti funkcije za imput od strane operatera: QR kod, brojevi itd
end_date_time = datetime.datetime.now()
id = "42100406"
rn = "1234567"
activity = "ekstrudiranje" # ovo treba da je promenjiva koja se sama menja na osnovu odabrane aktivnosti
quantity = 260
worker_id = "5" #id radnika je od 2 pa do 26 - stim što može da se dodaje borj kako se budu zapošljavali novi radnici

# new_record = [end_date_time.strftime("%d/%m/%Y %H:%M"), id, rn, quantity, None]
new_record = Actions()
pprint(vars(new_record))

new_record.extrudion(end_date_time, id, rn, quantity, worker_id)
# pprint(vars(new_record))

print(new_record.end_date_time)
print(new_record.id)
print(new_record.rn)
print(new_record.activity)
print(new_record.quantity)
print(new_record.equipment)
print(new_record.worker_id)

new_record.cleaning(end_date_time, id, rn, worker_id)
# pprint(vars(new_record))

# kod koji će svai atribut da stavlja u posebnu kolonu u csv fajlu
print(new_record.end_date_time)
print(new_record.id)
print(new_record.rn)
print(new_record.quantity)
print(new_record.equipment)
print(new_record.activity)
print(new_record.worker_id)
