class c1 :
    sn1 ="sn1"

    def __init__(self):
        self.ön1 = "ön1"

    def örn_met1(self):
        self.öm1 = "öm1"
        return self.öm1

    def ortak_metod(self):
        self.om = "ortak c1"
        return self.om


class c2:
    sn2 = "sn2"

    def __init__(self):
        self.ön2 = "ön2"

    def örn_met2(self):
        self.öm2 = "öm2"
        return self.öm2

    def ortak_metod(self):
        self.om = "ortak c2"
        return self.om

class c4(c1,c2):
    pass


c = c4()

print(c.ortak_metod())

print(c.örn_met2())