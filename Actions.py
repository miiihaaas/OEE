class Actions:
    def __init__(self):
        self.NewRecord = "novi zapis"


    def extrudion(self, end_date_time, id, rn, quantity, worker_id):
        #id, rn, quantity, end_date_time
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "ekstrudiranje"
        self.quantity = quantity
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id



    def cleaning(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "čišćenje opreme"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id


    def cleaning_work_space(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "čišćenje radnog mesta"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id


    def probe_from_mill(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "čekanje probe sa mlina"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id


    def quality_control(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "kontrola"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id


    def brakedown(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "kvar"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id
        #dodati ID kvarova

    def no_premix(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "nema premiksa"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id

    def warm_up(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "zagrevanje"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id

    def no_operator(self, end_date_time, id, rn, worker_id):
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "nema operatora"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id
