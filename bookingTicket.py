def singleTon(arg):
    l = []
    def inner():
        if len(l) == 0:
            obj = arg()
            l.append(obj)
        return l[0]
    return inner

@singleTon
class movie1:
    def __init__(self):
        self.total = 200
    
    def Booking(self):
        requird = int(input("Enter how many tickets to book: "))
        if requird <= self.total:
            self.total -= requird
            print(f"Available tickets: {self.total}")
        else:
            print("Not enough tickets available")

@singleTon
def BoxOffice():
    print(" 1)paytm \n 2)phonepay \n 3)amazonpay \n 4)BMyShow")
    choice = int(input("select which platform u want..:"))
    if choice == 1:
        print('paytm')
        user = movie1()
        user.Booking()
        print('Tickets bookes successfully')
    elif choice == 2:
        print('phonepay')
        user = movie1()
        user.Booking()
        print('Tickets bookes successfully')
    elif choice == 3:
        print('amazonpay')
        user = movie1()
        user.Booking()
        print('Tickets bookes successfully')
    elif choice == 4:
        print('BMyShow')
        user = movie1()
        user.Booking()
        print('Tickets bookes successfully')
    else:
        print("no tickes availble")
BoxOffice()
print('_' * 20)


