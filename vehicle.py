class Vehicle:
    def __init__(self, regno: str, make: str, yearofmanufacture: int, value: float):
        self.regno = regno
        self.make = make
        self.yearofmanufacture = yearofmanufacture
        self.value = value
    def getregnumber(self) -> str:
        return self.regno
    def getmake(self) -> str:
        return self.make
    def getyear(self) -> int:
        return self.yearofmanufacture
    def getvalue(self) -> float:
        return self.value
    def setvalue(self, value: float):
        self.value = value
    def calculateage(self, current_year: int) -> int:
        return current_year - self.yearofmanufacture

class SecondHandVehicle(Vehicle):
    def __init__(self, regno: str, make: str, yearofmanufacture: int, value: float, numberofowners: int):
        super().__init__(regno, make, yearofmanufacture, value)
        self.numberofowners = numberofowners
    def getnumberofowners(self) -> int:
        return self.numberofowners
    def sellvehicle(self, new_value: float):
        self.setvalue(new_value)
        self.numberofowners += 1
