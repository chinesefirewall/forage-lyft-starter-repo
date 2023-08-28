import unittest
from datetime import date
from battery.battery import SpindlerBattery, NubbinBattery

class TestBattery(unittest.TestCase):

    def test_spindler_battery_needs_service_upgrade(self):
        last_service_date = date(2020, 1, 1)
        current_date = date(2023, 1, 1)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

        current_date = date(2022, 12, 31)
        battery = SpindlerBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

    def test_nubbin_battery_needs_service(self):
        last_service_date = date(2022, 1, 1)
        current_date = date(2022, 4, 1)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertTrue(battery.needs_service())

        current_date = date(2022, 3, 31)
        battery = NubbinBattery(last_service_date, current_date)
        self.assertFalse(battery.needs_service())

if __name__ == '__main__':
    unittest.main()
