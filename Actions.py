class Actions:
    def __init__(self):
        self.NewRecord = "novi zapis"


    def extrudion(self, end_date_time, id, rn, quantity, worker_id):
        #id, rn, quantity, end_date_time
        record = []
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "ekstrudiranje"
        self.quantity = quantity
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id

        record = [self.id, self.rn, self.quantity, self.end_date_time, None]

        return record


    def cleaning(self, end_date_time, id, rn, worker_id):
        record = []
        self.end_date_time = end_date_time
        self.id = id
        self.rn = rn
        self.activity = "čišćenje radnog mesta"
        self.quantity = None
        self.equipment = "ZSK43"        #treba da je dinaično na osnovu odabrane opreme
        self.worker_id = worker_id

        record = [self.id, self.rn, self.quantity, self.end_date_time, None]

        return record
