class Car:
    def __init__(self,manufacturer, model, make, transmission, color):
        self.manufacturer = manufacturer
        self.model = model
        self.make = make
        self.transmission = transmission
        self.color = color
    def accelerate(self):
        print(self.manufacturer + " - " + self.model + " is moving")

    def stop(self):
        print(self.manufacturer + " - " + self.model + " has stopped")


myCar_1 = Car("Toyota", "Model-1","1990", 5, "Red")
myCar_2 = Car("Maruti", "Model-1","1990", 5, "Red")
myCar_3 = Car("MG", "Model-1","1990", 5, "Red")

myCar_1.accelerate()
myCar_1.stop()


