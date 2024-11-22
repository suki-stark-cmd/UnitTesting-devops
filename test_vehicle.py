import unittest
from vehicle import Vehicle, SecondHandVehicle

class TestVehicle(unittest.TestCase):

    def test_vehicle_creation(self):
        vehicle = Vehicle("ABC123", "Toyota", 2015, 15000.0)
        self.assertEqual(vehicle.getregnumber(), "ABC123")
        self.assertEqual(vehicle.getmake(), "Toyota")
        self.assertEqual(vehicle.getyear(), 2015)
        self.assertEqual(vehicle.getvalue(), 15000.0)

    def test_calculate_age(self):
        vehicle = Vehicle("XYZ987", "Honda", 2010, 10000.0)
        current_year = 2024
        self.assertEqual(vehicle.calculateage(current_year), 14)

    def test_set_value(self):
        vehicle = Vehicle("DEF456", "Ford", 2018, 20000.0)
        vehicle.setvalue(18000.0)
        self.assertEqual(vehicle.getvalue(), 18000.0)


class TestSecondHandVehicle(unittest.TestCase):

    def test_secondhandvehicle_creation(self):
        shv = SecondHandVehicle("LMN789", "BMW", 2017, 25000.0, 2)
        self.assertEqual(shv.getregnumber(), "LMN789")
        self.assertEqual(shv.getmake(), "BMW")
        self.assertEqual(shv.getyear(), 2017)
        self.assertEqual(shv.getvalue(), 25000.0)
        self.assertEqual(shv.getnumberofowners(), 2)

    def test_sell_vehicle(self):
        shv = SecondHandVehicle("LMN789", "BMW", 2017, 25000.0, 2)
        shv.sellvehicle(24000.0)
        self.assertEqual(shv.getvalue(), 24000.0)
        self.assertEqual(shv.getnumberofowners(), 3)

    def test_calculate_age_for_secondhand(self):
        shv = SecondHandVehicle("XYZ111", "Audi", 2012, 22000.0, 3)
        current_year = 2024
        self.assertEqual(shv.calculateage(current_year), 12)


if __name__ == "__main__":
    unittest.main()
