class Vehicles:
    """Class for describing vehicles"""

    def __init__(self, name):
        self.namevar= name
        self.wheels= 0
        self.doors=0
        self.seats=0
        self.passengers1=[]

        def num_wheels(self,wheels):
            self.wheels = wheels
        def num_dors(self,doors):
            self.doors = doors
        def num_seats(self,seats):
            self.seats = seats
        def add_pass(self, passengers):
            self.passengers1.append(passengers)



v1 = Vehicles("Car")
print (v1.namevar)
v1.wheels="4 wheels"
print (v1.wheels)
v1.doors= "6 doors"
print(v1.doors)
v1.seats= "9 seats"
print(v1.seats)

v1.add_pass("Gaby")
print(v1.passengers1)
my_list = ["Johnny","Bob","Mary","Mily"]
v1.add_pass(my_list)
print(v1.passengers)






v2 = Vehicles("Truck")
print (v2.namevar)
