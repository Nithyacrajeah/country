class P1:
    def m1(self):
        print("inside m1")


class P2 :
    def m2(self):
        print("inside m2")


class P3 (P2,P1):
    def m3(self):
        print("inside m3")


P3 = P3()
P3.m3()
P3.m2()
P3.m1()