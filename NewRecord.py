import datetime

class New_Record:
    #constructor
    def __init__(self, end_date_time, id, activity, quantity, equipment, worker_id=5):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = activity
        self.quantity = quantity
        self.equipment = equipment
        self.worker_id = worker_id


class Extruder(New_Record):
    def __init__(self, equipment = "ZSK43"):
        self.equipment = equipment

end_date_time = datetime.datetime.now()
id = "42100406"
rn = "1234567"
# moguće aktivnosti:    "ekstrudiranje", "čišćenje opreme", "čišćenje radnog mesta",
#                       "čekanje probe sa mlina", "kontrola", "kvar", "nema premiksa",
#                       "zagrevanje", "nema operatera"
activity = "nema operatera" # ovo treba da je promenjiva koja se sama menja na osnovu odabrane aktivnosti
quantity = 260
equipment = "ZSK43" #treba da je dinaično na osnovu odabrane opreme
worker_id = "2"

new_ = New_Record(end_date_time, id, activity, quantity, equipment, worker_id)
print(new_.end_date_time)
print(new_.id)
print(new_.rn)
print(new_.quantity)
print(new_.equipment)
print(new_.activity)
print(new_.worker_id)

new_ = Extruder(equipment)
print(new_.end_date_time)
print(new_.id)
print(new_.rn)
print(new_.quantity)
print(new_.equipment)
print(new_.activity)
print(new_.worker_id)
