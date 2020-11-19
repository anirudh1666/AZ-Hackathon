import tkinter as tk

def car_footprint(miles):
    return int(miles)*728/(1500*1000)

#14g per passenger mile for train
def train_footprint(miles):
    return 14/(1000*1000)*int(miles)

#80g per passenger mile for bus
def bus_footprint(miles):
    return 80/(1000*1000)*int(miles)

#0.256 kg of CO2 per kWh of electricity and 0.184kg per kWh of gas.
def elec_footprint(kwh):
    return 0.256*int(kwh)/1000

def gas_footprint(kwh):
    return 0.184*int(kwh)/1000


class User:
    
    def __init__(self):

        self.__dist_by_car = None
        self.__dist_by_train = None
        self.__dist_by_bus = None
        self.__electricity_use = None
        self.__gas_use = None
        self.calc_label = tk.Label(gui, text="", fg="black", bg="white")
        
        
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

    def calculate(self, text_output):
        if text_output != "No Error":
            self.calc_label.configure(text=text_output, fg="black", bg="red")
            self.calc_label.pack()
        else: #Replace the else statement so that the text = the calculation
            print(self)
            c = car_footprint(self.__dist_by_car) + train_footprint(self.__dist_by_train) + bus_footprint(self.__dist_by_bus) + elec_footprint(self.__electricity_use) + gas_footprint(self.__gas_use)
            footprint = "Carbon footprint per month: " + str(round(c*1000, 3)) + " kg"
            self.calc_label.configure(text=footprint, fg="black", bg="white")
            self.calc_label.pack()

            return c


gui = tk.Tk()

def isIntFormat(a):
    try:
        a = int(a)
        return 0
    except:
        return 1

def run():
    def checkAll():
        r = int()
        error1 = str("")
        error2 = str("")
        
        c = car_entry.get()
        t = train_entry.get()
        b = bus_entry.get()
        e = electricity_entry.get()
        g = gas_entry.get()

        r = isIntFormat(c)
        if r == 1: error1+= "Car distance, "
        else: c = int(c)
        r = isIntFormat(t)
        if r == 1: error1+= "Train distance, "
        else: t = int(t)
        r = isIntFormat(b)
        if r == 1: error1+= "Bus distance, "
        else: b = int(b)
        r = isIntFormat(e)
        if r == 1: error1+= "Electricity, "
        else: e = int(e)
        r = isIntFormat(g)
        if r == 1: error1+= "Gas, "
        else: g = int(g)

        if error1 != "":
            if error1.count(',') == 1:
                error1 = error1[:-2] + " is not an integer."
            else:
                error1 = error1[:-2] + " are not integers."
            user.calculate(error1)
            return()

        if c < 0: error2 += "Car Distance, "
        if t < 0: error2 += "Train Distance, "
        if b < 0: error2 += "Bus Distance, "
        if e < 0: error2 += "Electricity, "
        if g < 0: error2 += "Gas, "

        if error2 != "":
            if error2.count(',') == 1:
                error2 = error2[:-2] + " is not positive."
            else:
                error2 = error2[:-2] + " are not positive."
            user.calculate(error2)
            return()

        setAll()
        
    def setAll():
        c = car_entry.get()
        t = train_entry.get()
        b = bus_entry.get()
        e = electricity_entry.get()
        g = gas_entry.get()
        
        user.set_car_dist(c)
        user.set_train_dist(t)
        user.set_bus_dist(b)
        user.set_electricity(e)
        user.set_gas(g)
        
        footprint = user.calculate("No Error")
        over_year = footprint * 12
        avg_label = tk.Label(gui, text="", fg="black", bg="white")
        if over_year > 4:
            avg_label.configure(text="Your carbon footprint is above the average, try to reduce it!", fg="black", bg="white")
            avg_label.pack()
        else:
            avg_label.configure(text="Your carbon footprint is below the average, good job!", fg="black", bg="white")
            avg_label.pack()
        
    
    title_label = tk.Label(gui, text="Calculate your monthly carbon footprint")
    title_label.pack()
    
    car_label = tk.Label(gui, text="Enter distance travelled by car to the nearest mile.")
    car_entry = tk.Entry(gui, fg="black", bg="white", width=50)
    car_label.pack()
    car_entry.pack()

    train_label = tk.Label(gui, text="Enter distance travelled by train to the nearest mile.")
    train_entry = tk.Entry(gui, fg="black", bg="white", width=50)
    train_label.pack()
    train_entry.pack()

    bus_label = tk.Label(gui, text="Enter distance travelled by bus to the nearest mile.")
    bus_entry = tk.Entry(gui, fg="black", bg="white", width=50)
    bus_label.pack()
    bus_entry.pack()

    electricity_label = tk.Label(gui, text="Enter electricity usage to the nearest kWh per person in your household.")
    electricity_entry = tk.Entry(gui, fg="black", bg="white", width=50)
    electricity_label.pack()
    electricity_entry.pack()

    gas_label = tk.Label(gui, text="Enter gas usage to the nearest kWh per person in your household.")
    gas_entry = tk.Entry(gui, fg="black", bg="white", width=50)
    gas_label.pack()
    gas_entry.pack()

    b = tk.Button(gui, text="Calculate", command=checkAll)
    b.pack()

    user = User()
    avg_label = tk.Label(gui, text="", fg="black", bg="white")
    

run()
