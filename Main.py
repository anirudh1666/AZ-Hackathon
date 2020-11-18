import tkinter as tk

class User:
    
    def __init__(self):

        self.__dist_by_car = None
        self.__dist_by_train = None
        self.__dist_by_bus = None
        self.__electricity_use = None
        self.__gas_use = None

    def set_car_dist(self, car_dist):

        self.__dist_by_car = car_dist

    def set_train_dist(self, train_dist):

        self.__dist_by_train = train_dist

    def set_bus_dist(self, bus_dist):

        self.__dist_by_bus = bus_dist

    def set_electricity(self, elec_usage):

        self.__electricity_use = elec_usage

    def set_gas(self, gas_usage):

        self.__gas_use = gas_usage

    def calculate(self):

        # Algorithm to calculate footprint
        pass


gui = tk.Tk()

def run():

    user = User()
    car_label = tk.Label(text="Enter distance travelled by car")
    car_entry = tk.Entry(fg="black", bg="white", width=50)
    car_label.pack()
    car_entry.pack()
    user.set_car_dist(car_entry.get())


    user.calculate()

run()




    
    
