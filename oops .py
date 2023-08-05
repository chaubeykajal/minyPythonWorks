import datetime 
today=datetime.date(2022,12,13)
print(today.year)
print(today.month)
print(today.day)
print(today.weekday())#[0-monday,1-tuesday,2-wednesday........so on]


class wizcoin:
    def __init__(self, knuts,sickles, gallons):
        self.knuts=knuts
        self.sickles=sickles
        self.gallons=gallons
        
    def value(self):
        print(self.gallons*17*29)
    def weightgrams(self):
        print( self.gallons+self.sickles*10+self.knuts*5)
    
# class aa(wizcoin):
#     def bark(self):
#         print("vvvv")
# a=aa(3,6,9)
# a.value()
# a.weightgrams()


purse=wizcoin(2,5,99)
print(purse.knuts)
print(purse.sickles)
print(purse.gallons)
# print(purse.value())
# print(purse.weightgrams())
    





